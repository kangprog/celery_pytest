from celery import Celery


app = Celery(
    'app',
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
    include=[
        'tasks.celery_task'
    ]
)
