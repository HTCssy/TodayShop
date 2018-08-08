import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加文件夹
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
#xadmin
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=^)1s*z%!8uzj0ams!axniuerjh8u66tbqd+a*l*lf04#xar1n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# MY_APPS = ['apps.arts_app',
#            'apps.comments',
#            'apps.message',
#            'apps.statistic',
#            ]
# EXT_APPS = [#必须要导入的这两个xadmin模块
#             'extra_apps.xadmin',
#             'crispy_forms',
#             #扩展包
#             'reversion',
# ]
# SYS_APPS = ['django.contrib.admin',
#             'django.contrib.auth',
#             'django.contrib.contenttypes',
#             'django.contrib.sessions',
#             'django.contrib.messages',
#             'django.contrib.staticfiles',
# ]
#
# INSTALLED_APPS = SYS_APPS + EXT_APPS + MY_APPS


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TodayShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TodayShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'today_shop',
        'PASSWORD': '123456',
        'HOST': '192.168.227.131',
        'PORT': '3306',
        'CHARSET': 'utf8',
        'USER': 'lijian',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 后期项目部署统一到一个文件中去
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, ''),
)

#文件上传 上传目录的根目录
MEDIA_ROOT = os.path.join(BASE_DIR + '/media/')
#上传文件访问的路径
MEDIA_URL = '/media/'

# 'http://127.0.0.1:8000/static/
TEMP_STATIC_URL = 'http://127.0.0.1:8000' + STATIC_URL
TEMP_MEDIA_URL = 'http://127.0.0.1:8000' + MEDIA_URL
