from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

MIDDLEWARE += [
    # prod
    # "corsheaders.middleware.CorsMiddleware",
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'database',
#         'USER': 'database_user',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# -- -- -- -- -- -- STATIC AND MEDIA
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
