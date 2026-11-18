# Lab 07 - Calendar Verification System
# Check if a given year is a leap year or common year

print("==========================================")
print("    CALENDAR VERIFICATION SYSTEM")
print("==========================================")

year = int(input("Enter year: "))

# Validate year
if year <= 0:
    print("Invalid year! Please enter a positive number.")
else:
    # Check leap year rules
    if year % 400 == 0:
        # Century year divisible by 400 -> leap year
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_feb = 29
        reason = "Century year divisible by 400"
    elif year % 100 == 0:
        # Century year not divisible by 400 -> common year
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_feb = 28
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        # Non-century year divisible by 4 -> leap year
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_feb = 29
        reason = "Divisible by 4 and not a century year"
    else:
        # Not divisible by 4 -> common year
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_feb = 28
        reason = "Not divisible by 4"

    # Display results
    print()
    print("------------------------------------------")
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days_in_year} days")
    print(f"Days in February: {days_in_feb} days")
    print(f"Reason: {reason}")
    print("------------------------------------------")
