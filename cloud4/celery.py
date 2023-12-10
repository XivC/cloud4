import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

from cloud4 import conf

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloud4.settings')

celery = Celery('app')

celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.conf['CELERY_BROKER_URL'] = conf.CELERY_BROKER_URL

celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

celery.conf.beat_schedule = {
    'test_task': {
        'task': 'update_recommendations',
        'schedule': 60,
    }
}
