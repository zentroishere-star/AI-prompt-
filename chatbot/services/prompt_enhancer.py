class PromptEnhancer:
    """Transforms casual input into optimized prompts"""
    
    def __init__(self):
        self.templates = {
            'creative_writing': """Create creative content with these requirements:

Topic: {topic}

Requirements:
- Clear beginning, middle, and end
- Engaging narrative with descriptive language
- Well-developed characters (if applicable)
- Length: 500-800 words
- Tone: {tone}

Make it compelling and original.""",

            'coding': """Write {language} code for:

Task: {task}

Requirements:
- Clean, readable code with comments
- Follow best practices
- Include error handling
- Provide usage examples

Context: {context}""",

            'business': """Create a business {document_type} for:

Topic: {topic}

Include:
1. Executive Summary
2. Market Analysis
3. Target Audience
4. Strategy and Approach
5. Financial Considerations
6. Implementation Timeline
7. Success Metrics

Make it specific and actionable.""",

            'analysis': """Provide comprehensive analysis of:

Topic: {topic}

Analysis should include:
- Key points and main ideas
- Comparison with alternatives
- Strengths and weaknesses
- Data-driven insights
- Practical implications
- Conclusion with recommendations

Be thorough and objective.""",

            'email_professional': """Compose a professional {email_type}:

Purpose: {purpose}
Tone: {tone}

Structure:
- Clear subject line
- Professional greeting
- Well-organized body
- Call to action (if needed)
- Professional closing

Ensure proper business etiquette.""",

            'learning': """Explain {topic} in an educational way:

Approach:
- Start with fundamentals
- Use clear, simple language
- Include practical examples
- Provide step-by-step explanations
- Add real-world applications
- Note common mistakes to avoid

Target Level: Intermediate""",

            'conversational': """{original_query}

Please provide a helpful, clear, and engaging response."""
        }
    
    def enhance(self, user_input, language, intent):
        """Enhance user input into structured prompt"""
        template = self.templates.get(intent, self.templates['conversational'])
        enhanced = self._fill_template(template, user_input, intent)
        return enhanced
    
    def _fill_template(self, template, text, intent):
        values = {
            'topic': text,
            'tone': 'professional and engaging',
            'language': 'Python',
            'task': text,
            'context': text,
            'document_type': 'plan',
            'email_type': 'email',
            'purpose': text,
            'original_query': text
        }
        
        try:
            filled = template.format(**values)
        except KeyError:
            filled = template
        
        return filled
