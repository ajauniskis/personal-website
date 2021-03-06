venv_dir = .venv
venv_activate = . $(venv_dir)/bin/activate

install: venv_setup
	poetry install

venv_setup:
	python3 -m venv $(venv_dir)

run:
	$(venv_activate); python manage.py runserver

migrate:
	$(venv_activate); python manage.py makemigrations
	$(venv_activate); python manage.py migrate

test:
	$(venv_activate); python manage.py test

all: venv_setup install run
