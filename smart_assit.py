#importing all necessary packages
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

#setting the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#selecting the male/female version of the narrator
engine.setProperty('voice', voices[0].id)

#speak function to narrate a given string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#wish function. To be initiated when when the program starts
def wish():
    AP = ""
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        AP = "AM"
        speak("Good Morning,sir")
    elif hour>=12 and hour<18:
        hour=hour-12
        AP = "PM"
        speak("Good afternoon,sir")
    else:
        hour=hour-12
        AP = "PM"
        speak("Good evening,sir")
    s = "Now the time is"+str(hour)+str(minute)+AP
    speak(s)
    speak("If you need anything, please call me by my name,Jarvis")

#listener function to call the Assistant
def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.pause_threshold = 0.5
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        #print("Can't get it sir. Please repeat")
        return "None"
    return query

#command function. To be initiated when the Assistant is called
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening...")        
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        #print("User said", query)
    except Exception as e:
        print("Say that again, please")
        return "None"
    return query

#MAIN Function
if __name__ == "__main__": 
    wish()  #wish the user with the time
    while True:
        query = listener().lower()
        if query=="jarvis":
            while True:
                speak("Yes sir")
                ask = command().lower()
                if "open" in ask:
                    ask=ask.replace("open","")
                    webbrowser.open(ask)
                    
                    speak("Do you need anything else,sir?")
                    ask=command().lower()
                    if (ask=="yes" or ask=="yeah" or ask=="hmmm"):
                        continue
                    else:
                        print("Call me again if you need anything")
                        break
                
            
                
                    
