import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

# Where Django looks for your app static files (CSS/images/etc.)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'dairyapp', 'static')]

# Where Django collects all static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # ✅ THIS LINE
    'dairyapp',
]
