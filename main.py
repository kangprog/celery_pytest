from tasks.celery_task import work_task


if __name__ == "__main__":

    true_response_task = work_task.apply_async(args=[1])
    false_response_task = work_task.apply_async(args=[2])
