from sqlalchemy.orm import Session
from app import models


def get(db: Session, id: int) -> models.User | None:
    # id로 사용자 조회
    return db.query(models.User).filter(models.User.id == id).first()
