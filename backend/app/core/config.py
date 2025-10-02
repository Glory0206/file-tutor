from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL 연결 정보
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"

    # Google API 키
    GOOGLE_API_KEY: str

    # JWT
    JWT_SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUITES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 60 * 24 * 7

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return(
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'

settings = Settings()