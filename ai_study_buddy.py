# a conversational AI assistant using Python’s core logic - string matching, functions, dictionaries, and loops.
# rule-based python AI chatbot
# an extra feature added by me: when user say sad: there will be another conversation comes

import datetime

name = input("\nWelcome, Please Enter your name: ")
present_hour = datetime.datetime.now().hour

if 5 <= present_hour <= 11:
    print("\n🌅 Good morning,", name, "!")
elif 11 <= present_hour <= 17:
    print("\n🔆 Good Afternoon,", name, "!")
elif 17 <= present_hour <= 20:
    print("\n🌆 Good Evening,", name, "!")
else:
    print("\n🌃 Good Night!")

print("\n🤖 Hello, Welcome to the ChatBot!")
print("You can ask me basic questions, Type 'bye' to exit from the bot. ")

# chatbot memory creation[dictionary of responses]
responses = {
    "hello": "Hi, welcome! How can I help you?",
    "how are you": 'I am very fine. Thank you.',
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer.",
    "happy": "Great to here that. Being Happy is the bestest thing in the world🌏",
    "sad": "I'm sorry you're feeling sad.",
    "what is functions": "Read chapter 7"
}

def get_response_bot(user_question):
    for each_key in responses:
        if each_key in user_question:
            if user_question == "sad":
                print("Bot:",responses[each_key], end="")
                res = input(" Do you want to talk about it? Press y/n: ").lower()
                if res == "y":
                    input("\n🎤 Please explain: ")
                    return "\033[1m"+"No worries! \nI believe you're very strong and True strength is getting back up and trying again every single time!"+"\033[0m"
                elif res == "n":
                    return "Not an issue! But you can one this beautiful thing... \n"+"\033[1m"+"The successful warrior is the average man, with laser-like focus."+"\033[0m"
            else:  
                return responses[each_key]        
    return "I am not able to tell that yet. Soon, I will learn it!"

# take user input
while True:
    user_input = input("\nYou: ")
    reply = get_response_bot(user_input.lower())
    print("Bot:", reply)
    if "bye" in user_input.lower():
        break