class ModelSelector:
    """Selects the best free AI model for each task"""
    
    def __init__(self):
        # Keep selector focused on stable, supported models only.
        self.models = {
            'gemini-1.5-flash': {
                'name': 'Google Gemini 1.5 Flash',
                'strengths': ['analysis', 'multilingual', 'business', 'learning'],
                'languages': ['tamil', 'english', 'tanglish'],
                'best_for': ['business', 'analysis', 'learning']
            },
            'mixtral-8x7b-32768': {
                'name': 'Mixtral 8x7B',
                'strengths': ['coding', 'creative', 'reasoning'],
                'languages': ['english'],
                'best_for': ['coding', 'creative_writing']
            }
        }
    
    def select(self, intent, language):
        """Select best model based on intent and language"""
        scores = {}
        
        for model_name, capabilities in self.models.items():
            score = 0
            
            if language in capabilities['languages']:
                score += 3
            
            if intent in capabilities['best_for']:
                score += 5
            
            scores[model_name] = score
        
        best_model = max(scores.items(), key=lambda x: x[1])[0]
        model_info = self.models[best_model]
        
        return {
            'model': best_model,
            'name': model_info['name'],
            'reason': f"Best for {intent} in {language}",
            'description': f"{model_info['name']} selected"
        }
