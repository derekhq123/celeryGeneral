from __future__ import absolute_import
from celery import Celery

app=Celery('demo')
app.config_from_object('celery_server.celeryconfig')
