.PHONY: requirements.txt

APP = jsonschema_scratch

POETRY_VERSION = 1.0.9

TEST = poetry run pytest -x -s -rA --durations=10 -vv --cov $(APP) $(TEST_DIR)
TEST_DIR = tests

all: poetry install
	poetry run pre-commit install

bump-major:
	echo install bumpversion

bump-minor:
	echo install bumpversion

bump-patch:
	echo install bumpversion

bump-reset:
	git reset HEAD~1

clean:
	find ./ -type d -name *__pycache__ -exec rm -rf {} \;
	rm .coverage coverage.xml
	rm -rf .pytest_cache htmlcov

cov-reports:
	$(TEST) --cov-report html

cover: cov-reports
	open htmlcov/index.html

cover-codacy: cov-reports
	poetry run coverage xml
	source .env && poetry run python-codacy-coverage -r coverage.xml

install:
	poetry install

poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/$(POETRY_VERSION)/get-poetry.py | python

pre-commit-run:
	poetry run pre-commit run --all-files

release:
	git push && git push --tags

run-debug:
	DEBUG=1 FLASK_ENV=development poetry run python $(APP)/app.py

test:
	$(TEST)

update: update-with-poetry requirements.txt

update-with-poetry:
	poetry update

vulnerability:
	poetry run safety check
