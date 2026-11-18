# Lab 23 - File Handling Tool
# Manage student marks in student_marks.txt

import os

# Function to store a student record
def store_student(filename, name, marks):
    file = open(filename, 'a')
    file.write(f"{name},{marks}\n")
    file.close()
    print(f"\n--- Record for {name} saved successfully! ---")

# Function to display all records and calculate class average
def display_and_calculate_average(filename):
    if not os.path.exists(filename):
        print("\nNo records found. File does not exist.")
        return

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    print("\n===== Student Marks Record =====")
    print(f"{'Name':<15}{'Marks':<10}")
    print("-" * 25)

    total = 0
    count = 0
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(',')
            name = parts[0]
            marks = int(parts[1])
            total += marks
            count += 1
            print(f"{name:<15}{marks:<10}")

    if count > 0:
        average = total / count
        print("-" * 25)
        print(f"Class Average: {average:.2f}")
    print("================================")

# Main menu loop
while True:
    print("\n===== File Handling Tool =====")
    print("1. Display Records & Class Average")
    print("2. Add & Store Student Marks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        display_and_calculate_average("student_marks.txt")

    elif choice == '2':
        name = input("\nEnter student name: ")
        marks = int(input("Enter marks (0-100): "))
        # Validate marks
        if 0 <= marks <= 100:
            store_student("student_marks.txt", name, marks)
        else:
            print("\nInvalid marks! Please enter a value between 0 and 100.")

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
