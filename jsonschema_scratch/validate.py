import flask
import http
import json
import jsonschema
import os

from . import config

bp = flask.Blueprint("validate", __name__)


@bp.route("/validate", methods=["POST"])
def validate():
    schema = flask.request.args.get("schema")

    if schema is None:
        flask.abort(
            http.HTTPStatus.BAD_REQUEST,
            {
                "summary": "Specify a schema with '?schema=<schema>'",
                "error": "schema not specified",
            },
        )

    try:
        with open(
            os.path.join(
                config.SCHEMAS_DIR_NAME, flask.request.args.get("schema")
            )
        ) as f:
            schema = json.load(f)
    except Exception as e:
        flask.abort(
            http.HTTPStatus.BAD_REQUEST,
            {"summary": "Specified schema is invalid JSON", "error": e},
        )

    try:
        valid, summary = validate_against_schema(flask.request.data, schema)
        if valid:
            return flask.jsonify(
                {"valid": valid, "summary": json.loads(flask.request.data)}
            )
        flask.abort(
            http.HTTPStatus.UNPROCESSABLE_ENTITY,
            {"summary": "Validation failed", "error": summary},
        )
    except Exception as e:
        flask.abort(
            http.HTTPStatus.UNPROCESSABLE_ENTITY,
            {"summary": "Validation failed", "error": e},
        )


def validate_against_schema(document, schema):
    try:
        jsonschema.validate(
            instance=json.loads(flask.request.data), schema=schema
        )
        return True, "valid"
    except jsonschema.exceptions.ValidationError as e:
        return False, e
