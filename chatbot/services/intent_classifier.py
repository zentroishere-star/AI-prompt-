class IntentClassifier:
    """Classifies user queries into categories"""
    
    def __init__(self):
        self.intent_keywords = {
            'creative_writing': [
                'story', 'poem', 'write', 'creative', 'script',
                'கதை', 'கவிதை', 'எழுது'
            ],
            'coding': [
                'code', 'program', 'function', 'debug', 'python',
                'javascript', 'html', 'css'
            ],
            'business': [
                'business', 'plan', 'proposal', 'marketing', 'strategy',
                'பிசினஸ்', 'திட்டம்'
            ],
            'analysis': [
                'analyze', 'compare', 'explain', 'research',
                'ஆராய்', 'ஒப்பிடு'
            ],
            'email_professional': [
                'email', 'letter', 'formal', 'professional',
                'மெயில்', 'கடிதம்'
            ],
            'learning': [
                'learn', 'teach', 'explain', 'tutorial', 'how to',
                'கற்று', 'படி'
            ],
            'conversational': [
                'chat', 'talk', 'discuss', 'help',
                'பேசு', 'உதவி'
            ]
        }
    
    def classify(self, text):
        """Returns intent category"""
        if not text:
            return 'conversational'
        
        text_lower = text.lower()
        scores = {}
        
        for intent, keywords in self.intent_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                scores[intent] = score
        
        if scores:
            return max(scores.items(), key=lambda x: x[1])[0]
        
        return 'conversational'
