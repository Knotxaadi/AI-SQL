import pyttsx3
import speech_recognition as sr
import pyaudio

def speak(text):
        engine = pyttsx3.init('sapi5')
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 140)
        engine.say(text)
        engine.runAndWait()


def takecommand():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold=1
        recog.adjust_for_ambient_noise(source)

        audio = recog.listen(source, 10, 6)

    try:
        print("recognizing...")
        query = recog.recognize_google(audio , language='en-in')
        print(f'User said: {query}')

    except Exception as e:
        return "e"

    return query.lower()


text = takecommand()

speak(text)