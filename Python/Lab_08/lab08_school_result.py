# Lab 08 - School Result Processing
# Calculate grades and generate report card for a student

print("=====================================================")
print("              SCHOOL RESULT PROCESSING")
print("=====================================================")

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print()
print("--- Enter Marks for 5 Subjects (0-100) ---")

marks = []
failed = False  # flag to check if student failed any subject

for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))
    # Validate marks
    if m < 0 or m > 100:
        print("Invalid marks! Must be between 0 and 100.")
        exit()
    marks.append(m)
    if m < 40:
        failed = True

# Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100

# Determine grade and remark based on percentage
if failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remarks = "Outstanding"
elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remarks = "Excellent"
elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remarks = "Very Good"
elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remarks = "Good"
elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remarks = "Satisfactory"
elif percentage >= 40:
    result = "PASS"
    grade = "E"
    remarks = "Pass"
else:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"

# Display report card
print()
print("=====================================================")
print("              STUDENT REPORT CARD")
print("=====================================================")
print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll}")
print("  ---------------------------------------------------")
print(f"  Total Marks  : {total} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remarks}")
print("=====================================================")
