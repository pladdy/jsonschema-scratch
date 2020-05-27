import flask


def create_app():
    app = flask.Flask(
        __name__, static_url_path="/schemas", static_folder="../schemas"
    )

    @app.route("/")
    def foo():
        return flask.jsonify({"message": "hello"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
