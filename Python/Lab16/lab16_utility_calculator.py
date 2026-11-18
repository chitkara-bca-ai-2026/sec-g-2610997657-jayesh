# Lab 16 - Utility Calculator
# Using functions for mathematical operations with history tracking

# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    # Return int if no decimal part, else float
    if n == int(n):
        return int(n)
    else:
        return float(n)

# History list to store calculation records
history = []

print("=" * 40)
print("   UTILITY CALCULATOR")
print("=" * 40)

while True:
    print("\n--- Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus/Remainder")
    print("6. Power/Exponentiation")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        a = format_number(a)
        b = format_number(b)

        if choice == "1":
            result = add(a, b)
            result = format_number(result)
            print(f"[RESULT] {a} + {b} = {result}")
            history.append(f"{a} + {b} = {result}")

        elif choice == "2":
            result = subtract(a, b)
            result = format_number(result)
            print(f"[RESULT] {a} - {b} = {result}")
            history.append(f"{a} - {b} = {result}")

        elif choice == "3":
            result = multiply(a, b)
            result = format_number(result)
            print(f"[RESULT] {a} * {b} = {result}")
            history.append(f"{a} * {b} = {result}")

        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Division by zero is not allowed!")
            else:
                result = format_number(result)
                print(f"[RESULT] {a} / {b} = {result}")
                history.append(f"{a} / {b} = {result}")

        elif choice == "5":
            result = modulus(a, b)
            if result is None:
                print("Error: Modulus by zero is not allowed!")
            else:
                result = format_number(result)
                print(f"[RESULT] {a} % {b} = {result}")
                history.append(f"{a} % {b} = {result}")

    elif choice == "6":
        base = float(input("Enter base number: "))
        base = format_number(base)
        exp_input = input("Enter exponent (press Enter for default square): ")
        if exp_input == "":
            result = power(base)
            exp_val = 2
        else:
            exp_val = float(exp_input)
            exp_val = format_number(exp_val)
            result = power(base, exp_val)
        result = format_number(result)
        print(f"[RESULT] {base} ^ {exp_val} = {result}")
        history.append(f"{base} ^ {exp_val} = {result}")

    elif choice == "7":
        # View calculation history
        print("\n--- Calculation History ---")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")

    elif choice == "8":
        print("\nThank you for using the Utility Calculator. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
