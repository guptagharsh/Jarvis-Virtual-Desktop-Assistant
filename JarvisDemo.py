import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import playsound
import random
import pyjokes
from pynput.keyboard import Key, Controller
import pyautogui as pg
import time
import pywhatkit as kit
import subprocess
from requests import get
import calendar
from config import apikey
import openai
from click import prompt

chatStr = ""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User said: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    # with open(f"Openai/prompt- {random.randint(1, 21212145)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text12)

def ai(prompt):
    openai.api_key = apikey
    text12 = f"OpenAI response for prompt: {prompt}\n ********************\n\n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    # print(response["choices"][0]["text"])
    text12 += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
      os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 21212145)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
      f.write(text12)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hhhh = playsound.playsound("jarvis1.mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir! I am Jarvis! Please tell me how may I help you")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir! I am Jarvis! Please tell me how may I help you")

    else:
        speak("Good Evening Sir! I am Jarvis! Please tell me how may I help you")
    # speak("I am jarvis. Please tell me how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 20000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry! Say that again please...")
        speak("Sorry, I didn't understand")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search with youtube' in query or 'search on youtube' in query:
            speak("What you want to search")
            print("Speak")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=20000
            with sr.Microphone() as source:
                audio=r.listen(source)

                try:
                    text=r.recognize_google(audio)
                    url='https://www.youtube.com/results?search_query='
                    search_url=url+text
                    webbrowser.open(search_url)
                    speak("ok Sir")
                except:
                    speak("Please say clearly")
                    print("Can't Recognize")

        elif 'search on google' in query:
            speak("What you want to search")
            print("Speak")
            sr.Microphone(device_index=2)
            r=sr.Recognizer()
            r.energy_threshold=20000
            with sr.Microphone() as source:
                audio=r.listen(source)
                
                try:
                    text=r.recognize_google(audio)
                    url='https://www.google.co.in/search?q='
                    search_url=url+text
                    webbrowser.open(search_url)
                    speak("ok Sir")
                except:
                    speak("Please say clearly")
                    print("Can't Recognize")

        elif 'using artificial intelligence'.lower() in query.lower():
            speak("Sure Sir")
            ai(prompt=query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening. youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening. google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening. stackoverflow")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening. facebook")

        elif 'hey jarvis' in query:
            speak("hey there! how may i help")

        elif 'wake up' in query or 'wakeup' in query:
            ch = ["0", "1"]
            cho = random.choice(ch)
            if cho=="0":
                wakePath = playsound.playsound("yawning sound.mp3")
                speak("Hey there! how can i help?")
                
            elif cho=="1":
                list1 = "Hi Sir I'm awake! how can i help?"
                speak(list1)

        elif 'hello' in query:
            lst = ["Hello sir! how may i help", "Hi sir! good to see you again. please tell me how may i help"]
            # speak("Hello Sir! How may i Help")
            choice = random.choice(lst)
            speak(choice)

        elif 'how are you' in query or 'how r u ' in query:
            lst1 = ["i'm fine sir! and how about you", "thank you so much for asking, i'm fine sir"]
            choice1 = random.choice(lst1)
            speak(choice1)

        elif 'i am also good' in query or 'i am fine' in query or 'i am good' in query or 'i am also fit and fine' in query or 'i am fit and fine' in query:
            speak("well that's nice! tell me sir how may i help")

        elif'i am not good' in query or 'i am not well' in query or 'i am sad' in query or 'i am not feel good' in query:
            speak("Sorry sir if i upset you! please tell me what can i do for you")

        elif 'who are you' in query or 'who r u' in query:
            speak("Sir I am your personal assistant")

        elif 'why are you' in query:
            speak("Sir I am here, for solving your day to day problems")

        elif 'who develop this software' in query or 'who made you' in query or 'who make you' in query or 'who developed you' in query or 'who develop you' in query:
            speak("Harsh Developed this software")

        elif 'who developed this software' in query:
            speak("Harsh Developed this software")

        elif 'who created this software' in query:
            speak("Harsh created this software")

        elif 'who create this software' in query:
            speak("Harsh created this software")

        elif 'what can you do jarvis' in query:
            speak("i can do everything for you sir, i am able to search anything from wikipedia, i can open any appliation and software for you sir, i can search anything on google, Ask me anything sir")

        elif 'whatsapp' in query or 'whats up' in query:
            speak("in your service, sir")

        elif 'tell me a joke' in query or 'tell me any joke' in query:
            joke  = pyjokes.get_joke()
            speak(joke) 

        elif 'nice' in query:
            speak("Oh! thank you sir")

        elif 'start' in query:
            pg.hotkey('winleft')
            speak("ok")

        elif 'open it' in query:
            speak("ok")
            pg.hotkey('Enter')

        elif 'maximize' in query:
            speak("ok")
            pg.hotkey('winleft','up')

        elif 'minimise' in query:
            speak("ok")
            pg.hotkey('winleft','down')

        elif 'close it' in query or 'closeit' in query or 'closet' in query:
            speak("sure sir")
            pg.hotkey('alt','F4')

        elif 'system search' in query:
            speak("What you want to search")
            print("Speak")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=20000
            with sr.Microphone() as source:
                audio=r.listen(source)

                try:
                    text=r.recognize_google(audio)
                    speak("ok sir")
                    pg.hotkey('winleft','q')
                    keyboard = Controller()

                    time.sleep(2)

                    for char in text:
                        keyboard.press(char)
                        keyboard.release(char)
                        time.sleep(0.12)
                except:
                    speak("Please say clearly")
                    print("Can't Recognize")

        elif 'play songs on youtube' in query:
            speak("Sure sir")
            ch1 = ["0", "1"]
            cho1 = random.choice(ch1)
            if cho1=="0":
                kit.playonyt("build to last")
                
            elif cho1=="1":
                kit.playonyt("gun double")

        elif 'recent' in query or 'task view' in query:
            speak("sure sir")
            pg.hotkey('winleft','Tab')

        elif 'hide this view' in query or 'close the view' in query or 'close task view' in query:
            speak("ok")
            pg.hotkey('Enter')

        elif 'run and type' in query or 'open run command and type' in query or 'open run' in query:
            speak("What you want to type")
            print("Speak")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=20000
            with sr.Microphone() as source:
                audio=r.listen(source)

                try:
                    text=r.recognize_google(audio)
                    speak("ok sir")
                    pg.hotkey('winleft','r')
                    keyboard = Controller()

                    time.sleep(2)

                    for char in text:
                        keyboard.press(char)
                        keyboard.release(char)
                        time.sleep(0.12)
                except:
                    speak("Please say clearly")
                    print("Can't Recognize")

        # elif 'translate' in query:
        #     print("Speak")
        #     sr.Microphone(device_index=1)
        #     r=sr.Recognizer()
        #     r.energy_threshold=20000
        #     with sr.Microphone() as source:
        #         audio=r.listen(source)
                
        #         try:
        #             text=r.recognize_google(audio)
        #             speak("ok sir")
        #             sentence=text

        #             translator=Translator()

        #             translated_sentence=translator.translate(sentence,src='en',dest='hi')

        #             print(translated_sentence.text)

        #             speak(translated_sentence)

        #         except:
        #             speak("please say clearly")
        #             print("can't Recognize")

        elif 'selection' in query:
            pg.hotkey('Tab')

        elif 'next' in query:
            pg.hotkey('Tab')

        elif 'right' in query:
            pg.hotkey('right')

        elif 'left' in query:
            pg.hotkey('left')

        elif 'up' in query:
            pg.hotkey('up')

        elif 'down' in query:
            pg.hotkey('down')

        elif 'top' in query :
            pg.hotkey('home')

        elif 'bottom' in query:
            pg.hotkey('end')

        elif 'right click on windows button' in query or 'open quick link menu' in query:
            speak("ok")
            pg.hotkey('winleft','x')

        elif 'open notification panel' in query or 'open action centre' in query:
            speak("ok")
            pg.hotkey('winleft','a')

        elif 'hide this notification panel' in query or 'hide this action centre'in query or 'hide action centre' in query:
            speak("ok")
            pg.hotkey('winleft','a')

        elif 'desktop' in query or 'main screen' in query or 'show me desktop' in query or 'show desktop' in query:
            speak("ok")
            pg.hotkey('winleft','d')

        elif 'rename' in query:
            speak("ok")
            pg.hotkey('F2')

        elif 'delete' in query:
            speak("ok")
            pg.hotkey('delete')

        elif 'switch window' in query:
            speak("Sure sir")
            pg.hotkey('alt','tab')

        elif 'screenshot' in query:
            speak("Sure sir")
            pg.hotkey('winleft','PrtSc')

        elif 'open new tab' in query:
            speak("Sure Sir")
            pg.hotkey('ctrl','t')

        elif 'close this tab' in query or 'close current tab' in query:
            speak("Sure Sir")
            pg.hotkey('ctrl','w')

        elif 'reopen' in query or 're open' in query:
            speak("ok sir")
            pg.hotkey('ctrl','shift','t')

        elif 'backspace' in query:
            speak("ok sir")
            pg.hotkey('backspace')

        elif 'type' in query or 'edit' in query:
            speak("What you want to type")
            print("Speak")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=20000
            with sr.Microphone() as source:
                audio=r.listen(source)

                try:
                    text=r.recognize_google(audio)
                    speak("ok sir")
                    keyboard = Controller()

                    time.sleep(2)

                    for char in text:
                        keyboard.press(char)
                        keyboard.release(char)
                        time.sleep(0.12)
                except:
                    speak("Please say clearly")
                    print("Can't Recognize")

        elif 'create a new folder' in query:
            speak("Sure sir")
            pg.hotkey('ctrl','shift','n')
            
        elif 'click ok' in query:
            pg.hotkey('Enter')

        elif 'enter' in query:
            pg.hotkey('Enter')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Harsh Gupta\\Desktop\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        # elif 'open notepad' in query:
        #     speak("Opening. notepad")
        #     notePath = os.system('cmd /c "notepad"')

        elif 'open notepad' in query:
            speak("Opening. notepad")
            subprocess.Popen(['notepad.exe']) 

        elif 'camera' in query:
            speak("Opening. camera")
            camPath = os.system('cmd /c "explorer.exe shell:Appsfolder\\Microsoft.WindowsCamera_8wekyb3d8bbwe!App"')

        elif 'alarm' in query:
            speak("Opening. alarm")
            alarmPath = os.system('cmd /c "explorer.exe shell:Appsfolder\\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"')

        # elif 'open paint' in query or 'open ms paint' in query:
        #     speak("Opening. MS Paint")
        #     paintPath = os.system('cmd /c "mspaint"')   

        # "Subprocess module" is used because in os.system there's a slight issue here. The os.system() function returns the exit status of the command executed, not the path of the opened application
        
        elif 'open paint' in query or 'open ms paint' in query or 'open microsoft paint' in query:
            speak("Opening. MS paint")
            subprocess.Popen(['mspaint.exe'])  
            
        elif 'open wordpad' in query:
            wordpadPath = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordpadPath)
            speak("Opening. Wordpad")

        elif 'documents' in query:
            docPath = "C:\\Users\\Harsh GUpta\\Documents"
            os.startfile(docPath)
            speak("Opening. Documents")

        elif 'open calculator' in query:
            calcPath = "C:\\WINDOWS\\system32\\calc.exe"
            os.startfile(calcPath)
            speak("Opening. Calculator")

        elif 'open one drive' in query or 'open onedrive' in query:
            onePath = "C:\\Users\\Harsh Gupta\\OneDrive"
            os.startfile(onePath)
            speak("Opening. One Drive")

        elif 'on screen keyboard' in query or 'open screen keyboard' in query:
            scrkPath = "C:\\WINDOWS\\system32\\osk.exe"
            os.startfile(scrkPath)
            speak("Opening. Screen keyboard")

        elif 'open media player' in query or 'open windows media player' in query:
            wmpPath = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
            os.startfile(wmpPath)
            speak("Opening. Windows media player")

        elif 'open task manager' in query:
            taskPath = "C:\\WINDOWS\\system32\\Taskmgr.exe"
            os.startfile(taskPath)
            speak("opening. task manager")

        elif 'open c drive' in query:
            cPath = "C:\\"
            os.startfile(cPath)
            speak("Opening. C drive")

        elif 'downloads' in query:
            downlPath = "C:\\Users\\Harsh Gupta\\Downloads"
            os.startfile(downlPath)
            speak("Opening. Downloads")

        elif 'open pictures' in query:
            picturePath = "C:\\Users\\Harsh Gupta\\Pictures"
            os.startfile(picturePath)
            speak("Opening. Pictures")

        # elif 'help' in query:
        #     helpPath = "F:\\Harsh\\Jarvis\\Jarvis Commands\\Commands.txt"
        #     os.startfile(helpPath)
        #     speak("Opening. Help Center")

        elif 'open windows settings' in query:
            windowPath = "C:\\WINDOWS\\system32\\control.exe"
            os.startfile(windowPath)
            speak("Opening. Control Panel")

        elif 'open powerpoint' in query or 'open ms powerpoint' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(wordPath)
            speak("Opening. MS PowerPoint")

        elif 'open excel' in query or 'open ms excel' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(wordPath)
            speak("Opening. MS Excel")

        elif 'open word' in query or 'open ms word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)
            speak("Opening. MS Word")

        elif 'open this pc' in query or 'open windows explorer' in query:
            pcPath = "C:\\Windows\\explorer.exe"
            os.startfile(pcPath)
            speak("Opening. explorer")

        elif 'open vlc' in query or 'open vlc media player' in query:
            vlcPath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)
            speak("opening. VLC Media Player")

        elif 'prompt' in query or 'cmd' in query or 'open command prompt' in query:
            promptPath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(promptPath)
            speak("Opening Command Prompt")

        elif 'open edge' in query or 'open microsoft edge' in query:
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgePath)
            speak("Opening. Microsoft Edge")

        elif 'open explorer' in query:
            explorerPath = "C:\\Windows\\explorer.exe"
            os.startfile(explorerPath)
            speak("Opening. explorer")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print("Your ip address is "+ip)
            speak(f"Your ip address is {ip}")

        elif 'date' in query:
            def getDate():

                now = datetime.datetime.now()
                my_date = datetime.datetime.today()
                weekday = calendar.day_name[my_date.weekday()]
                monthNum = now.month
                dayNum = now.day

                month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decemeber']

                ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', 
                                  '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

                return 'Sir,  Today is '+weekday+' '+ month_names[monthNum - 1]+' the '+ ordinalNumbers[dayNum - 1]+'. '

            print (getDate())
            get_date = getDate()
            speak(get_date)

        elif 'open vs code' in query or 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'open browser' in query:
            bPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(bPath)

        elif 'thank you' in query:
            speak("Most welcome sir")

        elif 'exit' in query:
            speak("Ok sir, have a good day")
            os._exit(0)

        else:
            print("Chatting...")
