# Friday Voice Assistant

Friday is a small Windows voice assistant inspired by the Iron Man scene where Jarvis comes online and prepares the workspace. It listens for a wake command, reads the day's tasks, starts a random anthem, opens configured tools, and gives a spoken daily briefing.

## How Friday Works

1. Start `friday.py` from the `friday_ai_assistant` folder.
2. Friday turns on the microphone and adjusts for background noise.
3. Say a command containing both **"Friday"** and **"initiate"** or **"initialize"**.
4. Friday reads the tasks from `tasks.txt`.
5. It randomly chooses one of the `anthem1.mp3` through `anthem10.mp3` files and plays it at low volume.
6. It opens the configured workspace applications and websites.
7. Windows SAPI speaks the greeting and reads the tasks aloud.
8. The program stays open until the anthem finishes playing.

If the command cannot be understood, Friday reports that it could not understand the audio. If Google's speech-recognition service cannot be reached, it reports the connection problem.

## Requirements

- Windows
- Python 3.12
- A working microphone
- An internet connection for Google's speech-recognition service
- Microsoft Zira voice installed if you want Friday's configured female voice
- Python packages:

```bash
pip install SpeechRecognition pywin32 pygame PyAudio
```

`PyAudio` may need an installation method compatible with your Python version and Windows system if a normal `pip install` fails.

## Setup

Clone or download the repository, then open PowerShell in this folder:

```powershell
cd friday_ai_assistant
python -m pip install SpeechRecognition pywin32 pygame PyAudio
```

Keep `tasks.txt` and all ten anthem files in the same folder as `friday.py`. The program uses these relative paths when it runs.

## Run Friday

Open PowerShell in the `friday_ai_assistant` folder and run:

```powershell
python friday.py
```

Then say something such as:

```text
Friday, initiate
```

You can edit `tasks.txt` before starting Friday. Put one task on each line so that the assistant can read them as part of the briefing.

The included `start_friday.bat` can also be used as a launcher. Its `cd` command contains a computer-specific path, so update that path to the location of this `Friday` folder before using it.

## Workspace Actions

When activated, the script currently tries to:

- Open `Claude.lnk` from the desktop
- Open `ChatGPT.lnk` from the desktop
- Open Gemini in a web browser
- Start Visual Studio Code with the `code` command

The shortcut paths and commands are specific to my computer. Change them in `friday.py` if your shortcuts, browser setup, or development tools are different. The program also expects the `code` command to be available on `PATH`.

## Limitations

- Friday listens for one command each time it starts; it does not run as a continuous wake-word service.
- Speech recognition uses Google's online service, so an internet connection is required.
- The configured desktop shortcuts and workspace tools must exist on the computer running the script.

## Project Story

I first thought of this project after watching the Iron Man "Daddy's home" scene. I wanted to create something with that same feeling: saying a command and having an assistant bring the workspace to life.

Making it was much more challenging than I expected. I had to install and work with different Python versions and modules, fix bugs, troubleshoot audio and microphone issues, and keep grinding through the problems all day. It was frustrating at times, but it was also quite adventurous. In the end, that process became this program: my own small step toward a real-world voice assistant.

## Project Files

```text
friday_ai_assistant/
├── friday.py          # Main voice assistant program
├── tasks.txt          # Daily tasks read by Friday
├── start_friday.bat   # Optional Windows launcher
├── anthem1.mp3 ...
├── anthem10.mp3       # Random background anthems
└── README.md          # Project documentation
```
