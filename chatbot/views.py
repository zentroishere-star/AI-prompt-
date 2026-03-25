from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .models import Query, Feedback
from .services.language_detector import LanguageDetector
from .services.intent_classifier import IntentClassifier
from .services.prompt_enhancer import PromptEnhancer
from .services.model_selector import ModelSelector
from .services.ai_caller import AICaller


@login_required(login_url='login')
def dashboard_view(request):
    """Main dashboard with chatbot interface"""
    return render(request, 'chatbot/dashboard.html')


@login_required(login_url='login')
@require_POST
def enhance_prompt_api(request):
    """API endpoint to enhance prompts"""
    try:
        data = json.loads(request.body)
        user_input = data.get('user_input', '').strip()
        
        if not user_input:
            return JsonResponse({'error': 'No input provided'}, status=400)
        
        # Check credits
        user_profile = request.user.userprofile
        if user_profile.credits < 1:
            return JsonResponse({'error': 'No credits remaining'}, status=403)
        
        # Initialize services
        lang_detector = LanguageDetector()
        intent_classifier = IntentClassifier()
        prompt_enhancer = PromptEnhancer()
        model_selector = ModelSelector()
        ai_caller = AICaller()
        
        # Process query
        language = lang_detector.detect(user_input)
        intent = intent_classifier.classify(user_input)
        enhanced = prompt_enhancer.enhance(user_input, language, intent)
        model_info = model_selector.select(intent, language)
        ai_response_data = ai_caller.call_model(model_info['model'], enhanced)
        
        # Get AI response
        if ai_response_data['success']:
            ai_response = ai_response_data['response']
        else:
            ai_response = f"Error: {ai_response_data.get('error', 'Unknown')}"
        
        # Save to database
        Query.objects.create(
            user=request.user,
            original_input=user_input,
            detected_language=language,
            detected_intent=intent,
            enhanced_prompt=enhanced,
            selected_model=model_info['model'],
            ai_response=ai_response
        )
        
        # Deduct credit
        user_profile.credits -= 1
        user_profile.save()
        
        return JsonResponse({
            'success': True,
            'detected_language': language,
            'detected_intent': intent,
            'enhanced_prompt': enhanced,
            'model_info': model_info,
            'ai_response': ai_response,
            'remaining_credits': user_profile.credits,
            'api_success': ai_response_data['success']
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required(login_url='login')
def history_view(request):
    """Display query history"""
    queries = Query.objects.filter(user=request.user).order_by('-created_at')[:50]
    return render(request, 'chatbot/history.html', {'queries': queries})


@login_required(login_url='login')
def query_detail_view(request, query_id):
    """Display details of a specific query"""
    query = get_object_or_404(Query, id=query_id, user=request.user)
    return render(request, 'chatbot/query_detail.html', {'query': query})


@login_required(login_url='login')
def feedback_view(request):
    """Feedback submission page"""
    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        title = request.POST.get('title', '').strip()
        message = request.POST.get('message', '').strip()
        
        if not title or not message:
            return JsonResponse({'error': 'Title and message are required'}, status=400)
        
        # Only allow positive feedback (4-5 stars)
        try:
            rating = int(rating)
            if rating < 4:
                return JsonResponse({'error': 'Only positive feedback (4-5 stars) is accepted'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid rating'}, status=400)
        
        feedback = Feedback.objects.create(
            user=request.user,
            rating=rating,
            title=title,
            message=message,
            is_positive=True,
            is_approved=True  # Auto-approve positive feedback
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your feedback!',
            'feedback_id': feedback.id
        })
    
    return render(request, 'chatbot/feedback.html')


def get_positive_feedbacks(request):
    """API to get positive feedbacks for home page (live view)"""
    try:
        feedbacks = Feedback.objects.filter(
            is_positive=True, 
            is_approved=True
        ).order_by('-created_at')[:20]
        
        data = {
            'feedbacks': [
                {
                    'id': f.id,
                    'user': f.user.first_name or f.user.username,
                    'rating': f.rating,
                    'title': f.title,
                    'message': f.message,
                    'created_at': f.created_at.strftime('%B %d, %Y'),
                }
                for f in feedbacks
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e), 'feedbacks': []}, status=500)