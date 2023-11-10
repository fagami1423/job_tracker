# /app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    mongo_details: str  # Assuming you want to keep this for your MongoDB URI
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
