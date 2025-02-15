# model_server
WIP

Server for: [Chrome Assistant](https://github.com/DanielSawczuk/chrome-assistant)

Uses [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) for TTS

```
export CORS_ASSISTANT_EXTENSION=<>
fastapi dev main.py
```

### Set up pre-coomit hook for clang-format and black formatting
```
ln hooks/format.hook .git/hooks/pre-commit
```