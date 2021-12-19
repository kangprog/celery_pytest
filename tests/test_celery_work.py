import pytest
from tasks.celery_task import work_task


#
# pytest shared_task example
# https://medium.com/@scythargon/how-to-use-celery-pytest-fixtures-for-celery-intergration-testing-6d61c91775d9
#

@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
def test_celery_work_return_one():
    assert work_task.delay(1).get(timeout=10) == 1
    assert work_task.apply_async(args=[1]).get(timeout=10) == 1


def test_celery_work_return_two():
    assert work_task.delay(2).get(timeout=10) == 2
    assert work_task.apply_async(args=[2]).get(timeout=10) == 2
