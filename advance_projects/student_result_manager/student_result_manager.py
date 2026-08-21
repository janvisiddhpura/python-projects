'''
╔═══════════════════════════════════════════════════════════╗
║            🎓 Student Result Management System            ║
╚═══════════════════════════════════════════════════════════╝
A console-based system that manages student records and results.
It allows the user to add, view, search, update students,
and check their examination results.
'''

students = {}

while True:
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║            🎓 Student Result Management System            ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    print("1️⃣  ➕ Add Student")
    print("2️⃣  📋 View Students")
    print("3️⃣  📊 Check Result")
    print("4️⃣  📝 Update Student")
    print("5️⃣  🔍 Search Student")
    print("6️⃣  🚪 Exit")

    choice = input("\nEnter your choice: ")
    if not choice.isdigit():
        print("\nPlease enter only a digit! 🔢")
        continue
    else:
        choice = int(choice)
        # add student
        if choice == 1:
            roll_no = input("\nEnter Roll Number: ")
            name = input("\nEnter Student Name: ")            
            marks = int(input("Enter Marks (out of 100): "))
            students[roll_no] = {"name": name, "marks": marks}
            print(f"\n✅ {name} added successfully!")
        # view students
        elif choice == 2:
            if not students:
                print("\n📪 No student record found!")
            else:
                print("\n       📋 Student List       ")
                print("=" * 30)
                for roll_no, data in students.items():
                    print(f"Roll no.| {roll_no}\nName    | {data["name"]}\nMarks   | {data["marks"]}\n")                    
        # check result
        elif choice == 3:
            roll_no = input("Enter Roll Number: ")               
            if roll_no in students:
                print(f"\n🔠 Name : {students[roll_no]["name"]}")
                print(f"📊 Marks: {students[roll_no]["marks"]}")
                if marks >= 35:
                    print("\n✅ PASS - Congratulations!")
                else:
                    print("\n❌ FAIL - Better luck next time!")
            else:
                print("\n🔍 No student record found!")
        # update student
        elif choice == 4:
            roll_no = input("\nEnter Roll Number: ") 
            if roll_no in students:
                name = input("Enter New Name: ")
                marks = float(input("Enter New Marks: "))
                students[roll_no] = {"name": name, "marks": marks}
                print("\n📝 Student record updated successfully!")
            else:
                print("\n⛔ No record found!")
        # search student
        elif choice == 5:
            roll_no = input("\nEnter Roll Number: ")
            if roll_no in students:
                data = students[roll_no]
                print("\n📃 Student Details: ")
                print(f"🔠 Name : {students[roll_no]["name"]}")
                print(f"📊 Marks: {students[roll_no]["marks"]}")
        # exit
        elif choice == 6:
            print("\n👋 Thank you for using Student Result Management System!\n")
            break
        else:
            print("\n🔢 Please choose a valid option!")