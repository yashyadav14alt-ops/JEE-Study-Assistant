from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


# -----------------------------
# Banner
# -----------------------------
def banner():
    print("=" * 60)
    print("🤖 JEE Study Assistant")
    print("🚀 Made by cr1ms0ncode")
    print("=" * 60)
    print()


# -----------------------------
# User Input
# -----------------------------
def get_user_input():
    subjects = {"1": "Physics", "2": "Chemistry", "3": "Mathematics"}
    modes = {
        "1": "Concept Explanation",
        "2": "Formula Revision",
        "3": "MCQ Practice",
        "4": "Quick Revision",
    }

    print("Subjects Available:")
    for number, subject_name in subjects.items():
        print(f"{number}. {subject_name}")
    print()

    while True:
        subject_choice = input("Choose Subject (1-3): ").strip()
        if subject_choice in subjects:
            subject = subjects[subject_choice]
            break
        print("Please choose 1, 2, or 3.")

    while True:
        topic = input("Enter Topic: ").strip()
        if topic:
            break
        print("Topic cannot be empty.")

    print()
    print("Study Modes:")
    for number, mode_name in modes.items():
        print(f"{number}. {mode_name}")
    print()

    while True:
        mode = input("Choose Mode (1-4): ").strip()
        if mode in modes:
            break
        print("Please choose a mode from 1 to 4.")

    return subject, topic, mode


# -----------------------------
# Prompt Builder
# -----------------------------
def build_prompt(subject, topic, mode):
    if mode == "1":
        return f"""
You are an expert JEE mentor.

Subject: {subject}
Topic: {topic}

Explain:

1. Concept in simple Hinglish
2. Important formulas
3. Real life example
4. Common mistakes students make
5. 5 JEE-level MCQs with answers

Make it easy but exam-oriented.
"""

    if mode == "2":
        return f"""
Subject: {subject}
Topic: {topic}

Give:

1. All important formulas
2. Formula tricks
3. Units
4. Important notes
5. JEE tips

Use Hinglish.
"""

    if mode == "3":
        return f"""
Subject: {subject}
Topic: {topic}

Generate:

1. 10 JEE-level MCQs
2. Options A/B/C/D
3. Correct Answer
4. Short Explanation

Use Hinglish.
"""

    if mode == "4":
        return f"""
Subject: {subject}
Topic: {topic}

Give a quick revision sheet including:

1. Key concepts
2. Important formulas
3. Short tricks
4. Exam tips

Use Hinglish.
"""

    raise ValueError("Mode must be one of 1, 2, 3, or 4.")


# -----------------------------
# AI Response
# -----------------------------
def generate_response(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not found. Add it to your .env file and try again.")

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
        )
        answer = response.choices[0].message.content
        if not answer:
            raise RuntimeError("The API returned an empty response.")
        return answer
    except Exception as error:
        raise RuntimeError("Could not generate notes. Check your API key and network, then try again.") from error


# -----------------------------
# Save Notes
# -----------------------------
def save_notes(content):
    os.makedirs("generated_notes", exist_ok=True)

    with open("generated_notes/jee_notes.txt", "w", encoding="utf-8") as file:
        file.write(content)

    print()
    print("✅ Notes Saved Successfully")
    print("📄 generated_notes/jee_notes.txt")


# -----------------------------
# Main Program
# -----------------------------
def main():
    banner()

    subject, topic, mode = get_user_input()
    prompt = build_prompt(subject, topic, mode)

    print()
    print("⚡ Generating Response...")
    print()

    try:
        answer = generate_response(prompt)
    except RuntimeError as error:
        print(f"❌ {error}")
        return

    print("=" * 60)
    print(answer)
    print("=" * 60)

    save_notes(answer)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    main()
