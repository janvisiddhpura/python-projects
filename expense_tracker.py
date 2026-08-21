'''
╔═══════════════════════════════════════════════════╗
║            💰 PERSONAL EXPENSE TRACKER            ║
╚═══════════════════════════════════════════════════╝
A console-based expense tracking application that allows 
users to add expenses, view recorded expenses, and calculate
total expenses.
'''

expenseList = []

while True:
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║            💰 PERSONAL EXPENSE TRACKER            ║
    ╚═══════════════════════════════════════════════════╝
    """)
    print("1️⃣  ➕ Add Expense")
    print("2️⃣  📋 View All Expenses")
    print("3️⃣  💵 View Total Expenses")
    print("4️⃣  🚪 Exit")

    choice = input("\nEnter Your Choice: ")

    if not choice.isdigit():
        print("\nPlease enter only a digit! 🔢")
        continue
    
    else:
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
                print("\n📋 All Expenses")
                count = 1
                for eachItem in expenseList:
                    print(f"\n{count}. DATE: {eachItem["date"]} \n   CATEGORY: {eachItem["category"]} \n   DESCRIPTION: {eachItem["description"]} \n   AMOUNT: {eachItem["amount"]}")
                    count += 1
        
        # 3. view total expenses
        elif choice == 3:
            total = 0
            for eachItem in expenseList:
                total += eachItem["amount"]
            print("\n📊 Total Expense:", total)

        # 4. exit
        elif choice == 4:
            print("\n👋 Thanks for connecting! Visit Again!\n")
            break

        # invalid choise
        else:
            print("\n❌ Invaid choice! Please try again!\n")
            break