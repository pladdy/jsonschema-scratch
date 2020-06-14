import pytest

from jsonschema_scratch.app import create_app


@pytest.fixture
def app_in_test():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client_in_test(app_in_test):
    return app_in_test.test_client()
