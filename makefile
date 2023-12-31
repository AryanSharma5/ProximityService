install-deps:
	echo "installing dependencies"
	python -m pip install -r requirements.txt

linting:
	echo "running linter"
	python -m pylint src/

test:
	echo "running tests"
	python -m pytest