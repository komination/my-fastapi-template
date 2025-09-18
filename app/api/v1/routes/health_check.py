from fastapi import APIRouter

health_check_router = APIRouter()


@health_check_router.get("/")
def health() -> dict:
    return {"status": "ok"}
