# Lab 20 - Daily Log Book
# File handling with daily_log.txt using append mode

# Function to add a new log entry
def append_entry(filename, entry):
    file = open(filename, 'a')
    file.write(entry + '\n')
    file.close()
    print("\n--- Log entry added successfully! ---")

# Function to display all log entries
def display_log(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    print("\n========== Daily Log Book ==========")
    count = 0
    for line in lines:
        line = line.strip()
        if line:  # skip empty lines
            count += 1
            print(f"  {count}. {line}")
    print("====================================")
    print(f"Total Log Entries: {count}")

# Main menu loop
while True:
    print("\n===== Daily Log Book System =====")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        entry = input("\nEnter log message: ")
        append_entry("daily_log.txt", entry)

    elif choice == '2':
        display_log("daily_log.txt")

    elif choice == '3':
        print("\nExiting... Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
