from typing import Annotated
from fastapi import FastAPI, Response, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import tts
import os

app = FastAPI()

origins = [os.getenv("CORS_ASSISTANT_EXTENSION", "")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


class TTSRequest(BaseModel):
    text: Annotated[str, Body(max_length=2048)]


@app.post("/tts")
def text_to_wav(request: TTSRequest):
    try:
        audio = tts.tts(request.text)
        if not audio:
            raise HTTPException(status_code=500, detail="TTS conversion failed")
        return Response(content=audio, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unknown error")
