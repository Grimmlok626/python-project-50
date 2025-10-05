lint:
	flake8 . --config=.flake8

test:
	pytest --maxfail=1 --disable-warnings -q

test-coverage:
	pytest --maxfail=1 --disable-warnings --cov=src/hexlet_code --cov-report=xml:coverage.xml
