DJANGO_LOCAL_SETTINGS=ghibli_challenge_django.settings
DJANGO_TEST_SETTINGS=$(DJANGO_LOCAL_SETTINGS)

run-local: install
	DJANGO_SETTINGS_MODULE=$(DJANGO_LOCAL_SETTINGS) python manage.py createcachetable
	DJANGO_SETTINGS_MODULE=$(DJANGO_LOCAL_SETTINGS) python manage.py runserver
tests: install-tests
	DJANGO_SETTINGS_MODULE=$(DJANGO_TEST_SETTINGS) pytest --cov=apps --cov-report term-missing apps
install:
	pip install -r requirements/common.txt
install-tests:
	pip install -r requirements/test.txt