import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "change_this_in_production")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# -----------------------------
#  INSTALLED APPS (Jazzmin First)
# -----------------------------
INSTALLED_APPS = [
    "jazzmin",  # Dashboard Theme
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "cms",
]

# -----------------------------
#  MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# -----------------------------
#  TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# -----------------------------
#  DATABASE (PostgreSQL)
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "alfateh_db"),
        "USER": os.getenv("DB_USER", "alfateh_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "ASDma!@#2026"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# -----------------------------
#  PASSWORD VALIDATION
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]

# -----------------------------
#  INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Damascus"
USE_I18N = True
USE_TZ = True

# -----------------------------
#  STATIC FILES
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------
#  REST FRAMEWORK
# -----------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# -----------------------------
#  JAZZMIN SETTINGS (Dashboard)
# -----------------------------
JAZZMIN_SETTINGS = {
    "site_title": "ALFATEH ISP Dashboard",
    "site_header": "ALFATEH ISP",
    "site_brand": "ALFATEH ISP",
    "welcome_sign": "مرحباً بك في لوحة التحكم",
    "copyright": "ALFATEH ISP",
    "search_model": ["cms.Service", "cms.FAQ", "cms.ContactMessage"],

    "topmenu_links": [
        {"name": "الرئيسية", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "الموقع الرسمي", "url": "https://alfatehisp.sy", "new_window": True},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "cms.HeroSection": "fas fa-bullhorn",
        "cms.AboutSection": "fas fa-info-circle",
        "cms.Service": "fas fa-network-wired",
        "cms.ServiceDetail": "fas fa-file-alt",
        "cms.FAQ": "fas fa-question-circle",
        "cms.FooterInfo": "fas fa-shoe-prints",
        "cms.SocialLink": "fas fa-share-alt",
        "cms.ContactMessage": "fas fa-envelope",
    },

    "hide_apps": [],
    "hide_models": [],
}

# -----------------------------
#  JAZZMIN UI TWEAKS (Theme)
# -----------------------------
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark bg-primary",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
}

