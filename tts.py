import io

import torch
from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code="a", device="cuda")


def tts(text):
    generator = pipeline(
        text,
        voice="af_heart",
        speed=1,
        split_pattern=r"\n+",
    )

    audio_samples = []

    for i, (_, _, audio) in enumerate(generator):
        audio_samples.append(torch.tensor(audio))

    audio_samples = torch.cat(audio_samples, dim=0)
    wav_io = io.BytesIO()
    sf.write(wav_io, audio_samples.numpy(), 24000, format="WAV")
    return wav_io.getvalue()
