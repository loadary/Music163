#!/usr/bin/env python
# coding:utf-8

from celery import Celery

app = Celery('Music_163')
app.config_from_object('tasks.celeryconfig')

