SHELL=/bin/bash

setup:
	printf "#!/bin/bash\n./scripts/pre-commit.py" > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
	chmod +x scripts/pre-commit.py
	python3 -m venv activityTwo; \
	source activityTwo/bin/activate; \
	pip3 install wheel; \
	pip3 install -r requirements.txt; \
	deactivate

run:
	source activityTwo/bin/activate; \
	env FLASK_APP=hello.py flask run

clean:
	rm -rf activityTwo
	py3clean .
