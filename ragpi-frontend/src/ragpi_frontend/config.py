from functools import lru_cache
from typing import Any, Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application Configuration
    RAGPI_API_URL: str = "localhost:8000/chat"
    CHAT_MODEL: str = "gemini-2.0-flash"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_settings():
    return Settings()
