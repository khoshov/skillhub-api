PYTHON := docker-compose run -u $(USERID):$(GROUPID) --rm django python

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

collectstatic:
	$(PYTHON) manage.py collectstatic --noi -c

startapp:
	$(PYTHON) manage.py startapp ${app}

makemigrations:
	$(PYTHON) manage.py makemigrations ${app}

migrate:
	$(PYTHON) manage.py migrate ${app}

createsuperuser:
	$(PYTHON) manage.py createsuperuser

shell:
	$(PYTHON) manage.py shell_plus

reset_db:
	$(PYTHON) manage.py reset_db
