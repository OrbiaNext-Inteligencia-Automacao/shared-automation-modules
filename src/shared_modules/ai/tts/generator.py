"""TTS generator with multi-provider support."""

from typing import Optional, Dict, Any
import logging
from .base import BaseTTSProvider

logger = logging.getLogger(__name__)


class TTSGenerator:
    """Unified TTS generator supporting multiple providers."""
    
    PROVIDERS = {}  # Will be populated as providers are implemented
    
    def __init__(self, provider: str = "coqui", **kwargs):
        """
        Initialize TTS generator.
        
        Args:
            provider: TTS provider ('coqui', 'google', 'azure', 'openai')
            **kwargs: Provider-specific configuration
        """
        self.provider_name = provider
        self._provider = self._create_provider(provider, **kwargs)
    
    def _create_provider(self, provider: str, **kwargs) -> BaseTTSProvider:
        """Create provider instance."""
        if provider == "coqui":
            try:
                from .coqui import CoquiTTSProvider
                return CoquiTTSProvider(**kwargs)
            except ImportError:
                logger.error("Coqui TTS not installed. Install with: pip install TTS")
                raise
        
        elif provider == "google":
            try:
                from .google import GoogleTTSProvider
                return GoogleTTSProvider(**kwargs)
            except ImportError:
                logger.error("Google TTS not installed. Install with: pip install google-cloud-texttospeech")
                raise
        
        elif provider == "openai":
            try:
                from .openai_tts import OpenAITTSProvider
                return OpenAITTSProvider(**kwargs)
            except ImportError:
                logger.error("OpenAI not installed. Install with: pip install openai")
                raise
        
        else:
            raise ValueError(f"Unsupported TTS provider: {provider}")
    
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
            text: Text to convert
            voice: Voice ID
            output_path: Output file path
            **kwargs: Provider-specific options
            
        Returns:
            Path to audio file
        """
        return self._provider.generate(text, voice, output_path, **kwargs)
    
    def list_voices(self) -> Dict[str, Any]:
        """List available voices for current provider."""
        return self._provider.list_voices()
    
    def estimate_duration(self, text: str) -> float:
        """Estimate audio duration."""
        return self._provider.estimate_duration(text)
