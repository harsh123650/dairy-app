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

# Set to False in production
DEBUG = False

# Render production domain
ALLOWED_HOSTS = ['dairy-app-56d5.onrender.com', '127.0.0.1', 'localhost']

# Recommended for static files on Render
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Use WhiteNoise storage backend (optional but good)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
