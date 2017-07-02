#!/usr/bin/env python
# coding:utf-8

from celery.schedules import crontab
from kombu import Exchange, Queue

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CELERY_IMPORTS = (
    'tasks.index',
    'tasks.playlist',
    'tasks.comment',
)


CELERY_QUEUES = (
    Queue('index_queue', exchange=Exchange('index_spider', type='direct'), routing_key='tasks_index'),
    Queue('playlist_queue', exchange=Exchange('playlist_spider', type='direct'), routing_key='tasks_playlist'),
    Queue('comment_queue', exchange=Exchange('comment_spider', type='direct'), routing_key='tasks_comment'),
)

CELERYBEAT_SCHEDULE = {
    'run-comment-at-some-time': {
        'task': 'tasks.comment_task.index',
        'schedule': crontab(hour=9, minute=0),
        'args': ('http://music.163.com/discover', )
    }
}

