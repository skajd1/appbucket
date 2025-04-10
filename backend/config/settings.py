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

ENVIRONMENT = env('ENV')
env_path = os.path.join(BASE_DIR, ".env")

# .env 로드
if os.path.exists(env_path):
    environ.Env.read_env(env_path)

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': env.db()
}

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'bucket',
    'rest_framework',

]
# settings.py
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTH_USER_MODEL = 'users.User'  # 앱 이름에 맞게 수정

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
