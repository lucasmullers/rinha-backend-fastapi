from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@db:5432/rinha'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
