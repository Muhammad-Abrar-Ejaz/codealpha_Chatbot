def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if user_input in ["hi", "hello"]:
        return "\033[1;32m🤖 Chatbot:\033[0m Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "\033[1;32m🤖 Chatbot:\033[0m I'm fine, thanks for asking! 😊"
    elif user_input in ["bye", "exit", "goodbye"]:
        return "\033[1;32m🤖 Chatbot:\033[0m Goodbye! Have a great day! 👋"
    else:
        return "\033[1;32m🤖 Chatbot:\033[0m Sorry, I don't understand that. 🤔"

print("\033[1;33m==============================")
print("🤖 Welcome to Simple Chatbot 🤖")
print("==============================\033[0m")

print("\n\033[1;36mType 'bye' or 'exit' to end the chat.\033[0m")

while True:
    user_input = input("\n\033[1;34m👉 You:\033[0m ")
    response = chatbot_response(user_input)
    print(response)
    
    if user_input.lower() in ["bye", "exit", "goodbye"]:
        break

print("\033[1;35m🎉 Chat session ended. Thanks for chatting! 🎉\033[0m")
