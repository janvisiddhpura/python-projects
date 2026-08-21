''' 
╔════════════════════════════════════════════════════╗
║            🔑 Personal Password Manager            ║
╚════════════════════════════════════════════════════╝
A console-based password manager that program saves, views, and generates passwords.
Generated passwords are exactly 8 characters long and contain
uppercase letters, lowercase letters, numbers, and special symbols.
Instead of taking 'random' module, we'll take 'secrets' for better security purpose
'''

import secrets
import string

passwords = {}

# load existing file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":")
            passwords[website] = password
except:
    pass

# generate secure password
def generate_password():
    chars = (
        secrets.choice(string.ascii_uppercase) +
        secrets.choice(string.ascii_lowercase) +
        secrets.choice(string.digits) +
        secrets.choice("!@#$%^&*?") +
        "".join(
            secrets.choice(string.ascii_letters + string.digits + "!@#$%^&*?")
            for _ in range(4)
        )
    )
    chars = list(chars)
    secrets.SystemRandom().shuffle(chars)
    password = "".join(chars)
    return password

while True:
    print("""
    ╔════════════════════════════════════════════════════╗
    ║            🔑 Personal Password Manager            ║
    ╚════════════════════════════════════════════════════╝
    """)
    print("1️⃣  💾 Save Password")
    print("2️⃣  👁️  View Password")
    print("3️⃣  🔐 Generate Password")
    print("4️⃣  🚪 Exit")

    choice = int(input("\nEnter your choice: "))

    if not choice.isdigit():
        print("\nPlease enter only a digit! 🔢")
        continue
    else:
        choice = int(choice)

        # save password
        if choice == 1:
            website = input("\nEnter Website Name: ")
            password = input("Enter Password: ")
            passwords[website] = password
            with open("passwords.txt", "a") as file:
                file.write(f"{website}: {password}\n")
            print("\n✅ Password saved successfully!")

        # view password
        elif choice == 2:
            if not passwords:
                print("\n❌ No record found!")
            else:
                for website, password in passwords.items():
                    print("🌐 Website  : ", website)
                    print("🔑 Password :",password, "\n")

        # generate password
        elif choice == 3:
            print("Generated Password:", generate_password())

        # exit
        elif choice == 4:
            print("\n👋 Thanks for using Password Manager!")
            break

        # invalid
        else:
            print("\n🔢 Please choose a valid option!")