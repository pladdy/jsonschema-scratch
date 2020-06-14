import http


def test_app_schema(client_in_test):
    r = client_in_test.get("/schemas/invalid")
    assert r.status_code == http.HTTPStatus.NOT_FOUND

    r = client_in_test.get("/schemas/weapon.json")
    assert r.status_code == http.HTTPStatus.OK
