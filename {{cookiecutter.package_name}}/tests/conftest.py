import pytest

from {{ cookiecutter.package_name }}.api import app as service_app, app_init


@pytest.fixture(scope="session")
def app():
    # load configuration
    # service_app.config.from_object('{{ cookiecutter.package_name }}.test_settings')
    app_init(service_app)
    return service_app
