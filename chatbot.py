
import ollama
import pandas as pd
import csv
from datetime import datetime
from pathlib import Path

# Project configuration
MODEL = "llama3.2"
DATASET = Path("dataset")

CHAT_HISTORY = DATASET / "chat_history.csv"
RESPONSES = DATASET / "responses.csv"
LOG_FILE = DATASET / "chatbot_logs.txt"

# Create dataset folder if it does not exist
DATASET.mkdir(exist_ok=True)

# Create CSV files with headers if needed
def initialize_csv(file_path, headers):
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

initialize_csv(
    CHAT_HISTORY,
    ["timestamp", "user_question", "chatbot_response"]
)

initialize_csv(
    RESPONSES,
    ["timestamp", "user_question", "chatbot_response"]
)

# Conversation history for context-aware answers
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful Education Chatbot. "
            "Explain concepts in simple language, give examples, "
            "and help students learn programming and academic subjects. "
            "If you are unsure, say so instead of inventing facts."
        )
    }
]

print("=" * 50)
print("       EDUCATION AI CHATBOT")
print("       Model: Llama 3.2")
print("Type 'exit' to stop the chatbot.")
print("=" * 50)

while True:
    try:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Chatbot: Goodbye! Keep learning.")
            break

        if not question:
            print("Chatbot: Please enter a question.")
            continue

        messages.append({
            "role": "user",
            "content": question
        })

        print("\nChatbot is thinking...")

        result = ollama.chat(
            model=MODEL,
            messages=messages
        )

        answer = result["message"]["content"].strip()

        messages.append({
            "role": "assistant",
            "content": answer
        })

        print("\nChatbot:", answer)

        timestamp = datetime.now().astimezone().isoformat(
            timespec="seconds"
        )

        # Save the conversation to both CSV files
        with open(
            CHAT_HISTORY, "a", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, question, answer])

        with open(
            RESPONSES, "a", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, question, answer])

        # Save a readable text log
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}]\n")
            file.write(f"User: {question}\n")
            file.write(f"Chatbot: {answer}\n")
            file.write("-" * 50 + "\n")

    except KeyboardInterrupt:
        print("\nChatbot stopped by user.")
        break

    except Exception as error:
        print("\nError:", error)
        print("Check that Ollama is running and the model is available.")

print("\nConversation files are saved in the dataset folder.")
