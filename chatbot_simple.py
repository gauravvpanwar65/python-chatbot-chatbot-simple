# chatbot_simple.py

def chatbot_response(user_input):
    # Predefined responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "bye": "Goodbye! Have a great day 👋",
        "how are you": "I'm just a bot, but I'm doing great! 😃",
        "help": "I can assist you with basic questions. Try saying 'hello' or 'bye'."
    }

    # Convert user input to lowercase for matching
    user_input = user_input.lower()

    # Check if input matches a response
    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I didn't understand. Can you rephrase?"

# --- Run chatbot ---
print("🤖 Chatbot is ready! Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)
    if user.lower() == "bye":
        break
