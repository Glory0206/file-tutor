import os
import uuid
import aiofiles
from sqlalchemy.orm import Session

from fastapi import UploadFile
from app import models, schemas, repository

UPLOAD_DIRECTORY = "./uploads"
BASE_URL = "http://localhost:8000/uploads"

def get_files(db: Session, skip: int = 0, limit: int = 100, owner_id: int = None):
    return repository.crud_file.get_multi(db=db, skip=skip, limit=limit, owner_id=owner_id)


async def save_upload_file(*, db: Session, file: UploadFile, user_id: int) -> models.File:
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    original_filename = file.filename
    file_extension = os.path.splitext(original_filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)

    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while content := await file.read(1024):
                await out_file.write(content)

    finally:
        await file.close()

    # URL 생성
    file_url = f"{BASE_URL}/{unique_filename}"

    file_in = schemas.FileCreate(filename=original_filename, url=file_url)

    return repository.crud_file.create_user_file(db=db, file_in=file_in, owner_id=user_id)