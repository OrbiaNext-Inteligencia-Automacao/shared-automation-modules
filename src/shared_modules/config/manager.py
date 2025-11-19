"""Configuration manager for YAML, JSON, and environment variables."""

import os
import yaml
import json
from pathlib import Path
from typing import Any, Dict, Optional
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


class ConfigManager:
    """Unified configuration manager."""
    
    def __init__(self, config_file: Optional[str] = None, load_env: bool = True):
        """
        Initialize configuration manager.
        
        Args:
            config_file: Path to config file (YAML or JSON)
            load_env: Whether to load .env file
        """
        self.config: Dict[str, Any] = {}
        
        if load_env:
            load_dotenv()
            logger.info("Loaded environment variables from .env")
        
        if config_file:
            self.load_file(config_file)
    
    def load_file(self, file_path: str) -> None:
        """
        Load configuration from file.
        
        Args:
            file_path: Path to YAML or JSON config file
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {file_path}")
        
        with open(path, 'r') as f:
            if path.suffix in ['.yaml', '.yml']:
                self.config = yaml.safe_load(f)
            elif path.suffix == '.json':
                self.config = json.load(f)
            else:
                raise ValueError(f"Unsupported config format: {path.suffix}")
        
        logger.info(f"Loaded configuration from {file_path}")
    
    def get(self, key: str, default: Any = None, from_env: bool = True) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Config key (supports dot notation: "database.host")
            default: Default value if key not found
            from_env: Also check environment variables
            
        Returns:
            Configuration value
        """
        # Try environment variable first
        if from_env:
            env_key = key.upper().replace('.', '_')
            env_value = os.getenv(env_key)
            if env_value is not None:
                return env_value
        
        # Navigate nested keys
        value = self.config
        for part in key.split('.'):
            if isinstance(value, dict):
                value = value.get(part)
                if value is None:
                    return default
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Config key (supports dot notation)
            value: Value to set
        """
        parts = key.split('.')
        config = self.config
        
        for part in parts[:-1]:
            if part not in config:
                config[part] = {}
            config = config[part]
        
        config[parts[-1]] = value
        logger.debug(f"Set config {key} = {value}")
    
    def merge(self, other_config: Dict[str, Any]) -> None:
        """
        Merge another configuration dict.
        
        Args:
            other_config: Dict to merge
        """
        self._deep_merge(self.config, other_config)
        logger.info("Merged additional configuration")
    
    def _deep_merge(self, base: dict, update: dict) -> None:
        """Recursively merge update dict into base dict."""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary."""
        return self.config.copy()
    
    def save(self, file_path: str) -> None:
        """
        Save configuration to file.
        
        Args:
            file_path: Path to save config (YAML or JSON)
        """
        path = Path(file_path)
        
        with open(path, 'w') as f:
            if path.suffix in ['.yaml', '.yml']:
                yaml.dump(self.config, f, default_flow_style=False)
            elif path.suffix == '.json':
                json.dump(self.config, f, indent=2)
            else:
                raise ValueError(f"Unsupported config format: {path.suffix}")
        
        logger.info(f"Saved configuration to {file_path}")
