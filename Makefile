# install only in venv, please

install:
	pip install poetry
	poetry install
	pre-commit install
