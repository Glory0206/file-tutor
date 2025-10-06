from fastapi import APIRouter
from app.api.endpoints import file_router
from app.api.endpoints import auth_router, chat_router

router = APIRouter()

router.include_router(file_router.router, tags=["files"])
router.include_router(chat_router.router, tags=["chat"])
router.include_router(auth_router.router, tags=["users"])