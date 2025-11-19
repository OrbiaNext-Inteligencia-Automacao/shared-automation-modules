"""Shared Automation Modules - Core utilities for video automation pipelines."""

__version__ = "0.1.0"

from .storage import UnifiedStorageClient
from .config import ConfigManager

__all__ = ["UnifiedStorageClient", "ConfigManager", "__version__"]
