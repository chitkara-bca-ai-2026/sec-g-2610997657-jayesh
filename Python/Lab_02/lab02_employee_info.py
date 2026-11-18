# Lab 02 - Employee Information System
# Takes employee details, shows data types, and displays formatted info

# Taking inputs and showing data types
name = input("Enter Employee Name: ")
print(f"  Data type: {type(name)}")

emp_id = int(input("Enter Employee ID: "))
print(f"  Data type: {type(emp_id)}")

salary = float(input("Enter Salary: "))
print(f"  Data type: {type(salary)}")

department = input("Enter Department: ")
print(f"  Data type: {type(department)}")

active_input = input("Is the employee active? (yes/no): ")
is_active = active_input.lower() == "yes"
print(f"  Data type: {type(is_active)}")

# Display employee details
print()
print("--- Employee Details ---")
print(f"Name       : {name}")
print(f"ID         : {emp_id}")
print(f"Salary     : {salary}")
print(f"Department : {department}")
print(f"Active     : {is_active}")
