from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Generator

from app.repository import crud_user
from app.db.session import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), id: int = 1):
    user = crud_user.get(db, id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user