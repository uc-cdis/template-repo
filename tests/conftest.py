import pytest

from SERVICE_NAME.api import app as service_app, app_init


@pytest.fixture(scope='session')
def app():
    # load configuration
    # service_app.config.from_object('SERVICE_NAME.test_settings')
    app_init(service_app)
    return service_app
