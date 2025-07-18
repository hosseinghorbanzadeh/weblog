from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-3wg$63cv$1v%+#(arheq&*7$6boa&7na$ua=jo51fed=c8dyz3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['hosseinghorbanzadeh.com']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT=BASE_DIR / 'static'
MEDIA_ROOT=BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


CSRF_COOKIE_SECURE=True