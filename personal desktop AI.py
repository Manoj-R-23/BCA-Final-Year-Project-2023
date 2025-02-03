import ctypes
import random
import subprocess
import pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import requests
import webbrowser as wb
import pywhatkit
import pyautogui
import sys
import time
import winshell as winshell
import wolframalpha as wolframalpha
from bs4 import BeautifulSoup
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

# TO MAKE JARVIS TO UNDERSTAND THE EXECUTIVE VOICE
def voice():
    engine.setProperty('voice', voices[1].id)
    print(voices[1].id)
    speak("female voice activated")


# TO MAKE JARVIS TO SPEAK
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# TO MAKE JARVIS TO WISH
def wish_time():
    global v_name
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    engine.runAndWait()
    v_name = "MANOJ"
    speak(f"IM {v_name} , HOW CAN I HELP YOU")

# TO SEARCH IN WEBSITE
def search(query):
    query = query.replace("search", "")
    qn = query
    wb.open(f"https://www.google.com/search?q={qn}")


#  TO PLAY MUSIC
def music():
    speak("playing music")
    # time.sleep(1)
    music_dir = "C:\\Users\\manoj\\Music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))

# TO CHANGE MUSIC
def change_music():
    speak("changing music")
    # time.sleep(1)
    music_dir = "C:\\Users\\manoj\\Music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))


def show_note():
    speak("Showing Notes")
    file = open("leo.txt", "r")
    print(file.read())
    speak(file.read(6))

# TO PLAY MOVIE
def movie():
    speak("playing a movie")
    # time.sleep(1)
    movie_dir = "C:\\Users\\manoj\\Videos"
    movies = os.listdir(movie_dir)
    rd = random.choice(movies)
    os.startfile(os.path.join(movie_dir, rd))

#  TO CHANGE MOVIE
def change_movie():
    speak("changing movie")
    # time.sleep(1)
    movie_dir = "C:\\Users\\manoj\\Videos"
    videos = os.listdir(movie_dir)
    rd = random.choice(videos)
    os.startfile(os.path.join(movie_dir, rd))

# TO FIND VARIOUS LOCATIONS
def location(query):
    query = query.replace("where is", "")
    query = query.replace("located", "")
    query = query.replace("locate", "")
    query = query.replace("location", "")
    location = query
    speak("User asked to Locate")
    speak(location)
    wb.open("https://www.google.com/maps/place/" + location + "")

#  TO OPEN WIKIPEDIA
def wiki():
    speak("what should i search on wikipedia`")
    qn = take_command().lower()
    res = wikipedia.summary(qn, sentences=2)
    print(res)
    speak(f"According to wikipedia{res}")

# TO OPEN WIKIPEDIA SUMMARY
def qn(query):
    qn = query.lower()
    res = wikipedia.summary(qn, sentences=1)
    engine.setProperty('rate', 150)
    print("wait for few seconds")
    print(res)
    speak(f"{res}")

# TO TAKE SCREEN SHOT
def screenshot():
    speak("PLEASE TELL ME THE NAME OF THE SCREENSHOT")
    try:
        name = take_command()
    except Exception as e:
        speak("I can't understand please type that")
        name = input("enter file name: ")
        print(e)
    speak("I'm taking screenshot")
    # time.sleep()
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("screenshot is taken")

# TO OPEN AND PROCESS GOOGLE
def google():
    speak("what should i search on google")
    qn = take_command().lower()
    wb.open(f"https://www.google.com/search?q={qn}")

# TO OPEN YOUTUBE
def youtube():
    speak("opening youtube")
    wb.open('www.youtube.com')

# TO PROCESS YOUTUBE
def play_yt(query):
    query = query.replace("youtube", "")
    query = query.replace("search", "")
    query = query.replace("play", "")
    query = query.replace("on", "")
    query = query.replace("in", "")
    query = query.replace("from", "")
    speak("playing" + query)
    pywhatkit.playonyt(query)

# TO OPEN FACEBOOK
def facebook():
    speak("opening facebook")
    wb.open('www.facebook.com')

# TO OPEN CLASSROOM
def classroom():
    speak("opening google classroom")
    wb.open('https://classroom.google.com/u/1/')

# TO OPEN GMAIL
def gmail():
    speak("opening Gmail")
    wb.open('https://mail.google.com/mail/u/1/#all')

# TO OPEN EDU_SERVE
def edu_serve():
    speak("opening edu_serve students portal")
    wb.open('https://studentportal.eduserve.app/home')

# TO OPEN GOOGLE DOCS
def docs():
    speak("opening google docs")
    wb.open('https://docs.google.com/document/u/0/?tgif=d')


# TO OPEN NOTEPAD
def notepad():
    speak("opening notepad")
    path = "C:\\Users\\manoj\\Downloads\\Windows Notepad Installer.exe"
    os.startfile(path)


# TO WRITE IN NOTEPAD
def write_note():
    speak("What should I write")
    note = take_command()
    try:
        pyautogui.hotkey('win+r')  # Open the Run dialog
        time.sleep(0.5)
        pyautogui.write('')  # Type "notepad" into the Run dialog
        time.sleep(0.5)
        pyautogui.press('enter')  # Press Enter to open Notepad
        time.sleep(2)  # Wait for Notepad to open
        pyautogui.write(note)  # Type the note into Notepad
    except Exception as e:
        speak("Sorry, I encountered an error while writing the note.")
        print(e)


# TO CLOSE NOTEPAD
def close_notepad():
    speak("closing notepad")
    os.system("taskkill /f /im notepad.exe")


# TO FIND IP ADDRESS
def ip_address():
    ip = requests.get("https://api.ipify.org").text
    print(ip)
    speak(f"YOUR ID AdDRESS IS {ip}")


# TO OPEN CMD
def cmd():
    speak("opening command prompt")
    os.system("start cmd")


# TO CLOSE CMD
def close_cmd():
    speak("closing command prompt")
    os.system("taskkill /f /im cmd.exe")


# TO OPEN PYCHARM
def pycharm():
    speak("opening py charm")
    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.3.4\\bin\\pycharm64.exe"
    os.startfile(path)


# TO CLOSE PYCHARM
def close_pycharm():
    speak("closing py charm")
    os.system("taskkill /f /im pycharm64.exe")


# TO OPEN SQL PLUS ORACLE
def sql_plus():
    speak("opening sql plus")
    path = "C:\\Users\\manoj\\Desktop\\SQL Plus.lnk"
    os.startfile(path)

# TO CLOSE SQL PLUS
def close_sql_plus():
    speak("closing sql plus")
    os.system("taskkill /f /sql plus.exe")


# TO OPEN EXCEL
def excel():
    speak("opening excel")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
    os.startfile(path)

# TO CLOSE EXCEL
def close_excel():
    speak("closing excel")
    os.system("taskkill /f /im EXCEL.exe")


# TO OPEN POWER_POINT
def powerpoint():
    speak("opening powerpoint")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
    os.startfile(path)


# TO CLOSE POWER_POINT
def close_powerpoint():
    speak("closing powerpoint")
    os.system("taskkill /f /im POWER_POINT.exe")


#  TO OPEN PHOTOSHOP
def photoshop():
    speak("opening adobe photoshop")
    path = "C:\\Program Files (x86)\\Adobe"
    os.startfile(path)

# TO CLOSE PHOTOSHOP
def close_photoshop():
    speak("closing photoshop")
    os.system("taskkill /f /im Photoshop.exe")

# TO OPEN ARDUINO
def arduino():
    speak("opening arduino UNO")
    path = "C:\\Users\\manoj\\Downloads\\arduino-ide_2.3.2_Windows_64bit.exe"
    os.startfile(path)

# TO CLOSE ARDUINO
def close_arduino():
    speak("closing arduino UNO")
    os.system("taskkill /f /im  ArduinoIDE.exe")

# TO OPEN WORD
def word():
    speak("opening word")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
    os.startfile(path)

# TO CLOSE WORD
def close_word():
    speak("closing word")
    os.system("taskkill /f /im WIN WORD.exe")

# TO OPEN VLC MEDIA PLAYER
def vlc_media_player():
    speak("opening VLC media player")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player.lnk"
    os.startfile(path)

# TO CLOSE VLC MEDIA PLAYER
def close_vlc_media_player():
    speak("closing VLC media player")
    os.system("taskkill /f /im  vlc_media_player.exe")


# TO OPEN CHROME
def chrome():
    speak("opening chrome")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
    os.startfile(path)
    speak("what should i search on chrome")
    qn = take_command().lower()
    wb.open(f"https://www.google.com/search?q={qn}")

# TO CLOSE CHROME
def close_chrome():
    speak("closing chrome")
    os.system("taskkill /f /im chrome.exe")


def joke():
    n = pyjokes.get_joke()
    print(n)
    speak(n)

# TO OPEN WHATSAPP
def whatsapp():
    speak("opening whatsapp")
    path = "C:\\Users\\manoj\\Downloads\\WhatsApp Installer.exe"
    os.startfile(path)

# TO CLOSE WHATSAPP
def close_whatsapp():
    speak("closing whatsapp")
    os.system("taskkill /f /im  whatsapp.exe")

# TO OPEN PYTHON
def python():
    speak("opening python")
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.12\\Python 3.12 (64-bit).lnk"
    os.startfile(path)

# TO CLOSE PYTHON
def close_python():
    speak("closing python")
    os.system("taskkill /f /im python.exe")


# TO OPEN BIKE RACING 1
def bike_racing_1():
    speak("opening bike racing 1")
    path = "C:\\Users\\manoj\\Desktop\\Bike Racing 1.lnk"
    os.startfile(path)

# TO CLOSE BIKE RACING 1
def close_bike_racing_1():
    speak("closing bike racing 1")
    os.system("taskkill /f /im bike racing 1.app.exe")

def timme():
    strTime = datetime.datetime.now()
    curTime = str(strTime.hour) + " hours" + " " + str(strTime.minute) + " minutes" + " " + str(
        strTime.second) + " seconds"
    print(curTime)
    speak(f" the time is {curTime}")

# TO OPEN TELEGRAM
def telegram():
    speak("opening telegram")
    path = "C:\\Users\\HP\\Documents\\Desktop\\Telegram Desktop"
    os.startfile(path)

# TO CLOSE TELEGRAM
def close_telegram():
    speak("closing telegram")
    os.system("taskkill /f /im Telegram.exe")

# TO STOP EXECUTION
def stop():
    f = "bye sir", "see you again sir"
    speak(random.choice(f))
    sys.exit()

# TO OPEN NEWS
def news():
    wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
    speak('Here are some headlines from the Times of India,Happy reading')


# to take input from user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("YOU SAID:", query)
    except Exception as e:
        print(e)
        print("unable to recognize")
        return ""
    return query.lower()



if 1 == 1:
    wish_time()
    take_command()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            wiki()
        elif 'open youtube' in query:
            youtube()
        elif 'play on youtube' in query or 'search in youtube' in query or 'search youtube' in query or 'Search youtube' in query or 'play youtube' in query or 'Play youtube' in query or 'Youtube' in query or 'youtube' in query:
            play_yt(query)
        elif 'open google' in query:
            google()
        elif 'open facebook' in query:
            facebook()
        elif 'open classroom' in query or 'open gcr' in query:
            classroom()
        elif 'open mail' in query or 'open gmail' in query or 'open email' in query:
            gmail()
        elif 'open edu serve' in query or 'open edu_serve' in query or 'open students portal' in query:
            edu_serve()
        elif 'open dogs' in query or 'open docs' in query or 'open google docs' in query or 'open google dogs' in query:
            docs()
        elif 'open chrome' in query:
            chrome()
        elif 'close chrome' in query:
            close_chrome()
        elif 'open notepad' in query:
            notepad()
        elif 'write note' in query or 'write the note' in query or 'take note' in query or 'take the notes' in query:
            write_note()
        elif 'close notepad' in query:
            close_notepad()
        elif 'ip address' in query:
            ip_address()
        elif 'open py charm' in query or 'open pycharm' in query:
            pycharm()
        elif 'close py charm' in query or 'close pycharm' in query:
            close_pycharm()
        elif 'open sql plus' in query or 'open sql plus' in query:
            sql_plus()
        elif 'close sql plus' in query or 'close sql plus' in query:
            close_sql_plus()
        elif 'open excel' in query:
            excel()
        elif 'close excel' in query:
            close_excel()
        elif 'open powerpoint' in query:
            powerpoint()
        elif 'close powerpoint' in query:
            close_powerpoint()
        elif 'open photoshop' in query:
            photoshop()
        elif 'close photoshop' in query:
            close_photoshop()
        elif 'open arduino' in query or 'open arduino uno' in query:
            arduino()
        elif 'close arduino' in query or 'open arduino uno' in query:
            close_arduino()
        elif 'open word' in query:
            word()
        elif 'close word' in query:
            close_word()
        elif 'open vlc media player' in query or 'open vlc media player' in query:
            vlc_media_player()
        elif 'close vlc media player' in query or 'close vlc media player' in query:
            close_vlc_media_player()
        elif 'open command' in query or 'open cmd' in query or 'open comment' in query:
            cmd()
        elif 'close command ' in query or 'close cmd' in query or 'close comment' in query:
            close_cmd()
        elif 'open whatsapp' in query:
            whatsapp()
        elif 'close whatsapp' in query:
            close_whatsapp()
        elif 'open python' in query:
            python()
        elif 'close python' in query:
            close_python()
        elif 'open bike racing 1' in query:
            bike_racing_1()
        elif 'close bike racing 1' in query:
            close_bike_racing_1()
        elif 'open telegram' in query:
            telegram()
        elif 'close telegram' in query:
            close_telegram()
        elif 'play music' in query or 'play song' in query or 'play me a song' in query or 'sing me a song' in query:
            music()
        elif 'change music' in query or 'change song' in query or 'change a song' in query or 'change the song' in query or 'change the music ' in query:
            change_music()
        elif 'play movie' in query or 'play movie' in query or 'play me a movie' in query or 'play the movie' in query:
            movie()
        elif 'change movie' in query or 'change movie' in query or 'change a movie' in query or 'change the movie' in query or 'change the movie' in query:
            change_movie()
        elif 'screenshot' in query:
            screenshot()
        elif 'quit' in query or 'bye' in query or 'stop' in query or 'exit' in query or 'dont listen' in query:
            stop()
        elif 'hai' in query:
            speak("Hai !")
            speak("how are you")
            print("Hai !")
            print("how are you")
        elif "good morning" in query or "good afternoon" in query or "good evening" in query:
            speak("A very" + query)
            speak("Thank you for wishing me! Hope you are doing well!")
        elif "good night" in query:
            speak("good night")
            speak("Sweet dreams.Sleep peacefully")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            print("It's good to know that your fine")
        elif "who are you" in query:
            speak(f"My name is {v_name}, I am your personal voice assistant")
        elif "thank you" in query:
            speak("It's my pleasure!")
        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you")
        elif "hello" in query:
            speak("hello")
        elif 'time' in query:
            timme()
        elif 'joke' in query:
            joke()
        elif "my girlfriend" in query or "my boyfriend" in query:
            speak("I'm not sure about that, may be you should give me some time")
        elif "i love you" in query or "love you" in query:
            speak("Thank you! But, It's a pleasure to hear it from you.")
        elif 'search' in query:
            search(query)
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "your name" in query:
            speak(f"my name is {v_name}")
        elif "i am" in query or "am i" in query:
            speak("If you talk then definitely your human.")
        elif 'lock' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif "where is" in query or "locate" in query or "location" in query:
            location(query)
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query or "shutdown" in query:
            speak("logging off")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "show note" in query or "so note" in query or "show notes" in query or "so notes" in query:
            show_note()
        elif 'news' in query:
            news()
        elif "made you" in query or "created you" in query or "discovered you" in query:
            speak("I was built by JERK BRAHMOS AND TEAM")
            print("I was built by JERK BRAHMOS AND TEAM")
        elif 'you do' in query:
            speak(
                ' I am programmed to minor tasks like , opening  youtube , google , chrome , gmail and few more , and even opening and closing some software , predicting time , searching in youtube , google , wikipedia , playing music , movies , getting top headline news from times of india AND FEW MORE')
        elif 'ask' in query or 'who' in query or 'what' in query or 'how' in query:
            qn(query)
        elif "change voice" in query or "voice" in query or "Voice" in query:
            voice()
        elif "change name" in query:
            speak("What would you like to call me")
            v_name = take_command()
            speak("My name is changed")
        else:
            speak("Sorry, I am not able to understand you")
