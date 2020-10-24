# Settings for development in the source tree

from . import defaults
import os
from os.path import join, dirname

PRAKTOMAT_PATH = '/server/Praktomat'

# The name that will be displayed on top of the page and in emails.
SITE_NAME = 'Praktomat Development Edition'

# Identifie this Praktomat among multiple installation on one webserver
PRAKTOMAT_ID = 'dev'

# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# developmentserver.
BASE_HOST = 'http://localhost:8000'
BASE_PATH = '/'

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = join(dirname(dirname(dirname(__file__))), 'data')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(PRAKTOMAT_PATH, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

JPLAGJAR = join(dirname(dirname(dirname(__file__))), 'jplag.jar')

#PRIVATE_KEY = join(dirname(dirname(dirname(__file__))), 'examples', 'certificates', 'privkey.pem')
#CERTIFICATE = join(dirname(dirname(dirname(__file__))), 'examples', 'certificates', 'signer.pem')

PRIVATE_KEY = 0
CERTIFICATE = 0

# Finally load defaults for missing setttings.
defaults.load_defaults(globals())

# To get exceptions logged as well:
MIDDLEWARE += [
    'utilities.exceptionlogger.ExceptionLoggingMiddleware',
]
