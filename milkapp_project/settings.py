import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JS, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'dairyapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collectstatic

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dairyapp',
]

# Debug should be False in production
DEBUG = False

# Render domain + local for testing
ALLOWED_HOSTS = ['dairy-app-56d5.onrender.com', '127.0.0.1', 'localhost']

# Middleware stack
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Serves static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# TEMPLATES section (required for Django)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Required for resolving URLs
ROOT_URLCONF = 'milkapp_project.urls'

# Static file storage with hashed names (recommended)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WSGI
WSGI_APPLICATION = 'milkapp_project.wsgi.application'

# Database (default SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Timezone and language
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
