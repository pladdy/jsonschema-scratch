import flask

from jsonschema_scratch import errors
from jsonschema_scratch import validate
from jsonschema_scratch import schema


def create_app():
    app = flask.Flask(__name__)
    app = errors.add_error_handlers(app)

    app.register_blueprint(validate.bp)
    app.register_blueprint(schema.bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
