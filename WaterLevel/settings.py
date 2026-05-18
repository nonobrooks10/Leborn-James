"""
Django settings for WaterLevel project.
"""
import os
from pathlib import Path

# 基础路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 安全配置（简化，开发环境）
SECRET_KEY = 'django-insecure-hj^0@s8h@m3r+ccui-#+&-!wm@12597f=$6y$^6o%01n4w!_r8'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # 补充常用本地域名

# 应用注册（仅保留核心）
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'app01.apps.App01Config'
]

# 中间件（移除非核心，保留认证/会话）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'app01.middleware.auth.AuthMiddleWare'  # 自定义认证中间件保留
]

ROOT_URLCONF = 'WaterLevel.urls'

# 模板配置（简化）
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'WaterLevel.wsgi.application'

# 数据库（保留MySQL配置，注释SQLite）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'syj',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

# 密码验证（简化，开发环境可注释）
AUTH_PASSWORD_VALIDATORS = []

# 国际化（简化）
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'  # 修正为本地时区（UTC改为上海）
USE_I18N = False
USE_TZ = False

# 静态文件/上传路径
STATIC_URL = '/static/'
IMG_UPLOAD = os.path.join(BASE_DIR, 'app01/static/temp_img')

# 默认主键
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'