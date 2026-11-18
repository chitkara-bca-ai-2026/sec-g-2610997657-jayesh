# Lab 03 - Student Record Display
# Takes student info and displays it with formatting

print("=" * 40)
print("        STUDENT RECORD DISPLAY")
print("=" * 40)
print()

# Taking inputs
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

print()
print("-" * 40)

# Display student details
print()
print("Student Details:")
print(f"  Name  : {name}")
print(f"  Age   : {age}")
print(f"  Marks : {marks}")
print("-" * 40)
