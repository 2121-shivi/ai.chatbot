import tkinter as tk
import random

responses = {
    "hello": ["Hi there!", "Hello!"],
    "hi": ["Hey!", "Hello!"],
    "cybersecurity": ["It protects systems from attacks."],
    "machine learning": ["It helps systems learn from data."],
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice([
    "I'm still learning. Can you rephrase that?",
    "Interesting question! I’ll improve with more data.",
    "I don’t have that information yet."
])

def send():
    user_input = entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")

    response = get_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

# GUI window
root = tk.Tk()
root.title("AI Chatbot")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

root.mainloop()