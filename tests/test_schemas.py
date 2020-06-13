import json
import os
import pytest

from jsonschema_scratch import config


@pytest.fixture
def schemas():
    schema_files = []
    for dirpath, _, filenames in os.walk(config.SCHEMAS_DIR_NAME):
        schema_files += [
            os.path.join(dirpath, filename) for filename in filenames
        ]
    return schema_files


def test_schemas_valid_json(schemas):
    for schema in schemas:
        with open(schema) as f:
            assert json.load(f) is not None
