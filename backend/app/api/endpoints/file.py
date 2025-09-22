from typing import Any
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from app import services
from app.schemas.file import File as FileSchema
from app.db.session import get_db


router = APIRouter()

@router.post("/upload", response_model=FileSchema)
async def upload_file(
    *,
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
    current_user_id: int = 1
) -> Any:
    saved_file = await services.file_service.save_upload_file(
        db=db, file=file, user_id=current_user_id
    )
    return saved_file