from fastapi import APIRouter
from sqlalchemy import text

from app.database.engine import engine

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "service": "DevFlow AI",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": str(e),
        }