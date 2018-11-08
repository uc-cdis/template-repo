import pytest

from service_name.api import app as service_app, app_init


@pytest.fixture(scope='session')
def app():
    # load configuration
    # service_app.config.from_object('service_name.test_settings')
    app_init(service_app)
    return service_app
