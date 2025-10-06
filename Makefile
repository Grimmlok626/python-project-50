lint:
	flake8 . --config=.flake8

test:
	PYTHONPATH=. pytest --maxfail=1 --disable-warnings -q

test-coverage:
	PYTHONPATH=src pytest --maxfail=1 --disable-warnings --cov=src/hexlet_code --cov-report=xml:coverage.xml
