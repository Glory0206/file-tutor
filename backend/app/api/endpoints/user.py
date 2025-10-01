from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, services
from app.api import deps

router = APIRouter()


@router.post("/signup", response_model=schemas.User)
def handle_signup(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    return services.user_service.signup(db=db, user=user)


@router.post("/login")
def handle_login(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    services.user_service.authenticate(db=db, email=user.email, password=user.password)
    return {"message": "Login successful"}
