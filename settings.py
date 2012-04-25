# -*- coding: utf-8 -*-
# Django settings 
from mongoengine import connect
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Mongo Database settings
connect('kolabria-new')

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

PATH = os.path.dirname(__file__)

MEDIA_ROOT = PATH + '/media/'
MEDIA_URL = '/media/' 
    
STATIC_ROOT = PATH + 'static/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    PATH + '/static',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testkolabria@gmail.com'
EMAIL_HOST_PASSWORD = 'test_kolabria'
EMAIL_PORT = 587
FROM_EMAIL = EMAIL_HOST_USER

ADMINS = (
    (u'admin', 'admin@kolabria.com'),     
)

INTERNAL_IPS = ('127.0.0.1',)
LOGIN_REDIRECT_URL = '/mywalls/'
LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'
AUTH_PROFILE_MODULE = 'users.Profile'


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PATH + '/database',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Montreal'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8!xvqfrfretert45564y6565655566ythhhhhh&k0c@ru)v'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'kolabria.urls'

TEMPLATE_DIRS = (
    PATH + '/templates',
)

# fixtures
FIXTURE_DIRS = (
    PATH + '/fixtures',
)

#DISQUS_API_KEY = 'rr3r45gg7hoAnpar32erwr32432rerSLlxoos2JpnY' 
#DISQUS_WEBSITE_SHORTNAME = 'pythonprogramcilari'


TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.localflavor',
    'django.contrib.markup',

#    'kolabria.polls',
    'posts',
    'links',
    'users',
    'main',
    'appliance',
    'walls',


    'debug_toolbar',
#    'disqus',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
