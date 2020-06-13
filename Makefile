.PHONY: bump-patch bump-minor bump-major poetry run-debug
.PHONY: format lint security vulnerability
.PHONY: cov-reports cover test

APP = jsonschema_scratch
TEST = poetry run pytest -x -s -rA --durations=10 -vv --cov $(APP) $(TESTS)
TESTS = tests

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

cover-codacy: cov-reports
	poetry run coverage xml
	source .env && poetry run python-codacy-coverage -r coverage.xml

format:
	poetry run black -l 80 $(APP) $(TESTS)

install:
	poetry install

lint: format security
	poetry run flake8 $(APP) $(TESTS)

POETRY_VERSION = 1.0.9
poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/$(POETRY_VERSION)/get-poetry.py | python

run-debug:
	DEBUG=1 FLASK_ENV=development poetry run python jsonschema_scratch/app.py

security:
	poetry run bandit -r $(APP)

test:
	$(TEST)

vulnerability:
	poetry run safety check
