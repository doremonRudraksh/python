from tkinter import *
import speech_recognition as sr
from datetime import datetime
import pyttsx3
import subprocess
import webbrowser

root=Tk()
root.geometry("500x500")
root.configure(background="lightblue")

label=Label(root, text="Welcome to our personal dextop assistent", bg="Light Blue", font=("Bahnshrift Light", 15, "bold"))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

text_to_speach = pyttsx3.init()

def speak(audio):
    text_to_speach.say(audio)
    text_to_speach.runAndWait()

def r_audio():
    speak("How can I help You")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ""

    try:
        voice_data = speech_recognisor.recognize_google(audio, language="en-in")

    except sr.UnknownValueError:
        print(" Please repeat I did not get that")
        speak("Please repeat I did not get that")

    respond(voice_data)

def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)

    if "name" in voice_data:
        print("My Name is Jarvis")
        speak("My Name is Jarvis")

    if "time" in  voice_data:
        speak("The current time is ")
        now  = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        speak(current_time)

    if "search" in voice_data:
        speak("opening Google")
        print("Opening Google")
        webbrowser.get().open("https://www.google.com/")

    if "videos" in voice_data:
        speak("opening videos")
        print("Opening viseos")
        webbrowser.get().open("https://www.youtube.com/")

    if "text editor" in voice_data:
        speak("opening editor")
        print("Opening editor")
        subprocess.Popen(["notepad.exe"])

btn=Button(root, text="Start", bg="red3",fg="white",padx=10, pady=1,font=("Arial",11,"bold"), relief=FLAT, command=r_audio)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
    