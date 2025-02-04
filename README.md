# BCA-Final-Year-Project-2023
1. Initialization
When you run the script, the following initializations occur:

Text-to-Speech Engine: The pyttsx3 library initializes the text-to-speech engine and sets the voice properties.
Greeting: The assistant greets you based on the current time of day (morning, afternoon, or evening).

2. Listening for Commands
The assistant continuously listens for your voice commands using the speech_recognition library. It uses the microphone to capture audio input.

3. Processing Commands
Once a command is recognized, the assistant processes it to determine the appropriate action. The recognized command is converted to lowercase to ensure consistency in processing.

4. Executing Commands
Based on the recognized command, the assistant performs various tasks. Here are some examples:

Web Searches:

Google Search: If you say "search for [query]", the assistant will open a web browser and search Google for the specified query.
Wikipedia Search: If you say "search Wikipedia for [query]", the assistant will fetch a summary from Wikipedia.

Media Playback:

YouTube: If you say "play [video] on YouTube", the assistant will search for and play the specified video on YouTube.
Music: If you say "play music", the assistant will play a random music file from a specified directory.
Movies: If you say "play a movie", the assistant will play a random movie file from a specified directory.

Application Management:

Open Applications: Commands like "open Notepad", "open PyCharm", "open Excel", etc., will open the respective applications.
Close Applications: Commands like "close Notepad", "close PyCharm", "close Excel", etc., will close the respective applications.

System Operations:

IP Address: If you say "what is my IP address", the assistant will retrieve and speak your IP address.
Lock Device: If you say "lock the device", the assistant will lock your computer.
Take Screenshot: If you say "take a screenshot", the assistant will capture and save a screenshot.

Personalization:

Change Voice: If you say "change voice", the assistant will switch to a female voice.
Change Name: If you say "change your name to [name]", the assistant will change its name to the specified name.

Entertainment:

Tell a Joke: If you say "tell me a joke", the assistant will tell a joke using the pyjokes library.
News: If you say "give me the news", the assistant will open the Times of India news website.

5. Continuous Interaction
The assistant continuously listens for new commands and performs the corresponding actions. It provides voice feedback for each action, making the interaction more engaging and user-friendly.

6. Stopping the Assistant
If you say "stop", "quit", "bye", or "exit", the assistant will stop listening and terminate the program.

Performance and User Experience
Real-Time Interaction: The assistant provides real-time responses to voice commands, making the interaction seamless and efficient.
Task Automation: The assistant automates various tasks, reducing the need for manual input and enhancing productivity.
Personalization: The ability to change the assistant's voice and name adds a personal touch to the interaction.
Convenience: The assistant provides a convenient way to perform tasks using voice commands, making it easier to manage applications, search the web, and access information.
Overall, this personal assistant project aims to provide a user-friendly and efficient way to interact with your computer using voice commands, enhancing your productivity and user experience. If you have any more questions or need further assistance, feel free to ask! 😊
Overview
This code is a Python-based personal assistant that can perform various tasks based on voice commands. It uses libraries like speech_recognition for recognizing speech, pyttsx3 for text-to-speech conversion, and several other libraries for specific functionalities like web browsing, playing music, taking screenshots, etc.

Code Structure

1. Imports
The code imports various libraries required for different functionalities:

ctypes, random, subprocess, os, sys, time: Standard libraries for system operations. 
pyjokes, pyttsx3, datetime, speech_recognition, wikipedia, requests, webbrowser, pywhatkit, pyautogui, winshell, wolframalpha, BeautifulSoup, pytube: Third-party libraries for specific tasks.

2. Initialization
The text-to-speech engine (pyttsx3) is initialized, and the voice properties are set:

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

3. Helper Functions
Several helper functions are defined to perform specific tasks:

voice(): Changes the voice to a female voice.
speak(audio): Converts text to speech.
wish_time(): Greets the user based on the current time.
search(query): Searches the web using Google.
music(): Plays a random music file from a specified directory.
change_music(): Changes the currently playing music.
show_note(): Displays the content of a note.
movie(): Plays a random movie file from a specified directory.
change_movie(): Changes the currently playing movie.
location(query): Opens Google Maps to show a specified location.
wiki(): Searches Wikipedia for a specified query.
qn(query): Provides a brief summary from Wikipedia.
screenshot(): Takes a screenshot and saves it with a specified name.
google(): Searches Google for a specified query.
youtube(): Opens YouTube.
play_yt(query): Plays a specified video on YouTube.
facebook(): Opens Facebook.
classroom(): Opens Google Classroom.
gmail(): Opens Gmail.
edu_serve(): Opens the EduServe student portal.
docs(): Opens Google Docs.
notepad(): Opens Notepad.
write_note(): Writes a note in Notepad.
close_notepad(): Closes Notepad.
ip_address(): Retrieves and speaks the IP address.
cmd(): Opens the Command Prompt.
close_cmd(): Closes the Command Prompt.
pycharm(): Opens PyCharm.
close_pycharm(): Closes PyCharm.
sql_plus(): Opens SQL Plus.
close_sql_plus(): Closes SQL Plus.
excel(): Opens Excel.
close_excel(): Closes Excel.
powerpoint(): Opens PowerPoint.
close_powerpoint(): Closes PowerPoint.
photoshop(): Opens Adobe Photoshop.
close_photoshop(): Closes Adobe Photoshop.
arduino(): Opens Arduino IDE.
close_arduino(): Closes Arduino IDE.
word(): Opens Microsoft Word.
close_word(): Closes Microsoft Word.
vlc_media_player(): Opens VLC Media Player.
close_vlc_media_player(): Closes VLC Media Player.
joke(): Tells a joke using the pyjokes library.
whatsapp(): Opens WhatsApp.
close_whatsapp(): Closes WhatsApp.
python(): Opens Python.
close_python(): Closes Python.
bike_racing_1(): Opens Bike Racing 1 game.
close_bike_racing_1(): Closes Bike Racing 1 game.
timme(): Tells the current time.
telegram(): Opens Telegram.
close_telegram(): Closes Telegram.
stop(): Stops the assistant and exits the program.
news(): Opens the Times of India news website.
take_command(): Listens for a voice command and returns it as text.

4. Main Function
The main function initializes the assistant, greets the user, and continuously listens for commands to execute the corresponding functions:

if __name__ == "__main__":
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
        elif 'quit
