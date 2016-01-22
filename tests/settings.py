import os

DEBUG = False

ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'en-us'
ROOT_URLCONF = 'urls'
SECRET_KEY = '12345abcd'
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
SITE_ID = 1
TIME_ZONE = 'UTC'
USE_I18N = True

UMANAGE_BASE_TEMPLATE = 'base_umanage.html'
UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE = 'base_umanage_unauthenticated.html'
UMANAGE_FROM_EMAIL = 'noreply@example.com'
UMANAGE_SITE_ROOT_URI = 'http://somedomain.com'
UMANAGE_SITE_NAME = 'My Site Name'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django_core',
    'umanage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.template.context_processors.request',
    'django.template.context_processors.media',
    'django.contrib.auth.context_processors.auth',
    'umanage.context_processors.common',
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'tests/templates'),
    os.path.join(SITE_ROOT, 'umanage/templates'),
)

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': here('test_db.db')
    }
}
