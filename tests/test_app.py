import http
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


def test_app_root(client_in_test):
    r = client_in_test.get("/")
    assert r.status_code == http.HTTPStatus.OK
    assert r.get_json() == {"message": "hello"}


def test_app_schema(client_in_test):
    r = client_in_test.get("/schemas/invalid")
    assert r.status_code == http.HTTPStatus.NOT_FOUND

    r = client_in_test.get("/schemas/weapon.json")
    assert r.status_code == http.HTTPStatus.OK
