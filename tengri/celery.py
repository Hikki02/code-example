import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tengri.settings.development')

app = Celery('tengri')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'update-status-every-1-minutes': {
        'task': 'apps.business_trips.tasks.update_soon_status_task',
        'schedule': crontab(minute='0', hour='0'),
    },
    'delete-unconfirmed-users-every-1-minutes': {
        'task': 'apps.users.tasks.delete_unconfirmed_users',
        'schedule': crontab(minute='*/1'),
    },
}
