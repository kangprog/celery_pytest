import pytest
pytest_plugins = ["docker_compose"]


#
# https://github.com/pytest-docker-compose/pytest-docker-compose
# 테스트용 docker-compose.yml을 pytest 실행, 동작시 실행, 정지를 해준다.
# 아래 function에서 사용하는 docker compose 파일은 아래와 같은 경로에 위치해야한다.
# ./docker-compose.yml
#
# fixture function, module, session 사용처
# https://velog.io/@sangyeon217/pytest-fixture
#
@pytest.fixture(scope="module")
def wait_for_docker(module_scoped_container_getter):
    #
    # api server 같은 request가 필요한 Container라면,
    # 여기서 url 리턴하는 로직이 추가되면 된다.
    #
    # yield를 넣어봤으나, pass와 별다를 점이 없다.
    # class test에서 mark.fixtures로 들어가서 해당 class test가 끝날때까지는 유지되는듯?
    #
    pass


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'redis://127.0.0.1/1',
        'result_backend': 'redis://127.0.0.1/1'
    }