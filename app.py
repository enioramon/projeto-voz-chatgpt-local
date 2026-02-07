from recorder import record_audio
from whisper_stt import transcribe
from chatgpt_api import ask_chatgpt
from tts import speak
import os

if __name__ == "__main__":
    audio_file = record_audio("input.wav", duration=5)

    print("Transcrevendo...")
    text = transcribe(audio_file)
    print("Você disse:", text)

    print("Enviando ao ChatGPT...")
    response = ask_chatgpt(text)
    print("ChatGPT:", response)

    print("Gerando voz...")
    voice_file = speak(response)

    print("Resposta em áudio gerada:", voice_file)
    os.system(f"start {voice_file}" if os.name == "nt" else f"xdg-open {voice_file}")
