from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.routers import cabs, electronics

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Mock backend for electronics and cab fare comparison.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(electronics.router, prefix=settings.api_prefix)
app.include_router(cabs.router, prefix=settings.api_prefix)


@app.get("/")
async def root() -> dict[str, str]:
    """Simple root endpoint to confirm the API is running."""

    return {
        "message": "Welcome to oneCompare API",
        "docs": "/docs",
        "status": "running",
    }
