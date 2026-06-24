def chatbot():
    print("Hello! I am your chatbot.")
    print("Type 'bye' to end the conversation.")

    while True:
        message = input("You: ")

        if message.lower() == "hello":
            print("Chatbot: Hi there!")

        elif message.lower() == "how are you":
            print("Chatbot: I am doing well, thanks for asking!")

        elif message.lower() == "what is your name":
            print("Chatbot: My name is CodeAlpha Bot!")

        elif message.lower() == "who made you":
            print("Chatbot: Kavya created me during her internship project!")

        elif message.lower() == "thank you":
            print("Chatbot: You're welcome!")

        elif message.lower() == "good morning":
            print("Chatbot: Good morning! Have a great day!")

        elif message.lower() == "good night":
            print("Chatbot: Good night! Sleep well!")

        elif message.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
