# BCA-Final-Year-Project-2023

Overview
This code is a Python-based personal assistant that can perform various tasks based on voice commands. It uses libraries like speech_recognition for recognizing speech, pyttsx3 for text-to-speech conversion, and several other libraries for specific functionalities like web browsing, playing music, taking screenshots, etc.

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
