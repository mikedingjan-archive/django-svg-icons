.PHONY: clean


default: develop

clean:
	find src -name '*.pyc' | xargs rm
	find src -name '*.egg-info' | xargs rm -rf

develop: clean
	pip install -e .

lint:
	flake8 `find src -name '*.py'`
