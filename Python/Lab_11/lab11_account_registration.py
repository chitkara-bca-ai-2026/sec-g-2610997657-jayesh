# Lab 11 - Online Account Registration
# Validate password based on certain rules

username = input("Enter your username: ")
password = input("Enter your password: ")

print("==========================================")
print("  PASSWORD VALIDATION REPORT")
print("==========================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print()
print("--- Validation Rules ---")

# Rule 1: Minimum 8 characters
if len(password) >= 8:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
    rule1 = True
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")
    rule1 = False

# Rule 2: At least one digit
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if has_digit:
    print("[PASS] At least one digit")
    rule2 = True
else:
    print("[FAIL] At least one digit")
    rule2 = False

# Rule 3: At least one uppercase letter
has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True
        break

if has_upper:
    print("[PASS] At least one uppercase letter")
    rule3 = True
else:
    print("[FAIL] At least one uppercase letter")
    rule3 = False

# Final verdict
print()
print("--- Result ---")

if rule1 and rule2 and rule3:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
    print("Please fix the above issues and try again.")

print()
print("==========================================")
