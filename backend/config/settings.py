import os
import environ
from pathlib import Path

ROOT_URLCONF = 'config.urls'
BASE_DIR = Path(__file__).resolve().parent.parent

# 환경 변수 설정 객체 생성
env = environ.Env(
    ENV=(str, 'local'),
    DEBUG=(bool, True)
)

# ENV 값에 따라 .env 파일 경로 분기
ENVIRONMENT = os.getenv("ENV", "local")
env_path = os.path.join(BASE_DIR,".env.production") if ENVIRONMENT == "production" else os.path.join(BASE_DIR,".env")

# .env 또는 .env.production 로드
if os.path.exists(env_path):
    environ.Env.read_env(env_path)

# 이후 설정은 동일
ENV = env('ENV')
DEBUG = env('DEBUG')
# SECRET_KEY = env('SECRET_KEY')
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': env.db()
}

INSTALLED_APPS = [
    'users'
]
