.PHONY: install install-dev install-all test test-unit test-integration lint format clean build help

help:
	@echo "Available commands:"
	@echo "  make install          - Install base package"
	@echo "  make install-dev      - Install with dev dependencies"
	@echo "  make install-all      - Install all optional dependencies"
	@echo "  make test             - Run all tests"
	@echo "  make test-unit        - Run unit tests only"
	@echo "  make test-integration - Run integration tests only"
	@echo "  make lint             - Run linters (flake8, mypy)"
	@echo "  make format           - Format code (black, isort)"
	@echo "  make clean            - Clean build artifacts"
	@echo "  make build            - Build package"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

install-all:
	pip install -e ".[dev,ai,video,ml]"

test:
	pytest tests/ -v --cov=shared_modules --cov-report=html --cov-report=term

test-unit:
	pytest tests/unit/ -v -m unit --cov=shared_modules --cov-report=term

test-integration:
	pytest tests/integration/ -v -m integration --cov=shared_modules --cov-report=term

lint:
	flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	python -m build

publish-test:
	python -m twine upload --repository testpypi dist/*

publish:
	python -m twine upload dist/*
