import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_quote_5s': {
        'task': 'quotes.tasks.get_quote',
        'schedule': 5.0
    }
}
app.autodiscover_tasks()
