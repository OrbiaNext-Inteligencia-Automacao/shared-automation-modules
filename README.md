# Shared Automation Modules

Biblioteca compartilhada de módulos para pipelines de automação de vídeo, TTS, LLM e processamento de mídia.

## 🎯 Objetivo

Centralizar funcionalidades comuns usadas em múltiplos projetos de automação:
- `youtube-automation-pipeline`
- `go-video-generator`
- Futuros projetos de automação

## 📦 Módulos Disponíveis

### Storage
Abstração unificada para armazenamento (S3, MinIO, Local)

```python
from shared_modules.storage import UnifiedStorageClient

storage = UnifiedStorageClient(backend="s3", bucket="my-bucket")
storage.upload_file("video.mp4", "output/video.mp4")
```

### AI Services

#### TTS (Text-to-Speech)
```python
from shared_modules.ai.tts import TTSGenerator

tts = TTSGenerator(provider="coqui")
audio = tts.generate("Hello world", voice="male_voice")
```

#### LLM
```python
from shared_modules.ai.llm import LLMClient

llm = LLMClient(provider="openai")
response = llm.generate_text("Write a video script about AI")
```

### Video Processing
```python
from shared_modules.video import VideoRenderer

renderer = VideoRenderer(gpu_acceleration=True)
renderer.compose_video(
    frames=frame_list,
    audio="narration.mp3",
    output="final.mp4"
)
```

### Monitoring
```python
from shared_modules.monitoring import MetricsCollector, StructuredLogger

metrics = MetricsCollector()
logger = StructuredLogger()

with metrics.track_duration("video_render"):
    logger.info("Starting render", video_id="123")
    # ... render code
```

## 🚀 Instalação

### Básica
```bash
pip install -e .
```

### Com extras
```bash
# TTS support
pip install -e ".[tts]"

# Video processing
pip install -e ".[video]"

# ML/AI features
pip install -e ".[ml]"

# Desenvolvimento
pip install -e ".[dev]"
```

## 🏗️ Estrutura

```
src/
├── shared_modules/
│   ├── storage/          # S3, MinIO, Local storage
│   ├── ai/
│   │   ├── tts/          # Text-to-Speech providers
│   │   ├── llm/          # LLM integrations
│   │   └── vision/       # Image generation
│   ├── video/            # Video rendering & processing
│   ├── monitoring/       # Metrics & logging
│   ├── config/           # Configuration management
│   └── utils/            # Helper functions
```

## 🧪 Testes

```bash
# Run all tests
pytest

# With coverage
pytest --cov=shared_modules --cov-report=html

# Specific module
pytest tests/storage/
```

## 📖 Documentação

Veja `docs/` para documentação detalhada de cada módulo.

## 🔄 Versionamento

Seguimos [Semantic Versioning](https://semver.org/):
- `0.1.0` - Versão inicial alpha
- `0.2.0` - Adição de novos módulos
- `1.0.0` - Release estável

## 🤝 Contribuindo

1. Crie branch: `git checkout -b feature/new-module`
2. Implemente com testes
3. Execute linting: `black . && flake8`
4. Commit: `git commit -m "Add new module"`
5. Push e crie PR

## 📄 Licença

MIT
