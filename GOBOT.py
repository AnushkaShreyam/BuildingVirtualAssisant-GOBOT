
import speech_recognition as speech
import pyjokes
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#using default version of voice (male voice) :
#You can change this voice to a female voice by using
#this code:
#engine.setProperty('voice', voices[0].id)

engine.say('Hello Sunshine ')
engine.say('Myself Go-Bot')
engine.say('Any command?')
engine.runAndWait()

def communicate(txt):

    engine.say(txt)
    engine.runAndWait()
def commanding():
    try :
        with speech.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            #If you want to only print command
            # when you say go-bot in your txt, here is one line code
            #if 'Go-Bot' in command:
            print(command)
            communicate(command)
    except:
        pass
    return command

def gobot_run():
    command = commanding()

    print(command )
    if 'play' in command:
        song = command.replace('play', '')
        communicate('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command :
        time = datetime.datetime.now().strftime('%H : %M')
        #time = datetime.datetime.now().strftime('%I : %M %p')
        #Output of time is in AM/PM form
        communicate('Current time : ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        communicate(info)

    elif 'are you single' in command:
        communicate('I am in a relationship with wifi')
    elif 'joke' in command:
        communicate(pyjokes.get_joke())
    else:
        communicate('Please say the command again.')


while True :
    gobot_run()
