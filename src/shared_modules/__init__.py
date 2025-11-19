"""Shared Automation Modules - Core utilities for video automation pipelines.

This package provides reusable components for video automation projects:
- Storage abstraction (S3, MinIO, Local)
- Configuration management (YAML, JSON, ENV)
- AI services (TTS, LLM, Vision)
- Video processing utilities
- Monitoring and logging

Example:
    >>> from shared_modules import UnifiedStorageClient, ConfigManager
    >>> storage = UnifiedStorageClient(backend="s3", bucket="my-bucket")
    >>> config = ConfigManager("config.yaml")
"""

__version__ = "0.1.0"
__author__ = "OrbiaNext Automation Team"

# Public API - import only these from shared_modules
from .storage import UnifiedStorageClient, S3Client, LocalClient
from .config import ConfigManager

# Will be added as modules are implemented
# from .ai import TTSGenerator, LLMClient
# from .video import VideoRenderer
# from .monitoring import MetricsCollector, StructuredLogger

__all__ = [
    # Version
    "__version__",
    "__author__",
    
    # Storage
    "UnifiedStorageClient",
    "S3Client", 
    "LocalClient",
    
    # Config
    "ConfigManager",
    
    # AI (coming soon)
    # "TTSGenerator",
    # "LLMClient",
    
    # Video (coming soon)
    # "VideoRenderer",
    
    # Monitoring (coming soon)
    # "MetricsCollector",
    # "StructuredLogger",
]
