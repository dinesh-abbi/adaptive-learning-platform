from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=True,
    )

    APP_NAME: str = "Adaptive Learning Platform"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str

    OPENAI_API_KEY: str = ""

    SECRET_KEY: str = Field(...)

    REDIS_URL: str = "redis://redis:6379/0"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
