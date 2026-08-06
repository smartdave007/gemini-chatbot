"""
Simple AI Chatbot - built with Python + Google's Gemini API
Runs in the terminal (works great in Pydroid).

A beginner-friendly project to learn:
- Making web requests (talking to an API)
- Working with JSON data
- Keeping conversation history (so the AI remembers earlier messages)
"""

import requests

# ---------- SETUP ----------
# PASTE YOUR API KEY BETWEEN THE QUOTES BELOW.
# Keep this private - don't share this file with your key still in it!
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

MODEL = "gemini-2.5-flash"  # free-tier model
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


def ask_gemini(conversation_history):
    """
    Send the full conversation so far to Gemini and get a reply.
    conversation_history is a list of {"role": ..., "parts": [...]} dicts.
    """
    payload = {"contents": conversation_history}

    response = requests.post(URL, json=payload)

    if response.status_code != 200:
        print(f"\n[Error {response.status_code}]: {response.text}\n")
        return None

    data = response.json()

    # Pull the actual reply text out of Gemini's response structure
    reply = data["candidates"][0]["content"]["parts"][0]["text"]
    return reply


def main():
    print("=" * 50)
    print("  Gemini Chatbot - type 'quit' to exit")
    print("=" * 50)

    # This list keeps track of the whole conversation so the AI has memory
    conversation_history = []

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Add the user's message to history
        conversation_history.append({
            "role": "user",
            "parts": [{"text": user_input}]
        })

        print("\nThinking...")
        reply = ask_gemini(conversation_history)

        if reply is None:
            # Something went wrong - remove the message we just added
            # so it doesn't mess up the next request
            conversation_history.pop()
            continue

        print(f"\nGemini: {reply}")

        # Add the AI's reply to history too, so it remembers what it said
        conversation_history.append({
            "role": "model",
            "parts": [{"text": reply}]
        })


if __name__ == "__main__":
    main()
