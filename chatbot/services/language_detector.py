import re


class LanguageDetector:
    """Detects Tamil, English, or Tanglish"""
    
    def __init__(self):
        self.tamil_pattern = re.compile(r'[\u0B80-\u0BFF]+')
        self.tanglish_words = [
            'vanakkam', 'nandri', 'seri', 'illa', 'irukku',
            'vanthuten', 'ponga', 'vaanga', 'venum', 'sapadu',
            'panni', 'pannunga', 'sollunga', 'kudukka', 'vena'
        ]
    
    def detect(self, text):
        """Returns: 'tamil', 'english', or 'tanglish'"""
        if not text:
            return 'english'
        
        has_tamil_script = bool(self.tamil_pattern.search(text))
        has_english = bool(re.search(r'[a-zA-Z]+', text))
        
        if has_tamil_script and has_english:
            return 'tanglish'
        elif has_tamil_script:
            return 'tamil'
        elif self._is_tanglish(text):
            return 'tanglish'
        else:
            return 'english'
    
    def _is_tanglish(self, text):
        text_lower = text.lower()
        return any(word in text_lower for word in self.tanglish_words)
