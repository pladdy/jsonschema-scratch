.PHONY: bump-patch bump-minor bump-major format lint run-debug security test

APP = jsonschema_scratch
TESTS = tests

TEST = poetry run pytest -x -s -rA --durations=10 -vv --cov $(APP) $(TESTS)

bump-patch:
	poetry run bumpversion patch

bump-minor:
	poetry run bumpversion minor

bump-major:
	poetry run bumpversion major

cov-reports:
	$(TEST) --cov-report html

cover: cov-reports
	open htmlcov/index.html

format:
	poetry run black -l 80 $(APP) $(TESTS)

lint: format security
	poetry run flake8 $(APP) $(TESTS)

run-debug:
	DEBUG=1 FLASK_ENV=development poetry run python jsonschema_scratch/app.py

security:
	poetry run bandit -r $(APP)

test:
	$(TEST)

vulnerability:
	poetry run safety check
