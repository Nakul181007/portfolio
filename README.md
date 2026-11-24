# Nakul Dalal — Developer Portfolio

A personal portfolio built to present my software projects, technical skills, and experience.

## Tech stack

### Frontend
- React
- TypeScript
- Tailwind CSS
- Framer Motion
- Vite

### Backend
- Python
- FastAPI
- SQLite

## Features

- Responsive portfolio layout
- Dark/light theme toggle
- Generative neural-network canvas background
- Sections for About, Projects, Skills, Experience, and Contact
- Lazy-loaded page sections
- FastAPI endpoints for portfolio content
- Contact form API with SQLite persistence

## Project structure

```
portfolio/
├── frontend/   # React + TypeScript application
└── backend/    # FastAPI application and SQLite persistence
```

## Run locally

### 1. Start the backend

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API runs at `http://localhost:8000`; interactive API documentation is available at `http://localhost:8000/docs`.

### 2. Start the frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

The Vite development server runs at `http://localhost:5173`. The frontend proxies `/api/*` requests to the backend on port 8000.

## Notes

- The SQLite database is generated locally by the backend; it is not committed to the repository.
- Keep credentials and local environment files out of version control. Use the provided `.env.example` files where applicable.
- This project is actively maintained as my personal developer portfolio.

## Author

**Nakul Dalal**  
Computer Engineering Student | Frontend Development | UI/UX | AI-powered Products

[GitHub](https://github.com/Nakul181007)
