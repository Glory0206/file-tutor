from typing import Any, List
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app import services
from app.schemas.file import File as FileSchema
from app.api.deps import get_db


router = APIRouter()

@router.get("/files", response_model=List[FileSchema])
def read_files(
    db: Session = Depends(get_db),
    skip: int = 0, # 페이지네이션을 위한 시작점(offset)
    limit: int = 100, # 한 번에 가져올 최대 파일 개수
    current_user_id: int = 1
) -> Any:
    files = services.file_service.get_files(db=db, skip=skip, limit=limit, owner_id=current_user_id)
    return files

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