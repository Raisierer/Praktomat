# Settings for deployment

# These settings are specific for the University of Stuttgart and derive some parts of the settings
# from the directory name.
#
# If you are not deploying on praktomat.ils.uni-stuttgart.de you need to rewrite this file.

from os.path import join, dirname, basename
import re

PRAKTOMAT_PATH = dirname(dirname(dirname(__file__)))

PRAKTOMAT_ID = basename(dirname(PRAKTOMAT_PATH))

DEBUG = False

MIRROR = False


# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# development server.
BASE_HOST = 'https://praktomat.ils.uni-stuttgart.de'
BASE_PATH = '/' + PRAKTOMAT_ID + '/'

SITE_NAME = 'ILS Praktomat'
site_name = 'ILS Praktomat'

ALLOWED_HOSTS = ['localhost', 'praktomat.ils.uni-stuttgart.de']

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'

STATIC_ROOT = join(dirname(PRAKTOMAT_PATH), "static")

TEST_MAXLOGSIZE=512

TEST_MAXFILESIZE=512

TEST_TIMEOUT=180

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

SERVER_EMAIL = 'praktomat@ils.uni-stuttgart.de'

EMAIL_BACKEND = 'django.core.mail.backend.smtp.EmailBackend'

# import email settings from file located in Praktomat parent folder
from .configuration import load_configuration
load_configuration()


# Private key used to sign uploded solution files in submission confirmation email
# PRIVATE_KEY = '/srv/praktomat/mailsign/signer_key.pem'
PRIVATE_KEY = '/etc/ssl/private/praktomat.key'
#CERTIFICATE = '/srv/praktomat/mailsign/signer.pem'

# Enable Shibboleth:
SHIB_ENABLED = False
REGISTRATION_POSSIBLE = True

# SYSADMIN_MOTD_URL = "https://praktomat.cs.kit.edu/sysadmin_motd.html"

# Use a dedicated user to test submissions
USEPRAKTOMATTESTER = True

# Use docker to test submission
USESAFEDOCKER = False

# Various extra files and versions
CHECKSTYLEALLJAR = '/srv/praktomat/contrib/checkstyle-5.7-all.jar'
JPLAGJAR = '/srv/praktomat/contrib/jplag.jar'
#JAVA_BINARY = 'javac-sun-1.7'
#JVM = 'java-sun-1.7'

# Our VM has 4 cores, so lets try to use them
NUMBER_OF_TASKS_TO_BE_CHECKED_IN_PARALLEL = 6

# Finally load defaults for missing settings.
from . import defaults
defaults.load_defaults(globals())
