"""Seed placeholder data into the SQLite database for Nakul Dalal."""
from .database import SessionLocal
from .models import Project, Skill, Experience


PROJECTS = [
    {
        "title": "PrepPortal",
        "description": "A full-stack placement preparation portal with DSA practice, mock aptitude tests, and student analytics.",
        "long_description": (
            "Designed and built a complete placement preparation platform for FCRIT students. "
            "Features include a custom DSA challenge engine with code evaluation metrics, structured "
            "placement roadmaps, aptitude practice dashboards, and peer tracking. The app serves "
            "multiple concurrent users and provides a clean dashboard for students and placement mentors."
        ),
        "tech_stack": ["React", "FastAPI", "Python", "SQLite", "Tailwind CSS", "Axios"],
        "github_url": "https://github.com/nakuldalal/prepportal",
        "demo_url": "https://prepportal.demo.dev",
        "featured": 1,
    },
    {
        "title": "Concurrent HTTPServer",
        "description": "A high-performance multithreaded HTTP/1.1 server built from scratch in C++.",
        "long_description": (
            "Engineered a multithreaded HTTP server using raw C++ socket programming. Implemented "
            "epoll-based I/O multiplexing for asynchronous event handling and a robust thread pool "
            "to process concurrent connection requests. Features custom HTTP request parsing, "
            "static file serving, routing, and sub-10ms response times for 10k+ concurrent requests."
        ),
        "tech_stack": ["C++", "Socket Programming", "epoll", "Multithreading", "Linux"],
        "github_url": "https://github.com/nakuldalal/concurrent-server",
        "demo_url": None,
        "featured": 1,
    },
    {
        "title": "Enterprise Inventory System",
        "description": "A robust, scalable Spring Boot microservices backend for managing enterprise warehouse transactions.",
        "long_description": (
            "Developed an enterprise-grade backend system using Java and Spring Boot. Implemented "
            "JWT security authentication, JPA/Hibernate mapping, PostgreSQL relational schema, "
            "and transactional safety ensuring ACID guarantees across distributed warehouse nodes. "
            "Features automatic email notifications and analytics reports on inventory stock levels."
        ),
        "tech_stack": ["Java", "Spring Boot", "Hibernate", "PostgreSQL", "JWT", "Docker"],
        "github_url": "https://github.com/nakuldalal/enterprise-inventory",
        "demo_url": None,
        "featured": 0,
    },
    {
        "title": "DevPortfolio",
        "description": "Personal developer portfolio (this website) featuring interactive generative visuals and sleek styling.",
        "long_description": (
            "Created an elegant, interactive portfolio utilizing Vite, React, and Tailwind CSS. "
            "Features a custom particle canvas reflecting neural node networks that react dynamically to mouse drift, "
            "smooth scroll animations with Framer Motion, and light/dark theme persistence."
        ),
        "tech_stack": ["React", "Vite", "Tailwind CSS", "Framer Motion", "TypeScript"],
        "github_url": "https://github.com/nakuldalal/portfolio",
        "demo_url": "https://nakuldalal.dev",
        "featured": 0,
    },
]

SKILLS = [
    # Languages
    {"name": "Java", "category": "Languages", "level": 88},
    {"name": "C++", "category": "Languages", "level": 90},
    {"name": "Python", "category": "Languages", "level": 92},
    {"name": "JavaScript", "category": "Languages", "level": 85},
    # Backend
    {"name": "Spring Boot", "category": "Backend", "level": 80},
    {"name": "FastAPI", "category": "Backend", "level": 85},
    {"name": "Node.js", "category": "Backend", "level": 75},
    {"name": "PostgreSQL", "category": "Backend", "level": 82},
    {"name": "SQLite", "category": "Backend", "level": 85},
    # Frontend
    {"name": "React", "category": "Frontend", "level": 90},
    {"name": "TypeScript", "category": "Frontend", "level": 80},
    {"name": "Tailwind CSS", "category": "Frontend", "level": 90},
    {"name": "Framer Motion", "category": "Frontend", "level": 75},
    # Tools
    {"name": "Git / GitHub", "category": "Tools", "level": 92},
    {"name": "Docker", "category": "Tools", "level": 75},
    {"name": "Linux / Bash", "category": "Tools", "level": 80},
    {"name": "VS Code", "category": "Tools", "level": 95},
]

EXPERIENCE = [
    {
        "title": "Software Development Engineer (SDE) Intern",
        "organization": "Financial Technology Group (Placement)",
        "type": "job",
        "start_date": "May 2025",
        "end_date": "Present",
        "description": (
            "Secured a premier software developer internship during the college placement drive. "
            "Contributing to high-throughput backend services using Java/Spring Boot and optimization "
            "of database queries in PostgreSQL, achieving a 15% reduction in latency for API response payloads."
        ),
        "location": "Mumbai, India",
    },
    {
        "title": "Technical Placement Coordinator & Lead",
        "organization": "FCRIT Navi Mumbai",
        "type": "workshop",
        "start_date": "Jun 2024",
        "end_date": "Present",
        "description": (
            "Appointed as technical placement coordinator. Designed and conducted multiple coding bootcamps "
            "covering Data Structures, Algorithms, Java/C++ programming paradigms, and React basics for 150+ peers, "
            "significantly contributing to successful placements across campus batches."
        ),
        "location": "Navi Mumbai, India",
    },
    {
        "title": "Winner — FCRIT Hackathon 2024",
        "organization": "Fr. Conceicao Rodrigues Institute of Technology",
        "type": "hackathon",
        "start_date": "Oct 2024",
        "end_date": None,
        "description": (
            "Led a 4-member team to design and build 'PrepPortal' — a React + Python web application in under "
            "36 hours. Placed 1st out of 40 participating teams for utility, usability, and architecture."
        ),
        "location": "Navi Mumbai, India",
    },
    {
        "title": "Core Developer — FCRIT Capstone Project",
        "organization": "FCRIT Computer Engineering Department",
        "type": "research",
        "start_date": "Jan 2025",
        "end_date": "Apr 2025",
        "description": (
            "Researched and built a multithreaded application server architecture in C++. Analyzed system "
            "performance, context-switching latency under heavy connection load, and compiled findings into "
            "the academic capstone thesis."
        ),
        "location": "Navi Mumbai, India",
    },
]


def seed():
    db = SessionLocal()
    try:
        # Clear existing data first to force reload
        db.query(Project).delete()
        db.query(Skill).delete()
        db.query(Experience).delete()
        db.commit()

        # Seed new data
        db.add_all([Project(**p) for p in PROJECTS])
        db.add_all([Skill(**s) for s in SKILLS])
        db.add_all([Experience(**e) for e in EXPERIENCE])
        db.commit()
        print("[OK] Database cleared and seeded with Nakul Dalal's portfolio data")
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Failed to seed database: {e}")
    finally:
        db.close()
