"""
Django settings for XHVIT project.
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure--9g#3!jqpcf(&fl)wo_j53k)plmh^l%c6$#qw3*nxdo763jc+1')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS - Add Fly.io support
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
ALLOWED_HOSTS.extend(['.onrender.com', 'xhvit.onrender.com', '.fly.dev', 'localhost', '127.0.0.1', '0.0.0.0'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'corsheaders',
    'rest_framework',
    'whitenoise',
    'django_filters',
    
    # Your apps
    'Diagnosis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'XHVIT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'XHVIT.wsgi.application'

# Database
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Model Paths
XHVIT_MODEL_PATH = BASE_DIR / 'models'

XHVIT_MODEL_CONFIG = {
    'brain_tumor': {
        'name': 'Brain Tumor Classifier',
        'description': 'Classifies brain MRI into 4 types: Glioma, Meningioma, Pituitary, No Tumor',
        'num_classes': 4,
        'class_names': ['glioma', 'meningioma', 'pituitary', 'notumor'],
        'model_file': 'brain_tumor_best.pth',
        'img_size': 224,
        'icon': 'brain',
        'color': '#e74c3c'
    },
    'fracture': {
        'name': 'Fracture Classifier (FracAtlas)',
        'description': 'Detects bone fractures in X-ray images (FracAtlas dataset)',
        'num_classes': 2,
        'class_names': ['normal', 'fracture'],
        'model_file': 'fracture_best.pth',
        'img_size': 224,
        'icon': 'bone',
        'color': '#f39c12'
    },
    'fracture_multi': {
        'name': 'Fracture Classifier (Multi-Region)',
        'description': 'Detects fractures across multiple body regions in X-rays',
        'num_classes': 2,
        'class_names': ['normal', 'fracture'],
        'model_file': 'fracture_multi_best.pth',
        'img_size': 224,
        'icon': 'bone',
        'color': '#f1c40f'
    },
    'tb_chest': {
        'name': 'TB Chest X-ray Detector',
        'description': 'Detects Tuberculosis from chest X-ray images',
        'num_classes': 2,
        'class_names': ['normal', 'tuberculosis'],
        'model_file': 'tb_chest_best.pth',
        'img_size': 224,
        'icon': 'lungs',
        'color': '#3498db'
    },
    'diabetic_retinopathy': {
        'name': 'Diabetic Retinopathy Classifier',
        'description': 'Classifies diabetic retinopathy severity (0-4) from retina images',
        'num_classes': 5,
        'class_names': ['No_DR', 'Mild', 'Moderate', 'Severe', 'Proliferate_DR'],
        'model_file': 'diabetic_retinopathy_best.pth',
        'img_size': 224,
        'icon': 'eye',
        'color': '#2ecc71'
    },
    'skin_cancer': {
        'name': 'Skin Cancer Classifier',
        'description': 'Classifies skin lesions into 7 categories (HAM10000)',
        'num_classes': 7,
        'class_names': ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc'],
        'model_file': 'skin_cancer_best.pth',
        'img_size': 224,
        'icon': 'skin',
        'color': '#9b59b6'
    },
    'pneumonia': {
        'name': 'Pneumonia Detector',
        'description': 'Detects pneumonia from chest X-ray images',
        'num_classes': 2,
        'class_names': ['normal', 'pneumonia'],
        'model_file': 'pneumonia_best.pth',
        'img_size': 224,
        'icon': 'lungs',
        'color': '#e74c3c'
    }
}

# Authentication
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://xhvit.onrender.com',
    'https://*.fly.dev',  # Added for Fly.io
    'http://*.onrender.com',
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    'https://*.onrender.com',
    'https://xhvit.onrender.com',
    'https://*.fly.dev',  # Added for Fly.io
    'http://localhost:8000',
]
CORS_ALLOW_CREDENTIALS = True

# Groq API Key
GROQ_API_KEY = config('GROQ_API_KEY', default='')

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# Security Settings for Production
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Logging
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    }
