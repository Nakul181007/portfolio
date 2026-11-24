import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .database import Base, engine
from .routers import projects, skills, experience, contact
from .seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables and seed portfolio content on startup.
    Base.metadata.create_all(bind=engine)
    seed()
    yield


app = FastAPI(
    title="Portfolio API",
    description="Personal portfolio backend — projects, skills, experience, contact",
    version="1.0.0",
    lifespan=lifespan,
)

# Set CORS_ORIGINS to a comma-separated list of deployed frontend origins.
allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(experience.router)
app.include_router(contact.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "message": "Portfolio API is running"}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )
