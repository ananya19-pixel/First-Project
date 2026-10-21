def chatbot():
    print("===============================================")
    print("Welcome to ChatBot!")
    print("===============================================")
    print("You can Chat here: hello, how are you, or bye")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")

        elif user_input in ["good morning", "morning"]:
            print("Bot: Good morning! Have a wonderful day! ☀️")

        elif user_input in ["good afternoon"]:
            print("Bot: Good afternoon! Hope you are doing well!")

        elif user_input in ["good evening"]:
            print("Bot: Good evening! How was your day?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")
            reply = input("Bot: And how are you?:").lower().strip()

            if any(word in reply for word in
                   ["good", "fine", "great", "happy", "awesome", "well"]):
                print("Bot: Nice to hear that! 😊")

            elif any(word in reply for word in
                     ["bad", "sad", "upset", "not good", "unhappy"]):
                print("Bot: I'm sorry to hear that. I hope you feel better soon. 💙")

        elif user_input in ["what is your name", "your name"]:
            print("Bot: My name is a Python Chatbot!")

        elif user_input in ["what are you doing", "what are you up to"]:
            print("Bot: I'm chatting with you! 😊")

        elif user_input in ["who made you", "who created you"]:
            print("Bot: I was created by Ananya using Python! 💻")

        elif user_input in ["tell me something", "say something"]:
            print("Bot: Every expert was once a beginner, same as I'm also!")

        elif user_input in ["what can you do", "your features"]:
            print("Bot: I can chat, answer greetings, and respond to your messages!")

        elif user_input in ["nice to talk to you", "nice talking to you"]:
            print("Bot: Likewise!")

        elif user_input in ["good job", "well done"]:
            print("Bot: Thank you! You're awesome too! 🌟")

        elif user_input in ["see you", "see you later", "take care"]:
            print("Bot: See you soon! Take care! 👋")

        elif user_input in ["ok", "okay", "alright"]:
            print("Bot: Okay! What would you like to talk about?")

        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot() 

