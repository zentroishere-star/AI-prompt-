from django.db import models
from django.contrib.auth.models import User


class Query(models.Model):
    """Store user queries and AI responses"""
    INTENT_CHOICES = [
        ('creative_writing', 'Creative Writing'),
        ('coding', 'Coding'),
        ('business', 'Business'),
        ('analysis', 'Analysis'),
        ('email_professional', 'Email/Professional'),
        ('learning', 'Learning'),
        ('conversational', 'Conversational'),
    ]
    
    LANGUAGE_CHOICES = [
        ('tamil', 'Tamil'),
        ('english', 'English'),
        ('tanglish', 'Tanglish'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    original_input = models.TextField()
    detected_language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    detected_intent = models.CharField(max_length=100, choices=INTENT_CHOICES, default='conversational')
    enhanced_prompt = models.TextField()
    selected_model = models.CharField(max_length=50)
    ai_response = models.TextField(blank=True, null=True)
    user_rating = models.IntegerField(null=True, blank=True, choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.detected_intent}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Query'
        verbose_name_plural = 'User Queries'


class Feedback(models.Model):
    """Store user feedback and testimonials"""
    RATING_CHOICES = [
        (5, '⭐⭐⭐⭐⭐ Excellent'),
        (4, '⭐⭐⭐⭐ Very Good'),
        (3, '⭐⭐⭐ Good'),
        (2, '⭐⭐ Fair'),
        (1, '⭐ Poor'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_positive = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating} stars"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Customer Feedback'
        verbose_name_plural = 'Customer Feedbacks'

