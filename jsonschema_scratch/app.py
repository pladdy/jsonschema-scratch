import flask
import http
import json
import jsonschema
import os

SCHEMAS_DIR_NAME = "schemas"
SCHEMAS_RELATIVE_PATH = "../schemas"


def create_app():
    # One way to serve static files is using static* params:
    # Example:
    # flask.Flask(static_url_path="/schemas", static_folder="../schemas")
    app = flask.Flask(__name__)

    @app.errorhandler(http.HTTPStatus.NOT_FOUND)
    def not_found(error):
        print(dir(error))
        return flask.jsonify({"error": str(error)}), http.HTTPStatus.NOT_FOUND

    @app.errorhandler(http.HTTPStatus.METHOD_NOT_ALLOWED)
    def method_not_allowed(error):
        print(dir(error))
        return (
            flask.jsonify({"error": str(error)}),
            http.HTTPStatus.METHOD_NOT_ALLOWED,
        )

    @app.route("/")
    def foo():
        return flask.jsonify({"message": "hello"})

    @app.route("/schemas/<path:filename>")
    def schema(filename):
        return flask.send_from_directory(SCHEMAS_RELATIVE_PATH, filename)

    @app.route("/validate", methods=["POST"])
    def validate():
        with open(os.path.join(SCHEMAS_DIR_NAME, "weapon.json")) as f:
            schema = json.load(f)

        valid, summary = validate_against_schema(flask.request.data, schema)
        return flask.jsonify({"valid": valid, "summary": summary})

    return app


def validate_against_schema(document, schema):
    try:
        jsonschema.validate(
            instance=json.loads(flask.request.data), schema=schema
        )
        return True, "valid"
    except jsonschema.exceptions.ValidationError as e:
        print(e)
        return False, str(e)


if __name__ == "__main__":
    app = create_app()
    app.run()
