# Lab 24 - Student Result Analysis System
# Read and analyze students_data.csv using csv module

import csv

# Function to read and display all students
def read_all_students(filename):
    file = open(filename, 'r')
    reader = csv.DictReader(file)

    print("\n===== All Student Records =====")
    print(f"{'RollNo':<10}{'Name':<10}{'Subject':<10}{'Marks':<10}")
    print("-" * 40)

    count = 0
    for row in reader:
        print(f"{row['RollNo']:<10}{row['Name']:<10}{row['Subject']:<10}{row['Marks']:<10}")
        count += 1

    file.close()
    print("-" * 40)
    print(f"Total Students: {count}")

# Function to filter students above a threshold
def filter_students_above_threshold(filename, threshold=50):
    file = open(filename, 'r')
    reader = csv.DictReader(file)

    print(f"\n===== Students with Marks > {threshold} =====")
    print(f"{'RollNo':<10}{'Name':<10}{'Subject':<10}{'Marks':<10}")
    print("-" * 40)

    count = 0
    for row in reader:
        if int(row['Marks']) > threshold:
            print(f"{row['RollNo']:<10}{row['Name']:<10}{row['Subject']:<10}{row['Marks']:<10}")
            count += 1

    file.close()
    print("-" * 40)
    print(f"Students above {threshold}: {count}")

# Main menu loop
while True:
    print("\n===== Student Result Analysis System =====")
    print("1. Display All Students from CSV")
    print("2. Filter Students (Marks > 50)")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        read_all_students("students_data.csv")

    elif choice == '2':
        filter_students_above_threshold("students_data.csv")

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
