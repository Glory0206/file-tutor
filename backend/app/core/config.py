from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL 연결 정보
    # --- 데이터베이스 설정 ---
    # .env 파일에서 PostgreSQL 연결 정보를 읽어옵니다.
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"

    # Google API 키
    # --- 외부 API 키 ---
    GOOGLE_API_KEY: str
    

    # SQLAlchemy가 생성하는 데이터베이스 URL을 동적으로 생성하는 속성입니다.
    # 이 속성은 다른 POSTGRES_* 변수들을 조합하여 완전한 DB 연결 문자열을 만듭니다.
    @property
    def DATABASE_URL(self) -> str:
        return(
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    # SQLAlchemy 데이터베이스 URI
    SQLALCHEMY_DATABASE_URI: str | None = None

    class Config:
        # .env 파일의 상대 경로를 지정합니다. (현재 파일 위치 기준)
        env_file = "../.env"
        env_file_encoding = 'utf-8'

settings = Settings()