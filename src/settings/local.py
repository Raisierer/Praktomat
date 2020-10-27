# Settings for deployment

# These settings are specific for the University of Stuttgart and derive some parts of the settings
# from the directory name.
#
# If you are not deploying on praktomat.ils.uni-stuttgart.de you need to rewrite this file.

from . import defaults
import os
from os.path import join, dirname, basename
import re

PRAKTOMAT_PATH = dirname(dirname(dirname(__file__)))

PRAKTOMAT_ID = os.environ.get('ID', 'Praktomat')

DEBUG = int(os.environ.get('DEBUG', 0))

MIRROR = False


# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# development server.
BASE_HOST = os.environ.get('BASE_HOST', 'http://0.0.0.0:8000/')
BASE_PATH = '/'

SITE_NAME = os.environ.get('SITE_NAME', 'Praktomat')

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'
STATIC_ROOT = join(PRAKTOMAT_PATH, "static")

TEST_MAXLOGSIZE = 512

TEST_MAXFILESIZE = 512

TEST_TIMEOUT = 180

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.

# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = join(dirname(PRAKTOMAT_PATH), "PraktomatSupport/")

if MIRROR:
    SANDBOX_DIR = join('/srv/praktomat/sandbox_Mirror/', PRAKTOMAT_ID)
else:
    SANDBOX_DIR = join('/srv/praktomat/sandbox/', PRAKTOMAT_ID)

ADMINS = [
    ('Praktomat', 'praktomat@ils.uni-stuttgart.de')
]

# EMail settings

#SERVER_EMAIL = 'praktomat@ils.uni-stuttgart.de'

#EMAIL_BACKEND = 'django.core.mail.backend.smtp.EmailBackend'

#EMAIL_HOST_USER = os.environ['EMAIL_USERNAME']
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']

# Database settings

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


# Private key used to sign uploded solution files in submission confirmation email
# PRIVATE_KEY = '/srv/praktomat/mailsign/signer_key.pem'
PRIVATE_KEY = '/etc/ssl/private/praktomat.key'
CERTIFICATE = '/srv/praktomat/mailsign/signer.pem'

# Enable Shibboleth:
SHIB_ENABLED = False
REGISTRATION_POSSIBLE = True

# SYSADMIN_MOTD_URL = "https://praktomat.cs.kit.edu/sysadmin_motd.html"

# Use a dedicated user to test submissions
USEPRAKTOMATTESTER = True

# Use docker to test submission
USESAFEDOCKER = False

# Various extra files and versions
#CHECKSTYLEALLJAR = '/srv/praktomat/contrib/checkstyle-5.7-all.jar'
#JPLAGJAR = '/srv/praktomat/contrib/jplag.jar'
#JAVA_BINARY = 'javac-sun-1.7'
#JVM = 'java-sun-1.7'

# Our VM has 4 cores, so lets try to use them
NUMBER_OF_TASKS_TO_BE_CHECKED_IN_PARALLEL = 4

# Finally load defaults for missing settings.
defaults.load_defaults(globals())
