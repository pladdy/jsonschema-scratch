import flask

SCHEMAS_DIR = "../schemas"


def create_app():
    # One way to serve static files is using static* params:
    # Example:
    # flask.Flask(static_url_path="/schemas", static_folder="../schemas")
    app = flask.Flask(__name__)

    @app.route("/")
    def foo():
        return flask.jsonify({"message": "hello"})

    @app.route("/schemas/<path:filename>")
    def schema(filename):
        print({"args": flask.request.args})
        return flask.send_from_directory(SCHEMAS_DIR, filename)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
