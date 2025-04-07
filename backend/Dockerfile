## Python 베이스 이미지 사용
#FROM python:3.10-slim
#
## 환경변수 설정
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## 작업 디렉토리 생성
#WORKDIR /app
#
## 시스템 패키지 업데이트 및 의존 패키지 설치
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    libpq-dev \
#    netcat \
#    && rm -rf /var/lib/apt/lists/*
#
## requirements 복사 및 설치
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## 프로젝트 전체 복사
#COPY . .
#
## 포트 노출
#EXPOSE 8000
#
## 엔트리포인트 스크립트 복사
#COPY ./entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#
## 실행
#ENTRYPOINT ["/entrypoint.sh"]
