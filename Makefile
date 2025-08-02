# Makefile for DreamEngine 🧠

install:
	uv pip install -e .[dev]

lint:
	ruff check src/ tests/

format:
	black src/ tests/

typecheck:
	mypy src/

test:
	pytest -v

notebook:
	jupyter notebook

clean:
	rm -rf .pytest_cache __pycache__ */__pycache__ .mypy_cache dist build

all: install lint format typecheck test
