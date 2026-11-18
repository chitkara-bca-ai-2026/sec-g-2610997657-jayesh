# Lab 04 - Data Conversion Utility
# Demonstrates type casting and displays an invoice

print("=" * 48)
print("            DATA CONVERSION UTILITY")
print("=" * 48)

# Taking inputs with type conversion
product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

# Calculations
total_price = price * quantity
amount_str = str(total_price)

# Type casting summary
print()
print("-" * 48)
print("              TYPE CASTING SUMMARY")
print("-" * 48)
print("  Variable        Value           Python Type")
print("-" * 48)
print(f"  product_name    {product_name}          {type(product_name)}")
print(f"  price           {price}         {type(price)}")
print(f"  quantity         {quantity}              {type(quantity)}")
print(f"  total_price     {total_price}         {type(total_price)}")
print(f"  amount_str      {amount_str}         {type(amount_str)}")
print("-" * 48)

# Invoice
print()
print("-" * 48)
print("                  TAX INVOICE")
print("-" * 48)
print(f"  Product Name  : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print("  " + "-" * 41)
print(f"  Invoice Total  : Rs. {total_price}")
print("=" * 48)
