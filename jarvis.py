import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
change = 1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said {query}")
    
    except Exception as e:
        print("Say that again please... I didn't Recongnized it\n")
        return 'None'

    return query

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("Good Morning,Sir!")

    elif(hour>12 and hour<18):
        speak("Good AfterNoon,sir")

    else:
        speak("Good Evening,sir")
    
    speak("I am Jarvis. Please tell me how may I help you")

def sendMail(to , content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login('rupeshschavan12345@gmail.com' , 'Pubgmania@1')
    server.sendmail('rupeshschavan12345@gmail.com' , to , content)
    server.close()


wishMe()
while True:
    query = takeCommand().lower()

    if 'open youtube' in query:
        webbrowser.register('chrome' , None)
        speak("opening youtube")
        webbrowser.open("https://youtube.com")

    elif 'open instagram' in query:
        webbrowser.register('chrome' , None)
        speak("opening instagram")
        webbrowser.open("http://instgram.com")
    
    elif 'open facebook' in query:
        webbrowser.register('chrome' , None)
        speak("opening facebook")
        webbrowser.open('https://facebook.com')
    
    elif 'open stackover flow' in query:
        webbrowser.register('chrome' , None)
        speak("opening stack overflow")
        webbrowser.open('https://stackoverflow.com')

    elif 'change your voice' in query:
        voices = engine.getProperty('voices')
        if(change == 1):
            engine.setProperty('voice' , voices[1].id)
            change = 0
            speak("I am Friday. Please tell me how may I help you")
        else:
            engine.setProperty('voice' , voices[0].id)
            change = 1
            speak("I am Jarvis. Please tell me how may I help you")
    
    elif 'wikipedia' in query:
        speak('Searching on Wikipedia...')
        query = query.replace("wikipedia" ,"")
        result = wikipedia.summary(query , 2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    
    elif 'open code' in query:
        codedir = "C:\\Users\\R R\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening Code")
        os.startfile(codedir)
    
    elif 'send a mail' in query:
        email = {
            "RR" : 'rrindustries1@gmail.com',
            'Rishikesh' : 'rushikeshschavan400@gmail.com',
            "Rupesh" : 'musicdhindi@gmail.com'
        }

        speak("To whom do you want to send mail")
        to = takeCommand()
        try:
            if to in email:
                speak("What do I say ?")
                content = takeCommand()
                sendMail(email.get(to) , content)
                speak("Mail Sent Sucessfully")
            
            else:
                speak("Sorry Mail Not Found")

        except Exception as e:
            print(e)
            speak("Some error Occured")

    elif 'shutdown' in query:
        speak("Shuting down")
        os.system('shutdown /s /t 1')