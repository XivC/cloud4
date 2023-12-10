import os

from django.core.exceptions import ImproperlyConfigured

POSTGRES_URL = os.getenv('POSTGRES_URL', None)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', None)
CELERY_TASKS_DEFAULT_QUEUE = 'cloud4_celery'

if not POSTGRES_URL:
    raise ImproperlyConfigured('You must specify POSTGRES_URL env variable')

if not CELERY_BROKER_URL:
    raise ImproperlyConfigured('You must specify CELERY_BROKER_URL env variable')