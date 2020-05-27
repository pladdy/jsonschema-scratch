bump-patch:
	poetry run bumpversion patch

run-debug:
	DEBUG=1 FLASK_ENV=development FLASK_APP=jsonschema_scratch/app.py poetry run flask run
	# or
	# DEBUG=1 FLASK_ENV=development poetry run python jsonschema_scratch/app.py

test:
	poetry run pytest -x -s -rA --durations=0 -v tests/
