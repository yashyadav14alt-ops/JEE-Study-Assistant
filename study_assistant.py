from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY not found in .env file")
    exit()

client = Groq(api_key=api_key)


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

    print("Subjects Available:")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Mathematics")
    print()

    subject = input("Enter Subject: ").strip()
    topic = input("Enter Topic: ").strip()

    print()
    print("Study Modes:")
    print("1. Concept Explanation")
    print("2. Formula Revision")
    print("3. MCQ Practice")
    print("4. Quick Revision")
    print()

    mode = input("Choose Mode (1-4): ").strip()

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

    elif mode == "2":

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

    elif mode == "3":

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

    else:

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


# -----------------------------
# AI Response
# -----------------------------
def generate_response(prompt):

    try:

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ Error: {e}"


# -----------------------------
# Save Notes
# -----------------------------
def save_notes(content):

    os.makedirs("generated_notes", exist_ok=True)

    with open(
        "generated_notes/jee_notes.txt",
        "w",
        encoding="utf-8"
    ) as file:

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

    print()
    print("⚡ Generating Response...")
    print()

    prompt = build_prompt(
        subject,
        topic,
        mode
    )

    answer = generate_response(prompt)

    print("=" * 60)
    print(answer)
    print("=" * 60)

    save_notes(answer)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    main()