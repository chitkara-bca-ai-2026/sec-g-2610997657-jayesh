# Lab 19 - Student Notes Management System
# File handling with notes.txt - write and read operations

import os

# Function to write notes to a file
def write_notes(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()
    print("\n--- Notes saved successfully to", filename, "---")

# Function to read notes from a file
def read_notes(filename):
    if os.path.exists(filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return content
    else:
        return "No notes found. File does not exist yet."

# Main menu loop
while True:
    print("\n===== Student Notes Management System =====")
    print("1. Write/Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        text = input("\nEnter your notes:\n")
        write_notes("notes.txt", text)

    elif choice == '2':
        print("\n--- Saved Notes ---")
        result = read_notes("notes.txt")
        print(result)

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
