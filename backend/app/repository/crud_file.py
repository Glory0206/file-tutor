from sqlalchemy.orm import Session
from typing import Optional

from app import models, schemas

def get(db: Session, id: int) -> Optional[models.File]:
    return db.query(models.File).filter(models.File.id == id).first()

def create_user_file(*, db: Session, file_in: schemas.FileCreate, owner_id: int) -> models.File:
    # 파일 등록
    db_obj = models.File(
        filename=file_in.filename,
        file_path=file_in.file_path,
        owner_id=owner_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj