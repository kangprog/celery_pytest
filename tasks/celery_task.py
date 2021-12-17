from celery_app import app


@app.task
def work_task(self, number):
    if number == 1:
        print(f"input number is {number}")
        return number
    else:
        print(f"input number is {number}")
        return number
