import flask
import http
import jsonref
import os

from jsonschema_scratch import config

# An alternate way to serve static files is using static* params:
#
# Example:
# flask.Flask(static_url_path="/schemas", static_folder="../schemas")
#
# This app uses `send_from_directory` for now.

bp = flask.Blueprint("schemas", __name__)


def render_schema(path, filename):
    if "resolve" in flask.request.args.keys():
        with open(path) as schema:
            print(path)
            print(config.SCHEMAS_ABS_DIR)
            return flask.jsonify(
                jsonref.loads(schema.read(), base_uri=config.SCHEMAS_BASE_URI)
            )
    return flask.send_from_directory(config.SCHEMAS_RELATIVE_PATH, filename)


@bp.route("/schemas/", defaults={"filename": ""})
@bp.route("/schemas/<path:filename>")
def schema(filename):
    try:
        path = os.path.join(config.SCHEMAS_DIR_NAME, filename)

        if os.path.isfile(path):
            return render_schema(path, filename)
        if os.path.isdir(path):
            return flask.jsonify({"files": [os.listdir(path)]})
    except Exception as e:
        flask.abort(
            http.HTTPStatus.NOT_FOUND,
            {"summary": "Schema not found", "error": e},
        )
    flask.abort(http.HTTPStatus.NOT_FOUND, {"summary": "Schema not found"})
