import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petshop.settings")

app = Celery("petshop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def test_task(a, b):
    return a + b