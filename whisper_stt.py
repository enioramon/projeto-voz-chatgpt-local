from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")

def transcribe(audio_path, language="pt"):
    segments, info = model.transcribe(audio_path, language=language)
    text = ""
    for segment in segments:
        text += segment.text
    return text.strip()