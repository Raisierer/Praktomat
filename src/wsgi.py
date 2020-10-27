#!/usr/bin/env python3
import resource
from django.core.cache import CacheKeyWarning
import warnings
from django.core.wsgi import get_wsgi_application
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

warnings.simplefilter("ignore", CacheKeyWarning)


def set_to_hard(res):
    (s, h) = resource.getrlimit(res)
    resource.setrlimit(res, (h, h))


set_to_hard(resource.RLIMIT_AS)
set_to_hard(resource.RLIMIT_NPROC)

application = get_wsgi_application()
