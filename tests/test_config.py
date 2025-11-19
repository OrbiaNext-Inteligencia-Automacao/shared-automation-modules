"""Tests for ConfigManager."""

import pytest
import yaml
import json
from pathlib import Path
from shared_modules.config import ConfigManager


class TestConfigManager:
    """Test suite for ConfigManager."""
    
    def test_load_yaml_config(self, tmp_path):
        """Test loading YAML configuration."""
        config_file = tmp_path / "config.yaml"
        config_data = {
            "database": {
                "host": "localhost",
                "port": 5432
            },
            "api_key": "test-key"
        }
        
        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)
        
        manager = ConfigManager(str(config_file))
        assert manager.get("database.host") == "localhost"
        assert manager.get("database.port") == 5432
        assert manager.get("api_key") == "test-key"
    
    def test_load_json_config(self, tmp_path):
        """Test loading JSON configuration."""
        config_file = tmp_path / "config.json"
        config_data = {
            "app": {
                "name": "test-app",
                "version": "1.0.0"
            }
        }
        
        with open(config_file, 'w') as f:
            json.dump(config_data, f)
        
        manager = ConfigManager(str(config_file))
        assert manager.get("app.name") == "test-app"
        assert manager.get("app.version") == "1.0.0"
    
    def test_get_with_default(self):
        """Test getting config with default value."""
        manager = ConfigManager()
        assert manager.get("nonexistent.key", default="default_value") == "default_value"
    
    def test_set_config(self):
        """Test setting configuration values."""
        manager = ConfigManager()
        manager.set("new.nested.key", "value")
        assert manager.get("new.nested.key") == "value"
    
    def test_merge_config(self):
        """Test merging configurations."""
        manager = ConfigManager()
        manager.set("app.name", "original")
        manager.set("app.version", "1.0")
        
        manager.merge({
            "app": {
                "version": "2.0",
                "description": "Updated"
            },
            "new_key": "new_value"
        })
        
        assert manager.get("app.name") == "original"
        assert manager.get("app.version") == "2.0"
        assert manager.get("app.description") == "Updated"
        assert manager.get("new_key") == "new_value"
    
    def test_save_config(self, tmp_path):
        """Test saving configuration to file."""
        manager = ConfigManager()
        manager.set("test.key", "value")
        
        output_file = tmp_path / "output.yaml"
        manager.save(str(output_file))
        
        # Load and verify
        new_manager = ConfigManager(str(output_file))
        assert new_manager.get("test.key") == "value"
