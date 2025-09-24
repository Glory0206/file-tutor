from fastapi import FastAPI, staticfiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import router
from app.db.session import engine
from app.db.base_class import Base

# 데이터베이스 테이블을 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],   
    allow_headers=["*"], 
)

app.mount("/uploads", staticfiles.StaticFiles(directory="uploads"), name="uploads")


app.include_router(router, prefix="/api")

@app.get("/")
async def read_index():
    return {"message": "안녕하세요."}
