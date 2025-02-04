import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use a robotic/hacker-style voice

def speak(text):
    """Convert text to speech."""
    print(f"[SYSTEM]: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Listening...]")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"[USER]: {command}")
        return command
    except sr.UnknownValueError:
        speak("I did not understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def execute_command(command):
    """Process voice command and execute tasks."""
    if "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_now}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "search wikipedia" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {results}")

    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif "exit" in command or "quit" in command:
        speak("Goodbye, hacker.")
        exit()

    else:
        speak("Command not recognized.")

# Start the voice assistant
speak("Hacker voice assistant activated. How may I assist you?")
while True:
    user_command = listen()
    execute_command(user_command)