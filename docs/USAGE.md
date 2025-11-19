# Usage Guide

## Installation

### From GitHub (Development)

```bash
# Basic installation
pip install git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git

# Specific version/tag
pip install git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git@v0.1.0

# With optional dependencies
pip install "shared-automation-modules[ai] @ git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git"
```

### In requirements.txt

```txt
# Pin to specific version
shared-automation-modules @ git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git@v0.1.0

# Latest from master
shared-automation-modules @ git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git

# With extras
shared-automation-modules[ai,video] @ git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git
```

### In pyproject.toml

```toml
[tool.poetry.dependencies]
shared-automation-modules = { git = "https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git", tag = "v0.1.0" }

# Or with extras
shared-automation-modules = { git = "https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git", tag = "v0.1.0", extras = ["ai", "video"] }
```

## Quick Start

### Storage

```python
from shared_modules import UnifiedStorageClient

# Local storage
storage = UnifiedStorageClient(backend="local", base_path="./data")
storage.upload_file("video.mp4", "videos/output.mp4")

# S3/MinIO storage
storage = UnifiedStorageClient(
    backend="s3",
    bucket="my-bucket",
    endpoint_url="http://localhost:9000",  # For MinIO
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

# Upload with metadata
storage.upload_file(
    "video.mp4",
    "videos/2024/output.mp4",
    metadata={"project": "youtube-automation", "version": "1.0"}
)

# Download
storage.download_file("videos/2024/output.mp4", "./downloads/video.mp4")

# List files
files = storage.list_objects(prefix="videos/2024/")
for file in files:
    print(file)

# Check if exists
if storage.object_exists("videos/output.mp4"):
    print("File exists!")

# Get URL
url = storage.get_url("videos/output.mp4", expires_in=3600)
print(f"Download URL: {url}")
```

### Configuration

```python
from shared_modules import ConfigManager

# Load from YAML
config = ConfigManager("config.yaml")

# Get values with dot notation
db_host = config.get("database.host", default="localhost")
api_key = config.get("api.key")  # Also checks API_KEY env var
port = config.get("server.port", default=8000)

# Set values
config.set("new.setting", "value")

# Merge configurations
config.merge({
    "feature_flags": {
        "enable_gpu": True,
        "max_workers": 4
    }
})

# Save to file
config.save("updated_config.yaml")
```

### AI Services (Coming Soon)

```python
from shared_modules.ai import TTSGenerator

# Initialize TTS
tts = TTSGenerator(provider="coqui")

# Generate speech
audio_path = tts.generate(
    text="Hello, this is a test.",
    voice="en-us-female",
    output_path="output.wav"
)

# List voices
voices = tts.list_voices()
```

## Advanced Usage

### Custom Storage Backend

```python
from shared_modules.storage import StorageBackend

class MyCustomStorage(StorageBackend):
    """Custom storage implementation."""
    
    def upload_file(self, file_path, destination, metadata=None):
        # Your implementation
        pass
    
    def download_file(self, source, destination):
        # Your implementation
        pass
    
    # Implement other abstract methods...

# Use it
storage = MyCustomStorage()
storage.upload_file("test.txt", "uploads/test.txt")
```

### Exception Handling

```python
from shared_modules.core import StorageError, ConfigurationError

try:
    storage.upload_file("missing.mp4", "uploads/video.mp4")
except StorageError as e:
    logger.error(f"Storage operation failed: {e}")

try:
    config = ConfigManager("missing_config.yaml")
except ConfigurationError as e:
    logger.error(f"Configuration error: {e}")
```

## Integration Examples

### YouTube Automation Pipeline

```python
# youtube_automation/main.py
from shared_modules import UnifiedStorageClient, ConfigManager
from shared_modules.ai import TTSGenerator

# Load config
config = ConfigManager("config.yaml")

# Setup storage
storage = UnifiedStorageClient(
    backend=config.get("storage.backend"),
    bucket=config.get("storage.bucket"),
    endpoint_url=config.get("storage.endpoint")
)

# Setup TTS
tts = TTSGenerator(provider=config.get("ai.tts_provider"))

# Use in pipeline
def process_video(script_text):
    # Generate narration
    audio_path = tts.generate(script_text, output_path="narration.mp3")
    
    # Upload to storage
    storage.upload_file(
        audio_path,
        f"projects/{project_id}/audio/narration.mp3",
        metadata={"project": project_id, "type": "narration"}
    )
```

### Go Video Generator

```python
# go_video_generator/storage.py
from shared_modules import UnifiedStorageClient, ConfigManager

config = ConfigManager()

# Use local storage for development
storage = UnifiedStorageClient(
    backend="local",
    base_path=config.get("output_dir", default="./output")
)

def save_video(video_data, filename):
    """Save generated video to storage."""
    storage.upload_file(
        video_data,
        f"videos/{filename}",
        metadata={"generator": "go-video-generator", "timestamp": str(datetime.now())}
    )
```

## Best Practices

### 1. Use Configuration for Storage Selection

```python
# config.yaml
storage:
  backend: s3  # or 'local', 'minio'
  bucket: my-videos
  endpoint: http://localhost:9000

# main.py
config = ConfigManager("config.yaml")
storage = UnifiedStorageClient(
    backend=config.get("storage.backend"),
    bucket=config.get("storage.bucket"),
    endpoint_url=config.get("storage.endpoint")
)
```

### 2. Use Environment Variables for Secrets

```bash
# .env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
OPENAI_API_KEY=your-api-key
```

```python
config = ConfigManager(load_env=True)
api_key = config.get("openai_api_key")  # Reads from OPENAI_API_KEY env var
```

### 3. Handle Errors Gracefully

```python
from shared_modules.core import StorageError

try:
    storage.upload_file("video.mp4", "output.mp4")
except StorageError as e:
    logger.error(f"Upload failed: {e}")
    # Fallback to local storage
    local_storage = UnifiedStorageClient(backend="local")
    local_storage.upload_file("video.mp4", "output.mp4")
```

### 4. Use Metadata for Organization

```python
storage.upload_file(
    "video.mp4",
    "output.mp4",
    metadata={
        "project": "youtube-automation",
        "video_id": "abc123",
        "created_at": datetime.now().isoformat(),
        "tags": "tutorial,python,automation"
    }
)
```

## Troubleshooting

### Import Errors

```python
# ❌ Wrong
from shared_modules.storage.unified_client import UnifiedStorageClient

# ✅ Correct
from shared_modules import UnifiedStorageClient
# or
from shared_modules.storage import UnifiedStorageClient
```

### Version Conflicts

```bash
# Check installed version
pip show shared-automation-modules

# Update to latest
pip install --upgrade git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git

# Force reinstall specific version
pip install --force-reinstall git+https://github.com/OrbiaNext-Inteligencia-Automacao/shared-automation-modules.git@v0.2.0
```

### Missing Dependencies

```bash
# If you get import errors for TTS
pip install "shared-automation-modules[ai]"

# If you get import errors for video processing
pip install "shared-automation-modules[video]"

# Install everything
pip install "shared-automation-modules[all]"
```

## More Examples

See the `/examples` directory (coming soon) for complete working examples.
