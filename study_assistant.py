from groq import Groq

print("=" * 50)
print("   JEE Study Assistant 🤖📚")
print("   Made by cr1ms0ncode 🚀")
print("=" * 50)
print()
print("SETUP: console.groq.com se API key lo")
print()

api_key = input("Enter your Groq API Key: ")
client = Groq(api_key=api_key)

print()
print("Subjects: Physics, Chemistry, Maths")
subject = input("Subject daalo: ")
topic = input("Topic daalo: ")

print()
print("Generating response... ⚡")
print()

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": f"Tum ek helpful study assistant ho JEE/Board students ke liye. Subject: {subject}, Topic: {topic}. Simple Hinglish mein explain karo. Ek real-life example do. 3 practice questions do with answers."
        }
    ]
)

print("=" * 50)
print(response.choices[0].message.content)
print("=" * 50)