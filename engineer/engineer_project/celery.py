import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineer_project.settings")

app = Celery("engineer_project") # название Celery
app.config_from_object("django.conf:settings", namespace="CELERY") #
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

@app.task()
def debug_task():
    a= [12,12]
    len(a)
    time.sleep(10)
    print('run debug task')