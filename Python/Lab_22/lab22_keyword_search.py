# Lab 22 - Keyword Search Utility
# Search for keywords in report.txt (case-insensitive)

# Function to search for a keyword in the file
def search_keyword(filename, keyword):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    print(f"\n--- Searching for '{keyword}' ---")
    count = 0
    for i, line in enumerate(lines, 1):
        if keyword.lower() in line.lower():
            count += 1
            print(f"  Line {i}: {line.strip()}")

    print(f"\nTotal occurrences found: {count}")

# Function to display the full document
def display_document(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    print("\n--- Full Document ---")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Main menu loop
while True:
    print("\n===== Keyword Search Utility =====")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        keyword = input("\nEnter keyword to search: ")
        search_keyword("report.txt", keyword)

    elif choice == '2':
        display_document("report.txt")

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
