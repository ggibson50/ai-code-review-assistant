# AI Code Review Assistant (Phase 1)

## Features
- GitHub OAuth Authentication
- AI-Powered Code Analysis (GPT-4)
- PostgreSQL Database for storing code snippets
- Frontend for code upload & AI feedback

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `.env` with `OPENAI_API_KEY` and database credentials
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Open `frontend/index.html` to interact with the AI
    