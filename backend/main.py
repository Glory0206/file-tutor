from fastapi import FastAPI
from app.api.routers import router
from app.db.session import engine
from app.db.base_class import Base
# from app.models.file import File
# from app.models.user import User

# 데이터베이스 테이블을 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
async def read_index():
    return {"message": "안녕하세요."}
