# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Core exceptions module for consistent error handling
- StorageBackend abstract base class
- CODEOWNERS file for code review automation
- Separated unit and integration test directories
- GitHub Actions workflows for module-specific CI
- Contributing guidelines
- Pytest fixtures in conftest.py
- Makefile for common development tasks

### Changed
- Improved __init__.py with comprehensive docstrings
- Storage clients now inherit from StorageBackend
- Reorganized test structure (unit/ and integration/)
- Enhanced pyproject.toml with isort configuration
- Updated CI workflows to test specific modules

## [0.1.0] - 2025-11-18

### Added
- Initial release
- Storage abstraction (S3, MinIO, Local)
- Configuration management (YAML, JSON, ENV)
- AI services base (TTS generator)
- Test suite with pytest
- CI/CD with GitHub Actions
- Complete documentation

[Unreleased]: https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules/releases/tag/v0.1.0
