.PHONY: pylint
pylint:
	poetry run pylint .

.PHONY: flake8
flake8:
	poetry run flake8 .