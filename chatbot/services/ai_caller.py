import os


class AICaller:
    """Calls free AI model APIs"""
    
    def __init__(self):
        self.gemini_key = os.getenv('GEMINI_API_KEY')
        self.groq_key = os.getenv('GROQ_API_KEY')
    
    def call_gemini(self, prompt):
        """Call Google Gemini API"""
        try:
            import google.generativeai as genai
            
            if not self.gemini_key:
                return {
                    'success': False,
                    'error': 'Gemini API key not configured'
                }
            
            genai.configure(api_key=self.gemini_key)
            
            # Try gemini-2.0-flash first, fallback to 1.5-flash
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
            except:
                model = genai.GenerativeModel('gemini-1.5-flash')
            
            response = model.generate_content(prompt)
            
            return {
                'success': True,
                'response': response.text
            }
        except Exception as e:
            error_str = str(e)
            # If quota exceeded, suggest using Groq instead
            if '429' in error_str or 'quota' in error_str.lower():
                return {
                    'success': False,
                    'error': 'Gemini quota exceeded. Using Groq instead...',
                    'fallback': True
                }
            return {
                'success': False,
                'error': f'Gemini error: {error_str}'
            }
    
    def call_groq(self, prompt, model='llama-3.1-70b-versatile'):
        """Call Groq API (Llama or Mixtral). Tries a short, stable fallback list.
        If all fallbacks fail, returns an informative error asking the developer to
        check available models in the Groq console.
        """
        try:
            from groq import Groq
            
            if not self.groq_key:
                return {
                    'success': False,
                    'error': 'Groq API key not configured'
                }

            client = Groq(api_key=self.groq_key)

            # Small, explicit list of stable models to try (avoid models known to be decommissioned)
            fallback_models = []
            if model:
                fallback_models.append(model)
            # Add fallback models in order of preference
            if 'llama-3.1-70b-versatile' not in fallback_models:
                fallback_models.append('llama-3.1-70b-versatile')
            if 'llama-3.1-8b-instant' not in fallback_models:
                fallback_models.append('llama-3.1-8b-instant')

            last_error = None
            for try_model in fallback_models:
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model=try_model,
                    )
                    return {
                        'success': True,
                        'response': chat_completion.choices[0].message.content,
                        'used_model': try_model
                    }
                except Exception as e:
                    last_error = str(e)
                    # If model decommissioned, try the next one; otherwise stop
                    if 'decommissioned' in last_error.lower() or 'deprecated' in last_error.lower():
                        continue
                    else:
                        break

            # If we reached here, none of the fallbacks succeeded
            return {
                'success': False,
                'error': (
                    "Groq error: all attempted models failed. "
                    "Last error: " + (last_error or 'unknown') + ".\nPlease check your Groq account and available models: https://console.groq.com/docs/deprecations"
                )
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Groq error: {str(e)}'
            }
    
    def call_model(self, model_name, prompt):
        """Route to appropriate API"""
        if 'gemini' in model_name:
            result = self.call_gemini(prompt)
            # If Gemini is rate-limited, fallback to Groq
            if result.get('fallback'):
                return self.call_groq(prompt, 'llama-3.1-70b-versatile')
            return result
        else:
            return self.call_groq(prompt, model_name)
