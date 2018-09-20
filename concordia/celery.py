from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from raven import Client
from raven.contrib.celery import register_logger_signal, register_signal

SENTRY_DSN = os.environ.get("SENTRY_DSN", None)

if SENTRY_DSN:
    client = Client(SENTRY_DSN)
    register_logger_signal(client)
    register_signal(client)

app = Celery("concordia")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
