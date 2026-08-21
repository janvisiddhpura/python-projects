"""
╔══════════════════════════════════════════════╗
║            🧮 Advanced Calculator            ║
╚══════════════════════════════════════════════╝
A console-based calculator that performs mathematical calculations 
while providing a menu-driven interface with calculation history, 
history management, and an option to exit the application.
"""

HISTORY_FILE = "history.txt"

def display_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("📭 No history found!")
            else:
                count = 1
                print("📜  History\n")
                for line in reversed(lines):                    
                    print(count, " → ", line.strip())
                    count += 1
            file.close()
    except:
        print("⛔ The file does not exist!\nPlease calculate something to add inside the file!")

def clear_history():
    # opens as write mode
    # which will overwrite the file and clear its previous content
    with open(HISTORY_FILE, "w") as file:
        print("History cleared!")
        file.close()

def save_to_history(equation, result):
    # open as append mode 
    # to add new history without overwriting the previous content
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + " = " + str(result) + "\n")
        file.close()

def calculator(user_input):
    tokens = user_input.split()
    if len(tokens) != 3:
        print("❌ Invalid input!\nPlease enter in the format: (e.g., 2 + 3)")
        return

    operand1 = float(tokens[0])
    operator = tokens[1]
    operand2 = float(tokens[2])

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("➗ Can't divide with Zero!")
            return
        result = operand1 / operand2
    elif operator == "%":
        result = operand1 % operand2
    else:
        print("Invalid operator!")
        return

    if int(result) == result:
        result = int(result)

    print("📊 Result: ", result)
    save_to_history(user_input, result)

def main():
    print("""
    ╔══════════════════════════════════════════════╗
    ║            🧮 Advanced Calculator            ║
    ╚══════════════════════════════════════════════╝
    """)
    print("1️⃣  ⚙️  Calculate")
    print("2️⃣  📜 View History")
    print("3️⃣  🗑️  Clear History")
    print("4️⃣  🚪 Exit")

    while True:

        choice = input("\nEnter you choice: ")

        if not choice.isdigit():
            print("\nPlease enter only a digit! 🔢")
            continue

        else:
            choice = int(choice)
            if choice == 1:
                user_input = input("\n📌 Enter the equation (e.g., 2 + 4): ")
                calculator(user_input)
            elif choice == 2:
                display_history()
            elif choice == 3:
                clear_history()
            elif choice == 4:
                print("\n👋 Thank you for using the Calculator!\n")
                break
            else:
                print("\n❌ Please enter valid choice!")
main()