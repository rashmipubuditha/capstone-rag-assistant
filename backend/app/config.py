from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ERP Knowledge Assistant API"
    environment: str = "dev"
    allowed_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    openai_api_key: Optional[str] = None
    database_url:  Optional[str] = None 

    class Config:
        env_file = ".env"

settings = Settings()