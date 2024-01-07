from __future__ import absolute_import
import os

import environ
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
environ.Env.read_env('../.env')

app = Celery('config')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'run-task-8am': {
        'task': 'quotes.tasks.sending_daily_quote_task',
        'schedule': crontab(hour=8, minute=0),
    },
    'run-task-1pm': {
        'task': 'quotes.tasks.sending_daily_quote_task',
        'schedule': crontab(hour=13, minute=0),
    },
    'run-task-7pm': {
        'task': 'quotes.tasks.sending_daily_quote_task',
        'schedule': crontab(hour=19, minute=0),
    },
}

'''
crontab() - every minute
crontab(minute='*/15') - every 15 minutes
crontab(minute=0, hour='*') - every hour
crontab(minute=0, hour='*/3') - every 3 hours
crontab(minute=0, hour=0) - daily midnight
'''


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
