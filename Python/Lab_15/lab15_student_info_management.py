# Lab 15 - Student Information Management System
# Using nested dictionaries to manage student records

# Nested dictionary with roll number as key
students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
}

print("=" * 50)
print("   STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    print("\n--- Menu ---")
    print("1. View All Students")
    print("2. Search by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        # View all students
        print("\n--- All Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Semester: {info['Semester']} | Marks: {info['Marks']}")
        print(f"\nTotal students: {len(students)}")

    elif choice == "2":
        # Search by roll number using .get()
        roll = input("Enter roll number to search: ")
        student = students.get(roll)
        if student:
            print(f"\n--- Student Found ---")
            print(f"Roll No: {roll}")
            print(f"Name: {student['Name']}")
            print(f"Branch: {student['Branch']}")
            print(f"Semester: {student['Semester']}")
            print(f"Marks: {student['Marks']}")
        else:
            print(f"Error: Student with roll number '{roll}' not found!")

    elif choice == "3":
        # Register new student - check for duplicates
        roll = input("Enter roll number: ")
        if roll in students:
            print(f"Error: Roll number '{roll}' already exists!")
        else:
            name = input("Enter name: ")
            branch = input("Enter branch: ")
            semester = input("Enter semester: ")
            marks = []
            for i in range(3):
                mark = int(input(f"Enter marks for subject {i + 1}: "))
                marks.append(mark)
            students[roll] = {"Name": name, "Branch": branch, "Semester": semester, "Marks": marks}
            print(f"Student '{name}' registered successfully!")

    elif choice == "4":
        # Update student details
        roll = input("Enter roll number to update: ")
        if roll in students:
            print("What do you want to update?")
            print("1. Branch")
            print("2. Semester")
            update_choice = input("Enter choice (1-2): ")
            if update_choice == "1":
                new_branch = input("Enter new branch: ")
                students[roll]["Branch"] = new_branch
                print("Branch updated successfully!")
            elif update_choice == "2":
                new_semester = input("Enter new semester: ")
                students[roll]["Semester"] = new_semester
                print("Semester updated successfully!")
            else:
                print("Invalid choice!")
        else:
            print(f"Error: Student with roll number '{roll}' not found!")

    elif choice == "5":
        # View academic performance
        roll = input("Enter roll number: ")
        student = students.get(roll)
        if student:
            marks = student["Marks"]
            total = sum(marks)
            average = total / len(marks)
            percentage = (total / 300) * 100

            print(f"\n--- Academic Performance ---")
            print(f"Name: {student['Name']}")
            print(f"Marks: {marks}")
            print(f"Total: {total}/300")
            print(f"Average: {average:.2f}")
            print(f"Percentage: {percentage:.2f}%")

            # Pass/fail check (>=40% to pass)
            if percentage >= 40:
                print("Status: PASS")
            else:
                print("Status: FAIL")
        else:
            print(f"Error: Student with roll number '{roll}' not found!")

    elif choice == "6":
        # Delete student record using .pop()
        roll = input("Enter roll number to delete: ")
        removed = students.pop(roll, None)
        if removed:
            print(f"Student '{removed['Name']}' (Roll No: {roll}) has been deleted.")
        else:
            print(f"Error: Student with roll number '{roll}' not found!")

    elif choice == "7":
        print("\nThank you for using the Student Information Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
