SHELL=/bin/bash

setup:
	python3 -m venv activityTwo; \
	source activityTwo/bin/activate; \
	pip3 install -r requirements.txt; \
	deactivate

run:
	source activityTwo/bin/activate; \
	env FLASK_APP=hello.py flask run

clean:
	rm -rf activityTwo
	py3clean .
