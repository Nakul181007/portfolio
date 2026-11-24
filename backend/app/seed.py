"""Seed verified portfolio data without overwriting existing database content."""
from .database import SessionLocal
from .models import Project, Skill, Experience

PROJECTS = [
    {
        "title": "ClimateAI Maharashtra",
        "description": "International hackathon project: an AI-powered climate accountability and environmental intelligence platform.",
        "long_description": (
            "Built as part of the FCRIT engineering and design team for the PCCOE International Grand Challenge 2026. "
            "The documented prototype combines government climate-policy ingestion, Gemini-assisted policy extraction "
            "and multilingual explanations with deterministic audit calculations, environmental evidence views, "
            "and what-if intervention modelling. Demonstration data is explicitly identified as simulated."
        ),
        "tech_stack": ["TypeScript", "Google Gemini", "React", "Environmental Data", "AI-assisted Analysis"],
        "github_url": "https://github.com/Nakul181007/climate-ai",
        "demo_url": None,
        "featured": 1,
    },
    {
        "title": "CoffeeRide AI",
        "description": "A data-driven GenAI expansion concept that helps coffee businesses evaluate cyclist-friendly locations.",
        "long_description": (
            "Combines Gemini reasoning, BigQuery MCP, public Citi Bike mobility datasets, SQL analytics, "
            "and a weighted Cyclist Opportunity Score to rank potential expansion locations. "
            "The current submitted UI uses representative/demo results; live BigQuery MCP authentication "
            "is not configured in the submission frontend environment."
        ),
        "tech_stack": ["JavaScript", "React", "Tailwind CSS", "Gemini", "BigQuery", "SQL"],
        "github_url": "https://github.com/Nakul181007/CoffeeRide-AI",
        "demo_url": None,
        "featured": 1,
    },
    {
        "title": "Developer Portfolio",
        "description": "A personal portfolio built with React, TypeScript, Tailwind CSS, Framer Motion, and a FastAPI backend.",
        "long_description": (
            "Personal portfolio project with responsive sections for projects, skills, experience, and contact; "
            "theme support; animated visual elements; and API-backed portfolio content."
        ),
        "tech_stack": ["React", "TypeScript", "Tailwind CSS", "Framer Motion", "Python", "FastAPI", "SQLite"],
        "github_url": "https://github.com/Nakul181007/portfolio",
        "demo_url": None,
        "featured": 1,
    },
]

SKILLS = [
    {"name": "C", "category": "Languages", "level": 1},
    {"name": "Java", "category": "Languages", "level": 1},
    {"name": "Python", "category": "Languages", "level": 1},
    {"name": "JavaScript", "category": "Languages", "level": 1},
    {"name": "SQL", "category": "Languages", "level": 1},
    {"name": "HTML", "category": "Frontend", "level": 1},
    {"name": "CSS", "category": "Frontend", "level": 1},
    {"name": "React", "category": "Frontend", "level": 1},
    {"name": "TypeScript", "category": "Frontend", "level": 1},
    {"name": "Tailwind CSS", "category": "Frontend", "level": 1},
    {"name": "UI/UX Design", "category": "Design", "level": 1},
    {"name": "FastAPI", "category": "Backend", "level": 1},
    {"name": "SQLite", "category": "Backend", "level": 1},
    {"name": "Git / GitHub", "category": "Tools", "level": 1},
    {"name": "AI-assisted development tools", "category": "Tools", "level": 1},
    {"name": "Data Structures & Algorithms", "category": "Core", "level": 1},
]

EXPERIENCE = [
    {
        "title": "Participant — Google Gen AI APAC",
        "organization": "Google Gen AI APAC",
        "type": "workshop",
        "start_date": "2026",
        "end_date": None,
        "description": "Participated in the Google Gen AI APAC programme.",
        "location": "Online",
    },
    {
        "title": "International Hackathon Project",
        "organization": "PCCOE International Grand Challenge 2026 — FCRIT team",
        "type": "hackathon",
        "start_date": "2026",
        "end_date": None,
        "description": "Contributed to ClimateAI Maharashtra, an AI-powered climate accountability and environmental intelligence prototype, as part of the FCRIT engineering and design team.",
        "location": "India",
    },
]


def seed():
    """Insert verified starter content only when each table is empty."""
    db = SessionLocal()
    try:
        if db.query(Project).count() == 0:
            db.add_all([Project(**project) for project in PROJECTS])
        if db.query(Skill).count() == 0:
            db.add_all([Skill(**skill) for skill in SKILLS])
        if db.query(Experience).count() == 0:
            db.add_all([Experience(**item) for item in EXPERIENCE])
        db.commit()
        print("[OK] Portfolio starter content checked")
    except Exception as exc:
        db.rollback()
        print(f"[ERROR] Failed to seed database: {exc}")
    finally:
        db.close()
