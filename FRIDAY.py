import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyjokes
import sys  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("this is Friday at your service.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        print(e)    
        print("Say that again please...")
        speak("say that again please")   
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maddy.updh20@gmail.com', 'MADDY.UPADHYE')
    server.sendmail('madhuraupadhye20@gmail.com', to, content)
    server.close()

    


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia'in query:
            speak('Searching Wikipedia....Please Wait')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'how are you'in query:
            speak("i am good how are you")
            print("Listening...")
            
    

        elif 'open youtube' in query:
            speak('opening youtube....Please Wait')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google....Please Wait')
            webbrowser.open("google.com")  


        elif 'open netflix' in query:
            speak('opening netflix....Please Wait')
            webbrowser.open("netflix.com") 


        elif 'play music' in query:
            speak('playing music....Please Wait')
            music_dir = 'C:\\Users\\91942\\Desktop\\FRIDAY\\music'
            songs = os.listdir(music_dir)
            rd= random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
       

        elif 'open code' in query:
            codePath = "C:\\Users\\91942\\Desktop\\Microsoft VS Code"
            os.startfile(codePath)
        
        elif 'open whatsapp'in query:
            webbrowser.open("whatsapp.com")

       
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

    
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")


        elif 'tell me a joke' in query:
            jokes = pyjokes.get_joke()
            speak(jokes)

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            speak(" setting alarm....")  
            print("setting alarm.....")          
            if nn==20:
                music_dir ='C:\\Users\\91942\\Desktop\\FRIDAY\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'email to madhura' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "madhuraupadhye20@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend I am not able to send this email")  
        elif "how are you today" in query:
             speak ("i am good.")
        

        elif "you can sleep" in query:
            speak ("i hope i was helpful,thanks for using me, have a great day!")
            sys.exit()
        
        
        speak("what else can i do for you")