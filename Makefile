.PHONY: install test lint

install:
	pipenv install --dev

test:
	pipenv run pytest

lint:
	pipenv run flake8 .
	pipenv run black .
