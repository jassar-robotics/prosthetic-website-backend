"""
This is the base settings.py where both production and development enviromnent seetings are placed.
"""

import os
from pathlib import Path

import cloudinary
import cloudinary.api
import cloudinary.uploader
import environ

from core.config import REFRESH_LIFETIME, TOKEN_LIFETIME

BASE_DIR = Path(__file__).resolve().parent.parent.parent


env = environ.Env(DEBUG=(bool, False))


environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = env("SECRET_KEY", default="django-insecure-key")


CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
)

INSTALLED_APPS = [
    "jazzmin",
    'colorfield',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "tinymce",
    "cloudinary",
    "django_extensions",
    "users",
    "contacts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"


# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

# Database (To be overridden per environment)
DATABASES = {}

# Authentication
AUTH_USER_MODEL = "users.Users"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

GOOGLE_PLACE_ID = env("GOOGLE_PLACE_ID")
GOOGLE_PLACE_API = env("GOOGLE_PLACE_API")
GOOGLE_SECRET_KEY = env("GOOGLE_SECRET_KEY")

DEFAULT_SUPERUSER_USERNAME = env("DEFAULT_SUPERUSER_USERNAME")
DEFAULT_SUPERUSER_PASSWORD = env("DEFAULT_SUPERUSER_PASSWORD")

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": TOKEN_LIFETIME,
    "REFRESH_TOKEN_LIFETIME": REFRESH_LIFETIME,
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
    # "TOKEN_OBTAIN_SERIALIZER": "customUser.serializers.CustomTokenObtainPairView"
}


cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_NAME"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "django_errors.log"),
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}





JAZZMIN_SETTINGS = {
    "site_title": "PROJECT_NAME",
    "site_header": "PROJECT_NAME",
    "site_brand": "PROJECT_NAME",
    "welcome_sign": "Welcome to PROJECT_NAME Admin Panel",

    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",
    
    "brand_logo_xl": "images/image.webp",
    "brand_logo": "images/image.webp",

    "site_logo": "images/image.webp",
    "site_icon": "images/image.webp",

    "collapse_apps": True,
    "related_modal_active": True,
    "order_with_respect_to": ["tours", "tours.Tour",  "treks", "treks.Trek", "dayhikes", "dayhikes.DayHike","blogs","upcomingevents", "districts", "locations", "regions","contacts", "reviews", "tourstyles"],


    "collapse_apps_initially": [
        "users", "tours", "treks", "gears", "districts", "locations", "notices",
        "reviews", "blogs", "regions", "meals", "accomodations", "transportations",
        "contacts", "dayhikes", "tourstyles", "faqs", "upcomingevents",
    ],


    "icons": {
        "auth": "fas fa-users-cog",
        "users.Users": "fas fa-user",
        "auth.Group": "fas fa-user-shield",
        "gears": "fas fa-cogs",
        "blogs.Blogs": "fas fa-blog",
        "blogs.Categories": "fas fa-folder-open",
        "treks.Trek": "fas fa-hiking",
        "reviews": "fas fa-comments",

        "accomodations.Accomodation": "fas fa-hotel",

        "contacts.Booking": "fas fa-calendar-check",
        "contacts.Contact": "fas fa-address-book",
        "contacts.CustomTrip": "fas fa-route",


        "teams.Team": "fas fa-user-friends",

        # DayHike
        "dayhikes.DayHike": "fas fa-hiking",            
        "dayhikes.DayHikeGallery": "fas fa-images", 
        "dayhikes.Excludes": "fas fa-ban",                
        "dayhikes.Includes": "fas fa-check-circle",
        "dayhikes.Extras": "fas fa-plus-circle",       
        "dayhikes.FAQ": "fas fa-question-circle",         
        "dayhikes.Pricing": "fas fa-dollar-sign",           
        "dayhikes.Schedule": "fas fa-calendar-alt",         
        "dayhikes.Tips": "fas fa-lightbulb",  
        "dayhikes.DayhikeReview": "fas fa-star-half-alt",
        
        
        "tours.Tour": "fas fa-route",
        "tours.Includes": "fas fa-check-circle",
        "tours.Excludes": "fas fa-ban",
        "tours.Highlights": "fas fa-star",
        "tours.FunFacts": "fas fa-smile-beam",
        "tours.FAQ": "fas fa-question-circle",
        "tours.Pricing": "fas fa-dollar-sign",
        "tours.Schedule": "fas fa-calendar-alt",
        "tours.Gallery": "fas fa-images",
        "tours.ScheduleGallery": "fas fa-camera", 
        "tours.TourReview": "fas fa-star-half-alt", 


        
        "treks.Trek": "fas fa-hiking",
        "treks.Includes": "fas fa-check-circle",
        "treks.Excludes": "fas fa-ban",
        "treks.FAQ": "fas fa-question-circle",
        "treks.Pricing": "fas fa-dollar-sign",
        "treks.Schedule": "fas fa-calendar-alt",
        "treks.Gallery": "fas fa-images",
        "treks.ScheduleGallery": "fas fa-camera",  
        "treks.TrekReview": "fas fa-star-half-alt",


        
        "tourstyles.PatternColour": "fas fa-palette",
        "tourstyles.Pattern": "fas fa-image",
        "tourstyles.BentoTypeOne": "fas fa-th-large",
        "tourstyles.BentoTypeTwo": "fas fa-fill-drip",


        
        "districts.District": "fas fa-map-marker-alt", 
        "faqs.FAQ": "fas fa-question-circle",  
        
        "socialinitiatives.SocialInitiative": "fas fa-heart",   
        "socialinitiatives.SocialInitiativeGallery": "fas fa-images",           
        
        "gears.Gear": "fas fa-cogs",

        "locations.Location": "fas fa-map-marker-alt",
        "meals.Meal": "fas fa-utensils",

        "notices.Notices": "fas fa-tags",
        
        "regions.Region": "fas fa-map",


        "reviews.ExchangeRate": "fas fa-money-bill-wave",
        "reviews.Review": "fas fa-star-half-alt",
        "reviews.GoogleReview": "fab fa-google",

        "transportations.Transportation": "fas fa-bus-alt",

        "upcomingevents.UpcomingEvent": "fas fa-calendar-alt",       
    },


    "theme": {
        "sidebar": {
            "background": "#0000ff",
            "text": "#ecf0f1",
            "brand_background": "#1abc9c",
            "brand_text": "#ffffff",
            "nav_item_hover_background": "#16a085",
            "nav_item_hover_text": "#ffffff",
            "nav_item_active_background": "#2980b9",
            "nav_item_active_text": "#ffffff",
        },
    },
}
