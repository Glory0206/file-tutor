from sqlalchemy.orm import Session

from app import models, schemas

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