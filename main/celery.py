from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
#     'send-email-every-30-seconds': {
#         'task': 'app.tasks.send_email',
#         'schedule': 30.0
#     },
# }

# # app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))