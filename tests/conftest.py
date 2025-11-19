"""Pytest configuration and shared fixtures."""

import pytest
from pathlib import Path
import tempfile
import shutil


@pytest.fixture
def tmp_path():
    """Create a temporary directory for tests."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.fixture
def sample_config_yaml(tmp_path):
    """Create a sample YAML config file."""
    config_file = tmp_path / "config.yaml"
    config_content = """
database:
  host: localhost
  port: 5432
  name: test_db

storage:
  backend: local
  base_path: ./data

api:
  key: test-api-key
  endpoint: https://api.example.com
"""
    config_file.write_text(config_content)
    return config_file


@pytest.fixture
def sample_config_json(tmp_path):
    """Create a sample JSON config file."""
    import json
    config_file = tmp_path / "config.json"
    config_data = {
        "app": {
            "name": "test-app",
            "version": "1.0.0"
        },
        "features": {
            "enable_cache": True,
            "max_workers": 4
        }
    }
    config_file.write_text(json.dumps(config_data, indent=2))
    return config_file


@pytest.fixture
def sample_text_file(tmp_path):
    """Create a sample text file for storage tests."""
    text_file = tmp_path / "test.txt"
    text_file.write_text("Hello, World! This is a test file.")
    return text_file


@pytest.fixture
def sample_binary_file(tmp_path):
    """Create a sample binary file for storage tests."""
    binary_file = tmp_path / "test.bin"
    binary_file.write_bytes(b"\x00\x01\x02\x03\x04\x05")
    return binary_file
