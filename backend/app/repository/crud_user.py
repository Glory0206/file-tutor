from sqlalchemy.orm import Session
from app import models, schemas

def get_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, *, email: str, password: str) -> models.User | None:
    user = get_by_email(db, email=email)
    if not user:
        return None
    if user.password != password:
        return None
    return user