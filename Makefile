tests: install-tests
	pytest --cov=apps --cov-report term-missing apps
	pytest --cov=ghibli_challenge_django --cov-report term-missing ghibli_challenge_django
install:
	pip install -r requirements/common.txt
install-tests:
	pip install -r requirements/test.txt