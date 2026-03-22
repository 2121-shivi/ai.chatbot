import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Knowledge base
questions = [
    "hello",
    "hi",
    "what is cybersecurity",
    "what is machine learning",
    "what is python",
    "how are you"
]

answers = [
    "Hello! How can I help you?",
    "Hi there!",
    "Cybersecurity protects systems from cyber attacks.",
    "Machine learning allows systems to learn from data.",
    "Python is a popular programming language.",
    "I'm just a bot, but I'm doing great!"
]

# Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Memory
user_name = ""

def chatbot_response(user_input):
    global user_name

    # Store name
    if "my name is" in user_input.lower():
        user_name = user_input.split("is")[-1].strip()
        return f"Nice to meet you, {user_name}!"

    # Use name later
    if "what is my name" in user_input.lower():
        return f"Your name is {user_name}" if user_name else "I don't know your name yet."

    # Convert input to vector
    user_vec = vectorizer.transform([user_input])

    # Similarity check
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()

    if similarity[0][index] > 0.3:
        return answers[index]
    else:
        return random.choice([
            "I'm not sure I understand.",
            "Can you rephrase that?",
            "Interesting question!"
        ])

# Chat loop
print("🤖 Smart AI Chatbot (type 'bye' to exit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)