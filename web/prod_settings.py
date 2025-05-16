"""
Django and project specific settings for usage in production.
Edit this file and adjust the options to your own requirements! You may also set additional options from
https://docs.djangoproject.com/en/1.8/ref/settings/.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base_settings import *


# Content Security Policy header in the format `directive: [values]`, see e.g
# http://www.html5rocks.com/en/tutorials/security/content-security-policy/ for an explanation
# The initially selected directives should cover most sensitive cases, but still allow YouTube embeds,
# webfonts etc.
CSP_POLICIES = {
    'base-uri': ["'self'"],
    'connect-src': ["'self'"],
    'form-action': ["'self'"],
    'object-src': ["'none'"],
    'script-src': ["'self'"],
    'style-src': ["'self'"]
}

# Set to True if your site is available exclusively through HTTPS and not via plaintext HTTP
HTTPS = False


# Your database settings
# See https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'ctf_db',
        'USER': 'hades',
        'PASSWORD': 'Thanhloveliv2004@',
        'CONN_MAX_AGE': 60
    }
}

# Your cache configuration
# See https://docs.djangoproject.com/en/1.8/topics/cache/#setting-up-the-cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60
    }
}

# Settings for the SMTP server that will be used to send email messages
# See https://docs.djangoproject.com/en/1.8/ref/settings/#email-host and other options
# Because i am deploying in local, it's don't have email.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'thanhloveliv2004@gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'hades'
EMAIL_HOST_PASSWORD = 'Thanhloveliv2004@'
# See https://docs.djangoproject.com/en/1.8/ref/settings/#email-use-tls
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

# Sender address for messages sent by the gameserver
DEFAULT_FROM_EMAIL = ''

# Filesystem path where user-uploaded files are stored
# This directory must be served by the web server under the path defined by MEDIA_URL in 'base_settings.py'
# ("/uploads" by default)
MEDIA_ROOT = '/etc/ctf_gameserver/web/'

# Base filesystem path where files for per-team downloads are stored, optional without per-team downloads
# A hierarchy with a directory per team (called by net number) is expected below this path
# For example, file "vpn.conf" for the team with net number 42 must be in:
#     <TEAM_DOWNLOADS_ROOT>/42/vpn.conf
# This directory must *not* be served by a web server
TEAM_DOWNLOADS_ROOT = ''

# The backend used to store user sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# A long, random string, which you are supposed to keep secret
SECRET_KEY = 'WE ONLY LIVE ON THE MISTAKES OF OTHERS'

# Insert all hostnames your site is available under
# See https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['100.79.145.28','10.10.16.30','localhost']

# The name of the time zone (i.e. something like "Europe/Berlin") in which dates should be displayed
# See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for a list of valid options
TIME_ZONE = 'Asia/Ho_Chi_Minh'
# First day of the week: 0 means Sunday, 1 means Monday and so on
FIRST_DAY_OF_WEEK = 1

# When using Graylog for checker logging, base URL for generating links to log searches
# Probably either "http://<host>:<port>/search" or "http://<host>:<port>/streams/<stream>/search"
#GRAYLOG_SEARCH_URL = 'http://localhost:9000/search'


# You should not have to edit anything below this line

# Set up logging to syslog
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['syslog'],
            'level': 'WARNING'
        }
    }
}

DEBUG = False

if HTTPS:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

