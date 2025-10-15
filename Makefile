.PHONY: install lint test test-coverage

install:
	pip install -e .

lint:
	ruff .

test:
	PYTHONPATH=${PYTHONPATH:=.} hatch run pytest --maxfail=1 --disable-warnings

test-coverage:
	# Аналогично, запуск с покрытием
	hatch run pip install -e .
	PYTHONPATH=. hatch run pytest --maxfail=1 --disable-warnings --cov=gendiff --cov-report=xml:coverage.xml