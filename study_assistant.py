from google import genai

print("=" * 50)
print("   JEE Study Assistant 🤖📚")
print("   Made by cr1ms0ncode 🚀")
print("=" * 50)
print()
print("SETUP GUIDE:")
print("1. Go to: aistudio.google.com")
print("2. Login with Gmail")
print("3. Click 'Get API Key'")
print("4. Copy your API key")
print("5. Paste it below")
print()

api_key = input("Enter your Gemini API Key: ")

client = genai.Client(api_key=api_key)

print()
print("Available Subjects: Physics, Chemistry, Maths")
print()

subject = input("Enter Subject: ")
topic = input("Enter Topic: ")

print()
print("Generating response... please wait!")
print()

prompt = f"""
Tum ek helpful study assistant ho JEE/Board students ke liye.
Subject: {subject}
Topic: {topic}

1. Simple Hinglish mein explain karo
2. Ek real-life example do
3. 3 practice questions do with answers
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print("=" * 50)
print(response.text)
print("=" * 50)