from fastapi import APIRouter

from .routes import health_check_router

router = APIRouter()

router.include_router(health_check_router, prefix="/health", tags=["Health Check"])
