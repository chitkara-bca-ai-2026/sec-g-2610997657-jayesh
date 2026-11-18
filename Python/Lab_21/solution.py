# Lab 21 - Document Statistics Tool
# Analyze document.txt for lines, words, and characters

# Function to calculate document statistics
def get_document_statistics(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        words = line.split()
        word_count += len(words)
        char_count += len(line)

    return (line_count, word_count, char_count)

# Function to display document with line numbers
def display_document(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    print("\n--- Document Content ---")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}", end='')
    print()

# Main menu loop
while True:
    print("\n===== Document Statistics Tool =====")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        stats = get_document_statistics("document.txt")
        print("\n--- Document Statistics Report ---")
        print(f"Total Lines      : {stats[0]}")
        print(f"Total Words      : {stats[1]}")
        print(f"Total Characters : {stats[2]}")
        print("---------------------------------")

    elif choice == '2':
        display_document("document.txt")

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
