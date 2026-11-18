# ==============================================================================
# QUESTION 04: Supermarket Bill Generator with Coupon Codes
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

def generate_bill(cart_items, discount_code=""):
    """
    Takes:
      - cart_items: list of tuples (item_name, quantity, unit_price)
      - discount_code: str (e.g. "FESTIVE10", "SUPER20", or "")
    Returns tuple:
      (subtotal, discount_amount, net_total)
    Rules:
      - "FESTIVE10": 10% on subtotal
      - "SUPER20": 20% on subtotal IF subtotal >= 1000.0, else 0%
      - Others: 0%
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {
            "desc": "Festive 10% Discount",
            "items": [("Milk", 2, 40.0), ("Bread", 1, 30.0)],
            "code": "FESTIVE10",
            "expected": (110.0, 11.0, 99.0)
        },
        {
            "desc": "Super20 Qualified (>= 1000)",
            "items": [("Laptop", 1, 1200.0)],
            "code": "SUPER20",
            "expected": (1200.0, 240.0, 960.0)
        },
        {
            "desc": "Super20 Not Qualified (< 1000)",
            "items": [("Bag", 1, 500.0)],
            "code": "SUPER20",
            "expected": (500.0, 0.0, 500.0)
        },
        {
            "desc": "No Coupon Code",
            "items": [("Book", 3, 150.0)],
            "code": "",
            "expected": (450.0, 0.0, 450.0)
        },
        {
            "desc": "Empty Cart",
            "items": [],
            "code": "FESTIVE10",
            "expected": (0.0, 0.0, 0.0)
        }
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Supermarket Bill Generator")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        actual = generate_bill(tc["items"], tc["code"])
        is_match = (
            isinstance(actual, (tuple, list)) and len(actual) == 3 and
            abs(actual[0] - tc["expected"][0]) < 0.01 and
            abs(actual[1] - tc["expected"][1]) < 0.01 and
            abs(actual[2] - tc["expected"][2]) < 0.01
        )

        if is_match:
            print(f"[{i}/{total}] PASS: {tc['desc']} -> Subtotal={actual[0]:.2f}, Total={actual[2]:.2f}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Expected: Subtotal={tc['expected'][0]}, Disc={tc['expected'][1]}, Total={tc['expected'][2]}")
            print(f"       -> Got:      {actual}")

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
