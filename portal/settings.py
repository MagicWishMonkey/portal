"""
Django settings for this project
"""
import os
from rpg.util.configurator import Configurator


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
WORKSPACE = os.path.abspath(os.path.join(PROJECT_PATH, "../"))
CONFIG = Configurator(PROJECT_PATH)

DEBUG = CONFIG.debug # SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = CONFIG.debug
ALLOWED_HOSTS = CONFIG.get("ALLOWED_HOSTS", ["*"])
ADMINS = CONFIG.get("ADMINS", [])
EXTERNAL_REQUEST_TIMEOUT = float(CONFIG.get('EXTERNAL_REQUEST_TIMEOUT'))
SECRET_KEY = CONFIG.secret_key

URI = CONFIG.get("URI")
if URI.endswith("/"):
    URI = URI[0:len(URI) - 1]

NEWRELIC = CONFIG.get("NEWRELIC", None)
if NEWRELIC:
    NEWRELIC = os.path.abspath(os.path.join(PROJECT_PATH, NEWRELIC))

if CONFIG.get("LOGGING", None):
    if CONFIG.get("LOGGING").get("enabled", False):
        LOGGING = CONFIG.get("LOGGING")
        LOGGING.pop("enabled")


# Application definition
ROOT_URLCONF = 'portal.urls'
WSGI_APPLICATION = 'portal.wsgi.application'

DATABASES = CONFIG.get("DATABASES")

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ENABLE CROSS SITE STUFF
CORS_ORIGIN_ALLOW_ALL = True

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# # POINT TO THE FIXTURES SUBDIRECTORY
# FIXTURE_DIRS = (
#     os.path.abspath(os.path.join(PROJECT_PATH, "../rpg/migrations/fixtures")),
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rpg'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "portal.middleware.attach_values",
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'portal.middleware.ErrorHandler'
)

