from sqlalchemy.orm import Session
from typing import Optional, List

from app import models, schemas

def get(db: Session, id: int) -> Optional[models.File]:
    return db.query(models.File).filter(models.File.id == id).first()

def get_multi(db: Session, skip: int = 0, limit: int = 100, owner_id: int = None) -> List[models.File]:
    query = db.query(models.File)

    if owner_id is not None:
        query = query.filter(models.File.owner_id == owner_id)

    return query.offset(skip).limit(limit).all()

def create_user_file(*, db: Session, file_in: schemas.FileCreate, owner_id: int) -> models.File:
    # 파일 등록
    db_obj = models.File(
        filename=file_in.filename,
        url=file_in.url,
        file_path=file_in.file_path,
        owner_id=owner_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj