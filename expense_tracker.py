'''
A console-based Expense Tracker program in Python that allows the user to record daily expenses and view
summaries like total spending. Use only the concepts learned till Chapter 6.
(loops, conditionals, lists, dictionaries, and basic input/output).
'''

expenseList = []   # list of all expenses

print("Welcome to Expense Tracker 💸:")

while True:
    print("\n======== MENU ========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    print("======================")

    choice = int(input("\nPlease Enter Your Choice: "))

    # 1. add expense
    if choice == 1:
        date = input("\nEnter the date of your expense (DD/MM/YYYY): ")
        category = input("Enter the category (Food/Travel/Shopping/Books): ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))

        dict_expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseList.append(dict_expense)
        print("\n✅ Expense added successfully!")

    # 2. view all expense
    elif choice == 2:
        if len(expenseList) == 0:
            print("\n⚠ No Expense Added!")
        else:
            print("\n============ All Expenses ============")
            count = 1
            for eachItem in expenseList:
                print(f"\n{count}. DATE: {eachItem["date"]} \n   CATEGORY: {eachItem["category"]} \n   DESCRIPTION: {eachItem["description"]} \n   AMOUNT: {eachItem["amount"]}")
                count += 1
    
    # 3. view total expenses
    elif choice == 3:
        total = 0
        for eachItem in expenseList:
            total += eachItem["amount"]
        print("\n💰 Total Expense:", total)

    # 4. exit
    elif choice == 4:
        print("\n👋 Thanks for connecting! Visit Again!\n")
        break

    # invalid choise
    else:
        print("\n❌ Invaid choice! Please try again!\n")
        break