from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL 연결 정보
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    
    @property
    def DATABASE_URL(self) -> str:
        return(
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    # SQLAlchemy 데이터베이스 URI
    SQLALCHEMY_DATABASE_URI: str | None = None

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'

settings = Settings()