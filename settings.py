
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'dummy'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','core']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF = 'urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [BASE_DIR / 'templates'],'APP_DIRS': True,'OPTIONS': {'context_processors': ['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
