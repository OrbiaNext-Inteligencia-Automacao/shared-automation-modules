"""Custom exceptions for shared modules."""


class SharedModulesError(Exception):
    """Base exception for all shared modules errors."""
    pass


class ConfigurationError(SharedModulesError):
    """Raised when configuration is invalid or missing."""
    pass


class StorageError(SharedModulesError):
    """Raised when storage operations fail."""
    pass


class AIServiceError(SharedModulesError):
    """Raised when AI service operations fail."""
    pass


class VideoProcessingError(SharedModulesError):
    """Raised when video processing operations fail."""
    pass


class MonitoringError(SharedModulesError):
    """Raised when monitoring/logging operations fail."""
    pass
