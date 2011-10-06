import os
import sys
try:
    # dateutil is an absolute requirement
    import dateutil
except ImportError:
    raise ImportError(
        'django-swingtime requires the "dateutil" package '
        '(http://labix.org/python-dateutil)'
    )

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(PROJECT_DIR))

DEBUG = TEMPLATE_DEBUG = True
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = 'karate.db'
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'karate.db'
  }
}

SITE_ID = 1
TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'de'
LANGUAGES = (('en', 'English'),
             ('de', 'German'),)
USE_I18N = True
USE_L10N = True
FIRST_DAY_OF_WEEK = 1

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = 'j#_e3y&h=a4)hrmj=)bqo@$6qoz6(hrf9wz@uqq@uy*0uzl#ew'
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'swingtime.context_processors.current_datetime',
)

ROOT_URLCONF = 'demo.urls'
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'swingtime',
    'karate',
)


MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]


SWINGTIME_SETTINGS_MODULE = 'demo.swingtime_settings'

try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS += ('django_extensions',)

try:
    from local_settings import *
except ImportError:
    pass


