.PHONY: requirements.txt

APP = jsonschema_scratch
TEST = poetry run pytest -x -s -rA --durations=10 -vv --cov $(APP) $(TESTS)
TESTS = tests

all:
	poetry install

bump-patch:
	poetry run dephell project bump patch

bump-minor:
	poetry run dephell project bump minor

bump-major:
	poetry run dephell project bump major

clean:

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

pre-commit-run:
	poetry run pre-commit run --all-files

release:
	git push && git push --tags

requirements.txt:
	poetry run dephell deps converts --to-format=pip --to-path=$@

run-debug:
	DEBUG=1 FLASK_ENV=development poetry run python $(APP)/app.py

security:
	poetry run bandit -r $(APP)

test:
	$(TEST)

update: update-with-poetry requirements.txt

update-with-poetry:
	poetry update

vulnerability:
	poetry run safety check
