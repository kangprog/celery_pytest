from celery import shared_task
from celery_app import app


@shared_task
@app.task
def work_task(number):
    if number == 1:
        print(f"input number is {number}")
        return number
    else:
        print(f"input number is {number}")
        return number
