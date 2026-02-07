import sounddevice as sd
from scipy.io.wavfile import write

FS = 44100
DURATION = 5

def record_audio(filename="audio.wav", duration=DURATION):
    print("Gravando...")
    audio = sd.rec(int(duration * FS), samplerate=FS, channels=1)
    sd.wait()
    write(filename, FS, audio)
    print("Áudio salvo em", filename)
    return filename
