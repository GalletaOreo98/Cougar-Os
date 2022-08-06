import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

"""VOICE"""
voices = engine.getProperty('voices')
print(voices[20])
engine.setProperty('voice', voices[20].id)

"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 165)


"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

engine.say("Hola a")
engine.runAndWait()

listener = sr.Recognizer()
name = "cat"


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()

            if name in rec:
                print(rec)
    except:
        rec = ""
    return rec


def run():
    rec2 = listen()
    if "play" in rec2:
        music = rec2.replace("play", "")
        print(music)
    else:
        print(rec2 + "Again pls")


while True:
    run()