# Gemini Terminal Chatbot

A simple command-line chatbot built in Python that talks to Google's Gemini AI model. Built as a learning project to practice working with APIs, JSON, and error handling.

## Features

- Chat with Google's Gemini AI directly from your terminal
- Remembers the whole conversation (multi-turn context)
- Handles common errors gracefully: no internet, invalid API key, rate limits, timeouts
- Wraps long replies so they're easy to read

## How it works

The script sends your message (plus the full chat history) to Google's Gemini API using a simple HTTP POST request, then prints the AI's reply. Each new message and reply gets added to the conversation history, so the AI can refer back to earlier things you said.

## Requirements

- Python 3
- `requests` library (`pip install requests`)
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. Install the dependency:
   ```
   pip install requests
   ```

3. Get a free API key from [Google AI Studio](https://aistudio.google.com) (no credit card required).

4. Open `chatbot.py` and paste your key into this line:
   ```python
   API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
   ```

5. Run it:
   ```
   python chatbot.py
   ```

6. Type your messages and chat. Type `quit` or `exit` to leave.

## Notes

- Never commit your real API key to a public repo. Keep the placeholder in any version you upload, and only put your real key in a local copy that you don't push to GitHub.
- Uses the `gemini-3.6-flash` model on Google's free tier.

## What I learned building this

- Making HTTP requests to a REST API in Python
- Structuring and sending JSON payloads
- Keeping conversation state across multiple requests
- Handling network errors and bad API responses without crashing

## Possible next steps

- Save conversation history to a file so it persists between runs
- Add a simple GUI version
- Let the user switch between different Gemini models
- 
