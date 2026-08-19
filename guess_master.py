# A text-based word guessing game - GuessMaster

import random
import sys

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain", "diameter"]

attempts = 0
max_hints = 0
hints = {}
hint_count = 0
failed_attempts = 0
found_new_char = False

# take user input with current state
def take_user_input(current_state):
    secret = ""
    global max_hints
    while True:
        choice = input("\nEnter your choice: ")
        if not choice.isdigit():
            print("\nPlease enter only a digit! 🔢")
            continue
        else:
            choice = int(choice)
            if choice == 1:
                if current_state == "init":
                    secret = random.choice(easy_words).lower()
                    max_hints = len(secret)
                    return choice, secret
                elif current_state == "hint":
                    return choice
            elif choice == 2:
                if current_state == "init":
                    secret = random.choice(medium_words).lower()
                    max_hints = len(secret)
                    return choice, secret
                elif current_state == "hint":
                    return choice
            elif choice == 3:
                if current_state == "init":
                    secret = random.choice(hard_words).lower()
                    max_hints = len(secret)
                    return choice, secret
                elif current_state == "hint":
                    print("\n🎮 Please choose a valid option!!")
                    continue
            else:
                print("\n🎮 Please choose a valid option!")
                if current_state == "init":
                    print("Default level is easy!")
                    secret = random.choice(easy_words).lower()
                    max_hints = len(secret)
                    return choice, secret

# place the hint from dict
def get_secret_hint(guess, hint):
    global hint_count, hints
    for i in range(len(secret)):
        if guess[i] == secret[i] and guess[i] not in hints.values():
            hint += guess[i]
            hints[i] = guess[i]
            hint_count += 1
        else:
            hint += " _ "
    return hint

# checks the entered user guess
def validate_guess():
    global max_hints, attempts, hints
    while True:
        if attempts >= max_hints:
            guess = input("\nGuess (or type 'quit' to exit): ")        
        else:
            guess = input("\nGuess: ")
        if not guess.isalpha():
            print("\n🆎 Please enter a single word using alphabets only!")
            continue
        elif guess.isspace():
            print("\n🆎 Please enter only single word!")
            continue
        if guess == "quit":
            print("\n👋 No worries! Thanks for playing.")
            print(f"🔐 The secret word was: \033[1m{secret}\033[0m\n")
            sys.exit()
        elif len(guess) > len(secret):
            print(f"\n📏 Whoa! That's too long! Please enter exactly {len(secret)} characters.")
            continue
        elif len(guess) < len(secret):
            print(f"\n📏 Oops! That's too short! Please enter exactly {len(secret)} characters.")
            continue
        else:
            guess = guess.lower()            
            return guess

# foundation of the secret
def form_secret():    
    global attempts, hint_count, hints, failed_attempts, found_new_char
    while True:
        hint = ""
        found_new_char = False
        attempts += 1       
        guess = validate_guess()    
        if guess == secret:
            print(f"\n🎉 Congrats! You guessed it in \033[1m{attempts}\033[0m attempts!\n")
            break        
        elif len(guess) == len(secret):
            if attempts <= 2:
                hint = ""
                print("Hint: ", get_secret_hint(guess, hint))
            elif attempts >= 3:
                hint = ""
                if hint_count == 0:
                    print("\n💡 Need a little help?")
                    print("1️⃣  Yes, give me a hint!")
                    print("2️⃣  No, I'll try again!")
                    ask = take_user_input("hint")
                    if ask == 1:
                        # check for more occurances of characters in a word
                        hint_char = random.choice(secret).lower()
                        hint_index = secret.find(hint_char)
                        hints[hint_index] = hint_char
                        for i in range(len(secret)):
                            if i == hint_index:
                                hint += hint_char
                                hint_count += 1
                                found_new_char = True
                                failed_attempts = 0
                            else:
                                hint += " _ "                    
                        print("Hint: ", hint)
                        continue
                    elif ask == 2:
                        break     
                elif hint_count > 0:
                    hint = ""
                    for i in range(len(secret)):
                        if guess[i] == secret[i]:                            
                            if i not in hints.keys():
                                found_new_char = True
                                failed_attempts = 0
                    # match in entire guess
                    if found_new_char:
                        failed_attempts = 0    
                    else:
                        failed_attempts += 1
                        found_new_char = False
                    for i in range(len(secret)):
                        if guess[i] == secret[i] and i not in hints.keys():
                            hints[i] = guess[i]
                            hint_count += 1
                    for i in range(len(secret)):                    
                        if secret[i] == hints.get(i):
                            hint += hints.get(i)              
                        else:
                            hint += " _ "
                    # hints after 2 incorrect attempts
                    if failed_attempts == 2 and (hint_count < len(secret) - 2 and found_new_char == False):
                        failed_attempts = 0
                        hint = ""
                        for i in range(len(secret)):
                            if guess[i] == secret[i] and i not in hints.keys():
                                hints[i] = guess[i]
                                hint_count += 1                        
                        print("\n💡 Need more help?")
                        print("1️⃣  Yes, give me a hint!")
                        print("2️⃣  No, I'll try again!")
                        ask = take_user_input("hint")
                        if ask == 1:
                            # check for more occurances of characters in a word
                            available_indexes = [i for i in range(len(secret)) if i not in hints]
                            hint_index = random.choice(available_indexes)
                            hint_char = secret[hint_index]
                            hints[hint_index] = hint_char
                            hint_count += 1
                            for i in range(len(secret)):                    
                                if secret[i] == hints.get(i):
                                    hint += hints.get(i)              
                                else:
                                    hint += " _ "
                            print("Hint: ", hint)
                            continue
                        elif ask == 2:
                            break
                    # reached at the max hints
                    elif hint_count == max_hints and len(hints) != len(secret):
                        print("\n💡 \033[1mYou've used all the available hints!\033[0m")
                        print("🎯 Do you want to keep guessing or quit the game?")
                        print("1️⃣  Continue guessing")
                        print("2️⃣  Quit")
                        ask = take_user_input("hint")
                        if ask == 1:
                            continue
                        elif ask == 2:
                            print("\n👋 No worries! Thanks for playing.")
                            print(f"🔐 The secret word was: {secret}")
                            break
                    # already reached at the secret
                    if len(hints.items()) == len(secret):
                        if all(char in hints.values() for char in secret) and guess != hint:
                            print(f"\n🧩 Well Done! You've pieced together the entire word: \033[1m{secret}\033[0m")
                            if hint == secret:
                                print(f"\n🎉 Congrats! You guessed it in \033[1m{attempts}\033[0m attempts!\n")
                                break
                    else:
                        print("Hint: ", hint)

# main base starts here
print("\n----- 🎯 Word Guessing Game -----\n")
print("📊 The Difficulty Levels:")
print("1️⃣  Easy")
print("2️⃣  Medium")
print("3️⃣  Hard")

choice, secret = (take_user_input("init"))
form_secret()