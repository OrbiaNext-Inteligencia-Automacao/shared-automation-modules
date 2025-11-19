# Contributing to Shared Automation Modules

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git
cd shared-automation-modules
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Code Style

We use:
- **Black** for code formatting (line length: 100)
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

Run formatting before committing:
```bash
make format
```

Run linting:
```bash
make lint
```

## Testing

### Run all tests:
```bash
make test
```

### Run only unit tests:
```bash
pytest tests/unit/ -v
```

### Run only integration tests:
```bash
pytest tests/integration/ -v
```

### Test a specific module:
```bash
pytest tests/unit/test_storage.py -v
```

### With coverage:
```bash
pytest --cov=shared_modules --cov-report=html
```

## Branch Strategy

- `main`/`master` - Production-ready code
- `develop` - Integration branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent fixes

## Workflow

1. Create a feature branch:
```bash
git checkout -b feature/add-new-storage-backend
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Add Azure Blob Storage backend"
```

3. Push and create PR:
```bash
git push origin feature/add-new-storage-backend
gh pr create --base develop
```

4. Wait for CI to pass and code review

5. Merge after approval

## Module Structure

When adding a new module, follow this pattern:

```
src/shared_modules/new_module/
├── __init__.py          # Public API exports
├── base.py              # Abstract base classes
├── implementation.py    # Concrete implementations
└── utils.py             # Helper functions
```

And corresponding tests:

```
tests/
├── unit/
│   └── test_new_module.py
└── integration/
    └── test_new_module_integration.py
```

## Code Review Checklist

- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Type hints added
- [ ] Code formatted with black
- [ ] Linting passes
- [ ] CI passes
- [ ] No breaking changes (or documented)

## Release Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create release tag:
```bash
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0
```

## Questions?

Open an issue or contact the maintainers.
