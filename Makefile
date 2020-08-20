DJANGO_LOCAL_SETTINGS=ghibli_challenge_django.settings.settings_base
DJANGO_TEST_SETTINGS=$(DJANGO_LOCAL_SETTINGS)
DJANGO_PROD_SETTINGS=ghibli_challenge_django.settings.settings_prod

run-local: install
	DJANGO_SETTINGS_MODULE=$(DJANGO_LOCAL_SETTINGS) python manage.py createcachetable
	DJANGO_SETTINGS_MODULE=$(DJANGO_LOCAL_SETTINGS) python manage.py runserver
run-gunicorn: install
	GUNICORN_CMD_ARGS="--workers=1 --threads=1" gunicorn ghibli_challenge_django.wsgi
tests: install-tests
	DJANGO_SETTINGS_MODULE=$(DJANGO_TEST_SETTINGS) pytest --cov=apps --cov-report term-missing apps
	pep8 --exclude venv .
install:
	pip install -r requirements/common.txt
install-tests:
	pip install -r requirements/test.txt
