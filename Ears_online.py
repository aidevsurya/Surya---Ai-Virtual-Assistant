import speech_recognition as sr

Recognizer = sr.Recognizer()

def listen(lang="hi"):
    with sr.Microphone() as mic:
        audio = Recognizer.listen(mic)
        try:
            text = Recognizer.recognize_google(audio,language=lang)
        except:
            text = ""
    return [text]
