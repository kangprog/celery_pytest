import pytest
import time

from tasks.celery_task import work_task


#
# pytest shared_task example
# https://medium.com/@scythargon/how-to-use-celery-pytest-fixtures-for-celery-intergration-testing-6d61c91775d9
#

#
# celery_session_app, celery_session_worker가 fixture로 정의되지 않으면
# celery Worker가 없는 것으로 판단되어, Task가 실행되지 못하고 Time out 된다.
# 추가로, Task가 shared_task로 정의되어있지 않으면, fixture로 인해 생성된 celery app이 Task를 찾지 못하고 Time out 된다.
#

#
# usefixtures를 사용해서 celery_session_app, celery_session_worker를 데코레이터 하면,
# session fixture가 Docker Contaniner를 실행시키는 function fixture보다 먼저 실행된다.
# Celery Worker가 Broker를 찾지 못해서 Time Out 남.
#
# @pytest.mark.usefixtures('celery_session_app')
# @pytest.mark.usefixtures('celery_session_worker')
@pytest.mark.usefixtures('wait_for_docker')
class TestCeleryWork:
    def test_celery_work_return_one(
            self,
            celery_config,
            celery_app,
            celery_worker
    ):

        assert work_task.delay(1).get(timeout=10) == 1
        assert work_task.apply_async(args=[1]).get(timeout=10) == 1

    def test_celery_work_return_two(
            self,
            celery_config,
            celery_app,
            celery_worker
    ):
        assert work_task.delay(2).get(timeout=10) == 2
        assert work_task.apply_async(args=[2]).get(timeout=10) == 2
