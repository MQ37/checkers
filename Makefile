test:
	python3 tests/run.py

run:
	python3 run.py

format:
	yapf -i -r game/

.PHONY: test run format
