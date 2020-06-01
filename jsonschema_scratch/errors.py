import flask
import http


def add_error_handlers(app):
    app.register_error_handler(http.HTTPStatus.BAD_REQUEST, bad_request)
    app.register_error_handler(
        http.HTTPStatus.METHOD_NOT_ALLOWED, method_not_allowed
    )
    app.register_error_handler(http.HTTPStatus.NOT_FOUND, not_found)
    app.register_error_handler(
        http.HTTPStatus.UNPROCESSABLE_ENTITY, unprocessable_entity
    )
    return app


def error_message(error):
    """
    Takes a werkzeug HTTPException as an argument.

    Returns a dictionary that represents an error message for a client.
    """
    error_description = error.description

    msg = {"error": str(error_description.get("error"))}
    if error_description.get("summary"):
        msg["summary"] = error_description.get("summary")

    # TODO: log this with stack trace
    print("Error: {}".format(msg))
    return msg


def bad_request(error):
    return (flask.jsonify(error_message(error)), http.HTTPStatus.BAD_REQUEST)


def method_not_allowed(error):
    return (
        flask.jsonify(error_message(error)),
        http.HTTPStatus.METHOD_NOT_ALLOWED,
    )


def not_found(error):
    return flask.jsonify(error_message(error)), http.HTTPStatus.NOT_FOUND


def unprocessable_entity(error):
    return (
        flask.jsonify(error_message(error)),
        http.HTTPStatus.UNPROCESSABLE_ENTITY,
    )
