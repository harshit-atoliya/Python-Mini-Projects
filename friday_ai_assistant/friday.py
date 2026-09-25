import speech_recognition as sr
import win32com.client
import pygame
import os
import time
import webbrowser
import random

# ==========================================
# PHASE 1: SYSTEM INITIALIZATION
# ==========================================

# Initialize the pygame audio mixer to handle background music
pygame.mixer.init()

# Tap directly into the native Windows Voice engine (Bulletproof SAPI)
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Find and set the female voice (Microsoft Zira) for the "Friday" persona
voices = speaker.GetVoices()
for voice in voices:
    if "Zira" in voice.GetDescription():
        speaker.Voice = voice
        break

def speak(text):
    """Feeds text directly to the Windows OS to speak out loud."""
    speaker.Speak(text)

# Initialize the speech recognition brain (The Ears)
r = sr.Recognizer()

#choosing random anthem that we will play
anthem=['anthem1.mp3','anthem2.mp3','anthem3.mp3','anthem4.mp3','anthem5.mp3','anthem6.mp3','anthem7.mp3','anthem8.mp3','anthem9.mp3','anthem10.mp3',]
chosen_anthem=random.choice(anthem)
# ==========================================
# PHASE 2: THE LISTENING LOOP
# ==========================================

# Open the microphone and start listening
with sr.Microphone() as source:
    print("Friday is online. Listening for wake word...")
    
    # Analyze ambient room noise for 1 second to improve microphone accuracy
    r.adjust_for_ambient_noise(source)
    
    # Capture the audio input from the user
    audio = r.listen(source)
    
    try:
        # Convert spoken audio into lowercase text
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        
        # Check if the command contains 'friday', and either 'initiate' or 'initialize'
        if "friday" in command and ("initiate" in command or "initialize" in command):
            
            # ==========================================
            # PHASE 3: PREPARE THE DAILY DEBRIEF
            # ==========================================
            # We build what she is going to say silently BEFORE she says it.
            
            final_speech = "Welcome home, Harshly. Initiating workspace protocols. "
            
            try:
                # Open and read the daily agenda file safely
                with open("tasks.txt", encoding="utf-8") as f:
                    tasks = f.readlines()
                    
                    if len(tasks) == 0:
                        final_speech += "Your schedule is clear today. No tasks found."
                    else:
                        final_speech += "Here is your tasks for today: "
                        
                        # Loop through tasks and clean up invisible newline characters
                        for task in tasks:
                            clean_task = task.strip()
                            if clean_task:
                                # The comma forces Friday to take a natural breath/pause between tasks
                                final_speech += clean_task + ", " 
            
            except FileNotFoundError:
                final_speech += "Warning: I cannot locate your tasks file, sir."
                
            # ==========================================
            # PHASE 4: THE CINEMATIC SEQUENCE
            # ==========================================
            
            # 1. MUSIC: Start the background anthem immediately at 5% volume
            pygame.mixer.music.load(chosen_anthem)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            
            # 2. VISUALS: Send launch commands to Windows instantly
            # (These will begin opening in the background while Friday talks)
            os.startfile("C:/Users/erhar/Desktop/Claude.lnk")
            os.startfile("C:/Users/erhar/Desktop/ChatGPT.lnk")
            webbrowser.open("https://gemini.google.com/")
            os.system("code")
            
            # 3. VOICE: Speak the entire combined greeting and agenda
            speak(final_speech)
            
            # 4. HOLD: Keep the Python script alive until the anthem finishes playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
    # Handle cases where the microphone caught noise but couldn't make out the words
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    # Handle cases where Google's speech servers are unreachable
    except sr.RequestError:
        print("Could not connect to the internet.")