from fastapi import APIRouter
from app.api.endpoints import file

router = APIRouter()
router.include_router(file.router, tags=["files"])