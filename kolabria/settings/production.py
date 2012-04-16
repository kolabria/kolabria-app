from kolabria.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS += ('sentry,')

DATABASES['default']['NAME'] = 'kolabria_production.db'

SENTRY_LOG_DIR = os.path.join(PROJECT_DIR, 'logs')
SENTRY_RUN_DIR= os.path.join(PROJECT_DIR, 'run')
SENTRY_WEB_HOST = '127.0.0.1'
SENTRY_WEB_PORT = 9000
SENTRY_KEY = '86%96ay-ct*)3)s2(=0rozcb$0*9z(6#zxfi$-)#kih_ah_fu^'

SENTRY_FILTERS = (
    'sentry.filters.StatusFilter',
    'sentry.filters.LoggerFilter',
    'sentry.filters.LevelFilter',
    'sentry.filters.ServerNameFilter',
    'sentry.filters.SiteFilter',
)

SENTRY_VIEWS = (
    'sentry.views.Exception',
    'sentry.views.Message',
    'sentry.views.Query',
)


