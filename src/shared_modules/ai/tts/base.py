"""Base class for TTS providers."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class BaseTTSProvider(ABC):
    """Abstract base class for TTS providers."""
    
    def __init__(self, **kwargs):
        """Initialize TTS provider with configuration."""
        self.config = kwargs
        logger.info(f"Initialized {self.__class__.__name__}")
    
    @abstractmethod
    def generate(
        self,
        text: str,
        voice: Optional[str] = None,
        output_path: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Generate speech from text.
        
        Args:
            text: Text to convert to speech
            voice: Voice ID or name
            output_path: Path to save audio file
            **kwargs: Provider-specific parameters
            
        Returns:
            Path to generated audio file
        """
        pass
    
    @abstractmethod
    def list_voices(self) -> Dict[str, Any]:
        """
        List available voices.
        
        Returns:
            Dict of voice IDs to voice metadata
        """
        pass
    
    def estimate_duration(self, text: str, words_per_minute: int = 150) -> float:
        """
        Estimate audio duration from text.
        
        Args:
            text: Input text
            words_per_minute: Speaking rate
            
        Returns:
            Estimated duration in seconds
        """
        word_count = len(text.split())
        return (word_count / words_per_minute) * 60
