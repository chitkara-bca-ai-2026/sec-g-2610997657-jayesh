# Lab 06 - Shop Billing System
# Takes garment purchase details and generates a bill

print("=" * 42)
print("        CLOTHING STORE BILLING SYSTEM")
print("=" * 42)

# Taking inputs
customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# Calculate total
total_cost = price * quantity

# Display bill
print()
print("=" * 42)
print("                   BILL")
print("=" * 42)
print(f"  Customer Name  : {customer_name}")
print(f"  Garment Name   : {garment_name}")
print(f"  Price per Unit : Rs. {price}")
print(f"  Quantity       : {quantity}")
print(f"  Total Amount   : Rs. {total_cost}")
print("=" * 42)
