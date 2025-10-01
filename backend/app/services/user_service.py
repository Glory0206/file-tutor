from sqlalchemy.orm import Session
from fastapi import HTTPException

from app import schemas, repository


def signup(db: Session, user: schemas.UserCreate):
    db_user = repository.crud_user.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    return repository.crud_user.create(db=db, user=user)


def authenticate(db: Session, email: str, password: str):
    db_user = repository.crud_user.authenticate(db, email=email, password=password)
    if not db_user:
        raise HTTPException(status_code=400, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    return db_user