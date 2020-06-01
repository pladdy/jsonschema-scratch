import flask
import http
import json
import jsonschema
import os

import jsonschema_scratch.errors as errors

SCHEMAS_DIR_NAME = "schemas"
SCHEMAS_RELATIVE_PATH = "../schemas"


def create_app():
    # One way to serve static files is using static* params:
    # Example:
    # flask.Flask(static_url_path="/schemas", static_folder="../schemas")
    app = flask.Flask(__name__)
    app = errors.add_error_handlers(app)

    @app.route("/schemas/", defaults={"filename": ""})
    @app.route("/schemas/<path:filename>")
    def schema(filename):
        try:
            path = os.path.join(SCHEMAS_DIR_NAME, filename)

            if os.path.isfile(path):
                return flask.send_from_directory(
                    SCHEMAS_RELATIVE_PATH, filename
                )
            if os.path.isdir(path):
                return flask.jsonify({"files": [os.listdir(path)]})
        except Exception as e:
            flask.abort(
                http.HTTPStatus.NOT_FOUND,
                {"summary": "Schema not found", "error": e},
            )
        flask.abort(http.HTTPStatus.NOT_FOUND, {"summary": "Schema not found"})

    @app.route("/validate", methods=["POST"])
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
                os.path.join(SCHEMAS_DIR_NAME, flask.request.args.get("schema"))
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

    return app


def validate_against_schema(document, schema):
    try:
        jsonschema.validate(
            instance=json.loads(flask.request.data), schema=schema
        )
        return True, "valid"
    except jsonschema.exceptions.ValidationError as e:
        return False, e


if __name__ == "__main__":
    app = create_app()
    app.run()
