import werkzeug.exceptions
import jsonschema_scratch.errors as errors


def test_error_message():
    e = werkzeug.exceptions.HTTPException(description={"summary": "foo"})
    result = errors.error_message(e)
    assert result.get("error") == "None"
    assert result.get("summary") == "foo"
