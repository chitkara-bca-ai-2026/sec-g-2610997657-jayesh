# Lab 18 - Mathematics Learning Tool
# Using recursive functions for factorial and fibonacci

# Recursive function for factorial
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function for fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
print("=" * 40)
print("   MATHEMATICS LEARNING TOOL")
print("=" * 40)

while True:
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        # Calculate factorial
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Error: Please enter a non-negative integer!")
        else:
            result = factorial(n)
            print(f"[RESULT] Factorial of {n} ({n}!) = {result}")

    elif choice == "2":
        # Generate fibonacci series
        terms = int(input("Enter number of terms to generate: "))
        if terms <= 0:
            print("Error: Please enter a positive integer!")
        else:
            series = [fibonacci(i) for i in range(terms)]
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    elif choice == "3":
        print("\nThank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
