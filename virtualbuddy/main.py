import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'margo' in command:
                    command = command.replace('margo', '')
                    print(command)


    except:
        pass
    return command


def run_margo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        kit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The Current Time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'on a date' in command:
        talk("sorry, i have a headache") 
    

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    if 'search' in command:
        search = command.replace('search', '')
        talk('Searching' + search)
        kit.search(search)

    else:
        talk('Sorry i do not understand')

         
while True:
    run_margo()