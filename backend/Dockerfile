# 베이스 이미지 선택
FROM python:3.11-slim

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
# (pip 캐시를 활용하기 위해 requirements.txt를 먼저 복사하는 것이 좋습니다)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 전체 복사
COPY . .

# 8000번 포트를 외부에 노출
EXPOSE 8000

# uvicorn 서버 실행 (수정된 부분)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]