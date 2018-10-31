import pytest
from SERVICE_NAME.app import app as service_app

@pytest.fixture(scope='session')
def app():
    return service_app
