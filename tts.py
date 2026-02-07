from gtts import gTTS

def speak(text, filename="response.mp3", lang="pt"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
