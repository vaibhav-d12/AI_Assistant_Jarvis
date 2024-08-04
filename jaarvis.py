#here all import statement is use to apply external module in a code
import time #it performs all the functionality with respect to time...
import subprocess
import wikipedia #wikipedia module is use to open wikipedia on the internet
import pyttsx3 #this library is use to convert text to speech in python               
import speech_recognition as sr
import os #this module helps in way of using operating system-dependent functionality.
import datetime #this module is use to represent the information about the present date 
import webbrowser #helps in opening of any web browser
import smtplib #this module is used for sending email to an internet #simple mail transfer protocol
import requests #this module allows you to send http requests and returns a respnse object with all respanse data(ex- status,news,etc)
from ecapture import ecapture as ec #this module is used for the clicking of the photos
engine=pyttsx3.init("sapi5")#sapi5 (speech application programming interface) is microsoft platform which provides voices which was early added in system 
#init function is use to initialize the state of object
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id) #0 is for male voice whereas 1 is for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    date = int(datetime.datetime.now().hour)
    if date>=0 and date<12:
        speak("Good Morning")
    elif date>=12 and date<18:
        speak("Good afternoon")
    else :
        speak("Good Evening")
    speak(" I am Jarvis Sir. Please tell me how may I help you")#jarvis will say this line whenever we run the program   

def takeCommand():  #it take users input using microphone and gives output as a string
    r=sr.Recognizer()#here the jarvis will recognize the words spoken by the user
    with sr.Microphone() as source:#microphone will listen the voice of the user and it will recognize the words
        print("Listening.....")
        r.dynamic_energy_adjustment_damping = 0.15
        r.pause_threshold=0.8# seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold=150# minimum audio energy to consider for recording

        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said....: {query}\n")
        speak("sure sir")
    except Exception as e:
        print("say that again please....")
        return "none"
    return query        
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("Vaibhav.123.sharmaa@gmail.com","")
    server.sendmail("Vaibhav.123,sharmaa@gmail.com",to,content)
    server.close()

if __name__  == "__main__":
    wishMe()
    query=takeCommand().lower()   
    if"wikipedia" in query:
        speak("searching wikipedia....")
        query = query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=2)
        speak("according to wikipedia ")
        print(results)
        speak(results) 
    
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")    
    elif "play music" in query:
        musi="C:\\musi\\favourites"
        songs =os.listdir(musi)
        print(songs)   
        os.startfile(os.path.join(musi,songs[0]))
    elif"the time" in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strtime)
        speak(f"sir the time is{strtime}")    
    elif "email to vaibhav" in query:
        try:
            speak("what should i say") 
            content= takeCommand()
            to = "Vaibhav.123.sharmaa@gmail.com"
            sendEmail(to,content)
            speak("email has been sent!...")
        except Exception as e:
            print(e)
            speak("I am sorry sir.I am not able to sent email")       
    
    elif "camera" in query or "take a photo" in query: #the jarvis will automatically click the picture of the user
        ec.capture(0, "Jarvis Camera ", "img.jpg")
    elif "how are you" in query:
        speak("i am fine sir. glad to meet you")
        speak("how are you, sir?")
    elif"what i am" in query:
        speak("if you talk, definitely you are human")
    elif "log of computer" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
    elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f') 

