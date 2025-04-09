# Python slim 이미지 기반 (최소한의 크기)
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 시스템 패키지 설치 (간단한 필수만)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치 준비
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 전체 소스 복사
COPY . .

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Django static 파일 수집 및 DB 마이그레이션
RUN python manage.py migrate

# Uvicorn 실행
CMD ["uvicorn", "backend.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
