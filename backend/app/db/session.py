from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app.core.config import settings

# 데이터베이스 엔진 생성
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# 데이터베이스 세션 생성을 위한 sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)