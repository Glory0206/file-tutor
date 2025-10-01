from fastapi import APIRouter
from app.api.endpoints import file, chat, user

router = APIRouter()

router.include_router(file.router, tags=["files"])
router.include_router(chat.router, tags=["chat"])
router.include_router(user.router, tags=["users"])