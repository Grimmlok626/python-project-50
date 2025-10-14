lint:
	flake8 . --config=.flake8

test:
	PYTHONPATH=gendiff python -m pytest --maxfail=1 --disable-warnings -q

test-coverage:
	PYTHONPATH=gendiff pytest --maxfail=1 --disable-warnings --cov=src --cov-report=xml:coverage.xml
