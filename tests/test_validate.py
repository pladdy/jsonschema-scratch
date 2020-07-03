import http
import json

ammy = {
    "name": "red amulet",
    "description": "This amulet is red.",
    "type": "amulet",
    "armor-class-types": ["edged", "blunt", "mind", "energy"],
}

invalid_ammy = {
    "name": "red amulet",
    "description": "This amulet is red.",
    "type": "amulet",
}


def test_validate_ok(client_in_test):
    r = client_in_test.post(
        "/validate?schema=equipment.json", data=json.dumps(ammy)
    )
    assert r.status_code == http.HTTPStatus.OK


def test_validate_bad_request(client_in_test):
    r = client_in_test.post("/validate", data=json.dumps(ammy))
    assert r.status_code == http.HTTPStatus.BAD_REQUEST


def test_validate_invalid_post(client_in_test):
    r = client_in_test.post(
        "/validate?schema=equipment.json", data=json.dumps(invalid_ammy)
    )
    assert r.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY
