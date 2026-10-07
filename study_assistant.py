"""Command-line JEE study assistant powered by Groq."""

import os
import sys

from dotenv import load_dotenv
from groq import Groq

MODES = {
    "1": "Explain the concept in simple Hinglish, give important formulas, one real-life example, common mistakes, and 5 JEE-level MCQs with answers.",
    "2": "List important formulas, explain their variables and units, and give concise JEE tips. Use Hinglish.",
    "3": "Create 10 JEE-level MCQs with four options, the correct answer, and a short explanation. Use Hinglish.",
    "4": "Create a concise revision sheet with key concepts, formulas, short tricks, and exam tips. Use Hinglish.",
}


def build_prompt(subject: str, topic: str, mode: str) -> str:
    if mode not in MODES:
        raise ValueError("Choose a study mode from 1 to 4.")
    return f"You are a careful JEE tutor. Subject: {subject}\nTopic: {topic}\n\n{MODES[mode]}"


def generate_response(prompt: str, client) -> str:
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    if not answer or not answer.strip():
        raise RuntimeError("The model returned an empty response.")
    return answer.strip()


def save_notes(content: str) -> None:
    os.makedirs("generated_notes", exist_ok=True)
    with open("generated_notes/jee_notes.txt", "w", encoding="utf-8") as notes_file:
        notes_file.write(content + "\n")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key or api_key == "your_api_key_here":
        print("GROQ_API_KEY is missing. Copy .env.example to .env and add your key.", file=sys.stderr)
        return 1

    print("JEE Study Assistant · made by cr1ms0ncode")
    subject = input("Subject (Physics/Chemistry/Mathematics): ").strip()
    topic = input("Topic: ").strip()
    print("1 Concept explanation · 2 Formula revision · 3 MCQ practice · 4 Quick revision")
    mode = input("Choose mode (1-4): ").strip()
    if subject.casefold() not in {"physics", "chemistry", "mathematics", "maths"} or not topic:
        print("Enter Physics, Chemistry, or Mathematics and a non-empty topic.", file=sys.stderr)
        return 1
    try:
        prompt = build_prompt(subject, topic, mode)
        answer = generate_response(prompt, Groq(api_key=api_key))
    except Exception as error:
        print(f"Generation failed: {error}", file=sys.stderr)
        return 1

    print("\n" + answer)
    save_notes(answer)
    print("\nNotes saved to generated_notes/jee_notes.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
