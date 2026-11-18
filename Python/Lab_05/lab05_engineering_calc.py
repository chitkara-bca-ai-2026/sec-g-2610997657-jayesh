# Lab 05 - Engineering Calculation Tool
# Uses math module for power, sqrt, ceil, floor calculations

import math

print("=" * 40)
print("    ENGINEERING CALCULATION TOOL")
print("=" * 40)
print()

# Taking inputs
value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_val = float(input("Enter a decimal measurement: "))

# Calculations
power_result = pow(value, exponent)
sqrt_result = math.sqrt(value)
ceil_result = math.ceil(decimal_val)
floor_result = math.floor(decimal_val)

# Display results
print()
print("--- Results ---")
print(f"  Value          : {value}")
print(f"  Exponent       : {exponent}")
print(f"  Power (pow)    : {power_result}")
print(f"  Square Root (sqrt) : {sqrt_result:.4f}")
print(f"  Decimal Value  : {decimal_val}")
print(f"  Ceil Value     : {ceil_result}")
print(f"  Floor Value    : {floor_result}")
print("=" * 40)
