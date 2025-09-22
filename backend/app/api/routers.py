from fastapi import APIRouter
from app.api.endpoints import file, chat

router = APIRouter()

router.include_router(file.router, tags=["files"])
router.include_router(chat.router, tags=["chat"])