import pyaudio
from vosk import Model, KaldiRecognizer

recognizer = {"hi":KaldiRecognizer(Model(r"models\\hi"), 16000),"en":KaldiRecognizer(Model(r"models\\en"), 16000)}

audio = pyaudio.PyAudio()
mic = audio.open(16000,1,pyaudio.paInt16,True,frames_per_buffer=8192)
mic.start_stream()


def listen(lang="hi"):
    audio = mic.read(4096, exception_on_overflow=False)

    if recognizer[lang].AcceptWaveform(audio):
        text = recognizer[lang].Result()
        yield text[14:-3]
