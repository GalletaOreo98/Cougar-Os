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


engine.say("Hola, me has iniciado.")
engine.runAndWait()


listener = sr.Recognizer()

name = "puma"


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
        rec=""
    return rec


is_running = 1


def run():
    rec2 = listen()
    if "play" in rec2:
        music = rec2.replace("play", "")
        print(music)
        engine.say("Play" + music)
        engine.runAndWait()
    elif "stop" in rec2:
        global is_running
        is_running = 0
        engine.say("Hasta pronto! deteniendo servicio")
        engine.runAndWait()
    else:
        engine.say("Lo siento, no te he entendido")
        engine.runAndWait()


while is_running:
    run()

