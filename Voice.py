import pyttsx3
# import pygame.mixer as mixer

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice",voices[1].id)

# mixer.init()

def speak(text):
    voice_engine.say(text)
    # voice_engine.save_to_file(text,"audio.mp3")
    voice_engine.runAndWait()
    # mixer.music.load("audio.mp3")
    # mixer.music.play()
# def stop():
    # mixer.music.stop()