# a conversational AI assistant using Python’s core logic - string matching, functions, dictionaries, and loops.
# rule-based python AI chatbot
# an extra feature added by me: when user say sad: there will be another conversation comes

import datetime
import time 

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
    "what is functions?": "Read chapter 7",
    "what is string?": "A string is a data type in Python that stores a sequence of characters — letters, numbers, or symbols — enclosed in single (' '), double (" "), or triple (''' ''') quotes.",
    "what is conditional statement?": "Conditional statements allow your program to make decisions - run different parts of code based on certain conditions.",
    "what is list?": "A list is a built-in data type that can store multiple values in a single variable. Lists are mutable (can be changed) and can store different data types.",
    "what is tuples?": "A tuple is a built-in data type that stores multiple values like a list, but it is immutable (cannot be changed after creation).",
    "what is dictionary": "A dictionary is a built-in data type in Python used to store data in key-value pairs.",
    "what is set?": "A set is a collection of unordered and unique items. Sets automatically remove duplicate elements and are written using curly braces { }."
}

def get_response_bot(user_question):
    print("Thinking...", end="", flush=True)
    time.sleep(1)
    print("\r" + " " * len("Thinking...") + "\r", end="", flush=True)
    for each_key in responses:
        if each_key in user_question:
            if user_question == "sad":
                print("Bot:", responses[each_key], end="")
                res = input(" Do you want to talk about it? Press y/n: ").lower()
                if res == "y":
                    input("\n🎤 Please explain: ")
                    return "\033[1m" + "No worries! \nI believe you're very strong and True strength is getting back up and trying again every single time!" + "\033[0m"
                elif res == "n":
                    return "Not an issue! But you can one this beautiful thing... \n" + "\033[1m" + "The successful warrior is the average man, with laser-like focus." + "\033[0m"
            else:
                return responses[each_key]
    return "I am not able to tell that yet. Soon, I will learn it!"

# take user input
while True:
    user_input = input("\nYou: ").strip().lower()
    if user_input == "bye":
        print("Bot: Bye! See you soon!🤝\n")
        break

    reply = get_response_bot(user_input)
    print("Bot:", reply)