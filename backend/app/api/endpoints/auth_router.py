from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from redis.asyncio import Redis

from app.crud import crud_user
from app.db.redis_client import get_redis
from app.schemas.auth_schema import UserCreate, Token
from app.services import auth_service
from app.api import deps

router = APIRouter(prefix="/auth")

@router.post("/signup")
async def signup( user_create: UserCreate, db: Session = Depends(deps.get_db)):
    db_user = crud_user.get_user_by_email(db, email=user_create.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    crud_user.create_user(db=db, user=user_create)
    return {"message": "회원가입이 완료되었습니다."}

@router.post("/login", response_model=Token)
async def login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    redis: Annotated[Redis, Depends(get_redis)],
    db: Session = Depends(deps.get_db),
):
    user = crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not auth_service.verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="email 또는 password가 일치하지 않습니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    token_data = {"sub": user.email}
    access_token = auth_service.create_access_token(token_data)
    refresh_token = auth_service.create_refresh_token(token_data)

    # Redis 함수 호출
    await auth_service.store_refresh_token(redis, user.email, refresh_token)

    # HttpOnly 쿠키
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        # secure=True, # 배포 시에는 True로 설정하여 https에서만 전송되도록
        # samesite="strict", # CSRF 방어
        max_age=60*60*24*7
    )

    return {"access_token": access_token}

@router.post("/refresh", response_model=Token)
async def refresh(
    response: Response,
    refresh_token: Annotated[str | None, Cookie()] = None,
    redis: Annotated[Redis, Depends(get_redis)] = None,
):
    if refresh_token is None:
         raise HTTPException(status_code=401, detail="refresh token이 없습니다.")
    
    new_access_token, new_refresh_token = await auth_service.refresh_access_token(redis, refresh_token)

    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        max_age=60*60*24*7
    )
    
    return {"access_token": new_access_token}