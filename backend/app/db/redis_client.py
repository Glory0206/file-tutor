import redis.asyncio as redis
from app.core.config import settings

# Redis 연결 풀 생성
redis_pool = redis.ConnectionPool.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0", # DB 0번 사용
    decode_responses=True # 응답을 자동으로 유니코드로 디코딩
)

# FastAPI Dependency로 사용할 수 있도록 함수 정의
async def get_redis():
    """
    Redis 연결을 제공하는 Dependency
    """
    async with redis.Redis.from_pool(redis_pool) as client:
        yield client