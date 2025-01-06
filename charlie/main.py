import pyttsx3
import speech_recognition as sr
import webview
from engine.features import *
from engine.command import *
import mysql.connector as mysql
import tabulate
import json

mydb = mysql.connect(host='localhost',user='root',password='Aadi2007',database='aadi')

if mydb.is_connected():
    print('done!!!')
    
mycursor = mydb.cursor()

# Function to speak text using pyttsx3
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

# Function to take command from microphone input
def takecommand():
    global window
    recog = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            # Send message to JavaScript to indicate listening
            window.evaluate_js("DisplayMassage('Listening...')")
            
            recog.pause_threshold = 1
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source, 5, 8)

    
        print("recognizing...")
        window.evaluate_js("DisplayMassage('Recognizing...')")
        query = recog.recognize_google(audio, language='en-in')
        
    except Exception as e:
        window.evaluate_js("DisplayMassage('Say that again please...')")
        speak("Say that again please...")
        allCommand()

    return query

def allCommand(message=1):
    
    if message == 1:
        query = takecommand()
        window.evaluate_js(f"DisplayMassage('You said: {query}')")
        print(query)
        
    else:
        query = message
        print(query)
        window.evaluate_js(f"DisplayMassage('You said: {query}')")
        
    try:    
        if 'goodbye' in query or 'thank you' in query or 'exit' in query or 'bye' in query:
            print('Thank you Sir, Have a nice day')
            window.evaluate_js("DisplayMassage('Thank you Sir, Have a nice day.')")
            speak("Thank you Sir, Have a nice day.")
            window.evaluate_js("Showhood()")
        else:
            a= generate_sql(query,mycursor)
            print(a)
            window.evaluate_js(f"DisplayMassage('{json.dumps(a)}')")
            speak(a)
            allCommand()
        
             
    except Exception as e:
        print(e)
        window.evaluate_js("DisplayMassage('Sorry, I am not able to understand what you are saying!...')")
        speak("Sorry, I am not able to understand what you are saying!!.... please say again")
        allCommand()


playAssistantSound()
# Create the webview window and expose Python functions to JavaScript
window = webview.create_window('Simple JS-Python Interaction', 'web/index.html', width=900, height=800)
window.expose(allCommand,playAssistantSound)

# Start the webview
webview.start()



