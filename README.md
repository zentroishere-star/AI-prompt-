# AI Prompt Optimizer

A sophisticated Django-based web application that optimizes user prompts for AI interactions, featuring intelligent intent classification, multilingual support (English, Tamil, Tanglish), and seamless integration with multiple AI models including Google Gemini and Groq.

## 🚀 Features

### Core Functionality
- **Intelligent Prompt Enhancement**: Transforms casual user input into optimized, structured prompts for better AI responses
- **Multilingual Support**: Native support for English, Tamil, and Tanglish (Tamil-English mix)
- **Intent Classification**: Automatically categorizes queries into domains like creative writing, coding, business analysis, etc.
- **Smart Model Selection**: Dynamically selects the best AI model based on intent and language requirements

### AI Integration
- **Google Gemini**: Latest Gemini models for analysis, multilingual tasks, and business applications
- **Groq**: High-performance Llama models for coding, creative writing, and reasoning tasks
- **Automatic Fallback**: Seamless fallback between models when quotas are exceeded or models are unavailable

### User Experience
- **User Authentication**: Secure user accounts with profile management
- **Query History**: Track and review past interactions
- **Feedback System**: Rate and provide feedback on AI responses
- **Responsive Design**: Modern, mobile-friendly web interface

## 🛠️ Technology Stack

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, JavaScript
- **AI APIs**: Google Generative AI, Groq
- **Database**: SQLite (development), PostgreSQL (production)
- **Styling**: Custom CSS with responsive design

## 📋 Prerequisites

- Python 3.8+
- Git
- API keys for Google Gemini and Groq

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/prakashmurugan01/AI-Prompt-Optimizer.git
   cd ai-prompt-optimizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   - Copy `.env.example` to `.env.local` and update API keys:
   ```bash
   cp .env.example .env.local
   ```
   - Edit `.env.local` with your API keys:
   ```
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   GEMINI_API_KEY=your_gemini_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

## 🚀 Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`
   - Register a new account or login
   - Start optimizing your prompts with the AI assistant

## 📖 Usage

### For Users
1. **Register/Login**: Create an account to access the chatbot
2. **Chat Interface**: Enter your query in natural language
3. **Automatic Optimization**: The system enhances your prompt and selects the best AI model
4. **Review History**: Check your past queries and responses
5. **Provide Feedback**: Rate responses to help improve the system

### For Developers
- **API Endpoints**: RESTful API available for integration
- **Modular Services**: Easily extensible service architecture
- **Intent Classification**: Add new intent categories and keywords
- **Model Integration**: Add support for additional AI providers

## 🏗️ Project Structure

```
ai_prompt_optimizer/
├── accounts/              # User authentication app
├── chatbot/               # Main chatbot functionality
│   ├── services/          # AI services and utilities
│   │   ├── ai_caller.py       # AI API integrations
│   │   ├── intent_classifier.py # Query categorization
│   │   ├── language_detector.py  # Language detection
│   │   ├── model_selector.py     # Model selection logic
│   │   └── prompt_enhancer.py    # Prompt optimization
│   └── models.py          # Database models
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
├── ai_prompt_optimizer/   # Django project settings
└── manage.py             # Django management script
```

## 🔑 API Keys Setup

### Google Gemini API
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to your `.env.local` file: `GEMINI_API_KEY=your_key_here`

### Groq API
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and generate an API key
3. Add to your `.env.local` file: `GROQ_API_KEY=your_key_here`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the Gemini AI models
- Groq for providing fast inference APIs
- Django community for the excellent web framework
- All contributors and users of this project

## 📞 Support

For support, please:
- Create an issue in this repository
- Email support@aipromptoptimizer.com
- Check existing issues for solutions

## 🔄 Future Enhancements

- [ ] Support for additional AI providers (OpenAI, Anthropic)
- [ ] Voice input/output capabilities
- [ ] Advanced analytics dashboard
- [ ] API rate limiting and caching
- [ ] Multi-language UI support
- [ ] Integration with popular platforms (Slack, Discord)
- [ ] Real-time collaboration features
- [ ] Prompt templates library