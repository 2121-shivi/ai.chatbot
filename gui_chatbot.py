import nltk
import random
from nltk.tokenize import word_tokenize

# Download tokenizer (run once)
nltk.download('punkt')

# Define responses
responses = {
    "hello": ["Hi there!", "Hello! How can I assist you?"],
    "hi": ["Hello!", "Hey! What can I do for you?"],
    "cybersecurity": ["Cybersecurity protects systems and networks from attacks."],
    "machine learning": ["Machine learning allows systems to learn from data."],
    "bye": ["Goodbye!", "See you later!"]
}

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())

    for word in tokens:
        if word in responses:
            return random.choice(responses[word])

    return "I'm not sure about that, but I'm learning!"

# Chat loop
print("🤖 AI Chatbot (type 'bye' to exit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)