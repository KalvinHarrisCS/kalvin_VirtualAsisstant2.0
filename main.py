import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha



# imports voices for the engine/AI
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id, )


# function for tech bot AI to speak
def talk(text):
    engine.say(text)
    engine.runAndWait()


# defined my function for the mircrophone so it can listen to the user
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening to you.')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tech bot' in command:
                command = command.replace('tech bot', '')
                print(command)
    except:
        pass
    return command


# make a if or else statments for Tek Bot to be able to tell time, play music only on youtube, also google maps api and open your mail.
def run_techbot():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Hello Integrity User the Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'you single' in command:
        talk('Im dating your router.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # email and and search the web
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")

    elif 'email' in command:
        webbrowser.open_new_tab("outlook.com")
        talk("Here is your email. I cannot log in for you")

    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)

    elif 'hello' in command:
        talk("Hi i am tech bot your personal AI. How can i help you Integrity User ")

    elif 'ask' in command:
        talk('I can answer to computational and geographical questions  and what question do you want to ask now')
        question = command()
        app_id = "L6Q2V7-TQPQYQYLUR "
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)





    # """use switch command at the top of elif possibly???

    # switch(command){
    #   case 'hello': talk("Hi i am tech your personal AI. How can i help you Kay Bee");
    #        break;
    #
    #
    #
    #
    # }
    #
    #
    #
    #

    # google maps API. i should need  some sort of  request to send all types of http request.

    # ecapture images from user possibly might need json too store and exchange data within a data base possibly sql?

    # wolf api for computation and geographical analysis

    # use subprocess to be able to make your computer restart
    else:
        talk('Please say that command again.')


while True:
    run_techbot()

# look at my depedeancy using pip to manage what my dependacy is. he could not run on his machine cause he would have to import the same dependacy so we have same enviroment.
# try to find file to set up package.json its in my js project that package contains a list of dependacy in a dev enviroment. It states what dependacys
# how to define a set of dependacys that i am using to run this program. create a scripit that looks at a file that tells me what dependacy is need for other  programmers to use
