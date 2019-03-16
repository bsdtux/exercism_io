lint:
	pipenv run isort -rc .
	pipenv run flake8 .
	pipenv run pylint * -r n --ignore=Makefile,README.md

test:
	pipenv run pytest ./two_fer_test.py