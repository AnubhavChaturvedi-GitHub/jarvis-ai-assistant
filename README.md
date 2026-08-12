# J.A.R.V.I.S: Voice-Controlled AI Assistant in Python

> An offline-friendly, voice-activated AI desktop assistant that listens, thinks, speaks and controls your computer. Speech recognition, text to speech, real-time web search, image generation, computer vision and WhatsApp automation in one Python project.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/AnubhavChaturvedi-GitHub/jarvis-ai-assistant?style=for-the-badge&color=yellow)](https://github.com/AnubhavChaturvedi-GitHub/jarvis-ai-assistant/stargazers)
[![Forks](https://img.shields.io/github/forks/AnubhavChaturvedi-GitHub/jarvis-ai-assistant?style=for-the-badge&color=blue)](https://github.com/AnubhavChaturvedi-GitHub/jarvis-ai-assistant/network/members)

![J.A.R.V.I.S in action](https://github.com/user-attachments/assets/59727c15-d85a-41bc-b27d-bea08b3b3a41)

## What it does

J.A.R.V.I.S (Just A Rather Very Intelligent System) is a Python voice assistant inspired by Iron Man. You speak, it understands the intent, runs the right module, and answers out loud. It is built as separate, swappable subsystems rather than one giant script, so you can use only the parts you need.

## Features

| Module | What it gives you |
|---|---|
| `NetHyTechSTT` | Custom speech to text engine, no paid API required |
| `TextToSpeech` | Natural spoken replies |
| `Brain` / `co_brain.py` | Language model reasoning and conversation memory |
| `Real_Time` | Live web search so answers are not limited to training data |
| `TextToImage` | Generate images from a spoken prompt |
| `Vision` | Camera capture and image understanding |
| `Automation` | Open apps, control the desktop, run system tasks |
| `Whatsapp_automation` | Send WhatsApp messages hands free |
| `Weather_Check` | Live weather by location |
| `Time_Operations` | Alarms, reminders and scheduling |

## Getting started

### Prerequisites

- Python 3.10 or newer
- A working microphone and speakers
- Google Chrome (used by the browser automation modules)

### Installation

```bash
git clone https://github.com/AnubhavChaturvedi-GitHub/jarvis-ai-assistant.git
cd jarvis-ai-assistant
pip install -r requirements.txt
```

### Run it

```bash
python jarvis.py
```

Prefer a window over a terminal:

```bash
python ui.py
```

## Usage

Say the wake word, then speak naturally:

- "What is the weather in Bangalore?"
- "Open Chrome and search for transformer architecture"
- "Generate an image of a red sports car at sunset"
- "Send a WhatsApp message to Rahul saying I am running late"
- "What is happening in the news right now?"

## Project structure

```
jarvis.py              entry point, intent routing
ui.py                  desktop interface
co_brain.py            reasoning and conversation memory
NetHyTechSTT/          speech to text engine
TextToSpeech/          voice output
TextToImage/           image generation
Real_Time/             live web search
Vision/                camera and image understanding
Automation/            desktop and app control
Whatsapp_automation/   messaging
Weather_Check/         weather lookups
Time_Operations/       alarms and scheduling
```

## Tech stack

Python, SpeechRecognition, Selenium, PyWhatKit, OpenCV, Requests, Tkinter.

## Contributing

Issues and pull requests are welcome. Fork the repo, create a feature branch, and open a PR describing what changed and why.

## License

Released under the [MIT License](LICENSE).

## Author

**Anubhav Chaturvedi**, founder of [NetHyTech](https://www.youtube.com/@NetHyTech), a developer community of 30,000+ members.

[![YouTube](https://img.shields.io/badge/YouTube-NetHyTech-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@NetHyTech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anubhav-chaturvedi-/)

If this project saved you time, a star on the repo helps other people find it.
