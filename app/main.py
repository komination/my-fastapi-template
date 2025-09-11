from fastapi import FastAPI

from app.api.v1.routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="App")
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
