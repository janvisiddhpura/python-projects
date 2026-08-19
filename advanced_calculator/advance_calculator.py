# Calculator with History
# future features:
# - multiple operation: logical, comparision, trigonometric, etc.
# - save calculation history to a file
# - load calculation history from a file
# - history, clear, exit
# modulus, exponentiation, floor division, etc.
# multinumber input, e.g. 1 + 2 + 3 + 4, can use eval() function

HISTORY_FILE = "history.txt"

def display_history():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No hisory found!")
        else:
            for line in reversed(lines):
                print(line.strip())
        file.close()

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
        print("Invalid input!\nPlease enter in the format: (e.g., 2 + 3)")
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
            print("Can't divide with Zero!")
            return
        result = operand1 / operand2
    elif operator == "%":
        result = operand1 % operand2
    else:
        print("Invalid operator!")
        return

    if int(result) == result:
        result = int(result)

    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print("\n------ 🧮 ADVANCE CALCULATOR ------\n")
    print("1. Calculate")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")
    while True:
        choice = int(input("\n🔢 Enter you choice(1-4): "))

        if choice == 1:
            user_input = input("Enter the equation (e.g., 2 + 4): ")
            calculator(user_input)
        elif choice == 2:
            display_history()
        elif choice == 3:
            clear_history()
        elif choice == 4:
            print("Goodbye!\n")
            break
        else:
            print("Please enter valid choice!")
main()