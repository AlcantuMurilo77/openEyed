from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "openEyed"
    database_url: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()

