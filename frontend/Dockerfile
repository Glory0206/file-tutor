# 베이스 이미지 선택
FROM node:22 AS alpine

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY package*.json ./
RUN npm install

# 소스 코드 전체 복사
COPY . .

# 5173번 포트를 외부에 노출
EXPOSE 5173

# 애플리케이션 실행
CMD ["npm", "run", "dev", "--", "--host"]
