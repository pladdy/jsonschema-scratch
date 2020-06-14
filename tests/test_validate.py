import http
import json

ammy = {
    "name": "red amulet",
    "description": "This amulet is red.",
    "type": "amulet",
    "armor-class-types": ["edged", "blunt", "mind", "energy"],
}


def test_validate(client_in_test):
    r = client_in_test.post(
        "/validate?schema=equipment.json", data=json.dumps(ammy)
    )
    assert r.status_code == http.HTTPStatus.OK
