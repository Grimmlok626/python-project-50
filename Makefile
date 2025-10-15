.PHONY: install lint test test-coverage

install:
	pip install -e .

lint:
	ruff .

test:
	# Устанавливаем пакет, если не установлен, в режиме editable
	hatch run pip install -e .
	# Запускаем pytest с PYTHONPATH=., чтобы модуль был доступен
	PYTHONPATH=. hatch run pytest --maxfail=1 --disable-warnings

test-coverage:
	# Аналогично, с включением покрытия
	hatch run pip install -e .
	PYTHONPATH=. hatch run pytest --maxfail=1 --disable-warnings --cov=gendiff --cov-report=xml:coverage.xml