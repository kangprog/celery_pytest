import pytest


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'redis://127.0.0.1/1',
        'result_backend': 'redis://127.0.0.1/1'
    }