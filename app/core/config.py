from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

def _build_db_url(
    user: str,
    password: str,
    host: str,
    port: int,
    database: str,
) -> str:
    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Read from project-root .env
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = "/api/v1"

    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    # Database
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_NAME: str = "app"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"

    @property
    def DATABASE_URL(self) -> str:
        return _build_db_url(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )
