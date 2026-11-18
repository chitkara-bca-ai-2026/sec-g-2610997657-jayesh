# Lab 17 - Student Records Handling
# Using dictionaries and functions to manage student records

# Pre-populated student records
students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]}
}

# Function to calculate total and average from marks
def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return (total, average)

# Function to display a single student record
def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}")

# Function to add a new student
def add_student(records, roll, name, marks):
    if roll in records:
        print(f"Error: Roll number '{roll}' already exists!")
        return False
    records[roll] = {"Name": name, "Marks": marks}
    print(f"Student '{name}' added successfully!")
    return True

# Main program
print("=" * 50)
print("   STUDENT RECORDS HANDLING SYSTEM")
print("=" * 50)

while True:
    print("\n--- Menu ---")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        # Display all students
        print("\n--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"\nTotal students: {len(students)}")

    elif choice == "2":
        # Add new student
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = []
        for i in range(3):
            mark = int(input(f"Enter marks for subject {i + 1}: "))
            marks.append(mark)
        add_student(students, roll, name, marks)

    elif choice == "3":
        # Search student by roll number
        roll = input("Enter roll number to search: ")
        if roll in students:
            print("\n--- Student Found ---")
            display_student(roll, students[roll])
        else:
            print(f"Error: Student with roll number '{roll}' not found!")

    elif choice == "4":
        print("\nThank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
