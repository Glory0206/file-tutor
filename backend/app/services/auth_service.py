from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from jose import JWTError, jwt
from redis.asyncio import Redis
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUITES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt

async def store_refresh_token(redis: Redis, email: str, refresh_token: str):
    expire_seconds = int(timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS).total_seconds())
    await redis.set(f"refresh_token:{email}", refresh_token, ex=expire_seconds)

async def get_stored_refresh_token(redis: Redis, email: str) -> str | None:
    return await redis.get(f"refresh_token:{email}")

async def refresh_access_token(redis: Redis, refresh_token: str) -> dict[str, str]:
    try:
        payload = jwt.decode(refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str | None = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="refresh token이 유효하지 않습니다.")

        get_refresh_token = await get_stored_refresh_token(redis, email)
        print("get_refresh_token: ", get_refresh_token)
        print("refresh_token: ", refresh_token)
        if get_refresh_token is None or get_refresh_token != refresh_token:
            raise HTTPException(status_code=401, detail="refresh token이 유효하지 않거나 만료되었습니다.")

        new_access_token = create_access_token(data={"sub": email})
        new_refresh_token = create_refresh_token(data={"sub": email})
        
        await store_refresh_token(redis, email, new_refresh_token)
        
        return new_access_token, new_refresh_token

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
