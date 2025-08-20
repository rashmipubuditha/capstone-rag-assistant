from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    database_url: str
    env: str = "dev"


class Config:
    env_file = ".env"


settings = Settings()