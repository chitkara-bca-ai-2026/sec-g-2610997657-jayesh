# ==============================================================================
# QUESTION 05: Recursive Sum of Digits & Digital Root
# ==============================================================================
# INSTRUCTIONS:
# Implement the two recursive functions below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

def sum_of_digits(n):
    """
    Recursively computes the sum of digits of non-negative integer n.
    Must NOT convert to string.
    """
    # --- WRITE YOUR RECURSIVE CODE HERE ---
    pass


def digital_root(n):
    """
    Recursively computes the single-digit digital root of non-negative integer n.
    """
    # --- WRITE YOUR RECURSIVE CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {"desc": "Standard 4-Digit Number", "n": 9875, "exp_sum": 29, "exp_root": 2},
        {"desc": "Single Digit", "n": 7, "exp_sum": 7, "exp_root": 7},
        {"desc": "All 9s", "n": 999, "exp_sum": 27, "exp_root": 9},
        {"desc": "Power of 10", "n": 1000, "exp_sum": 1, "exp_root": 1},
        {"desc": "Two Digits", "n": 45, "exp_sum": 9, "exp_root": 9},
        {"desc": "Zero", "n": 0, "exp_sum": 0, "exp_root": 0}
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Recursive Sum of Digits & Digital Root")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        actual_sum = sum_of_digits(tc["n"])
        actual_root = digital_root(tc["n"])

        is_correct = (actual_sum == tc["exp_sum"] and actual_root == tc["exp_root"])

        if is_correct:
            print(f"[{i}/{total}] PASS: {tc['desc']} (n={tc['n']}) -> Sum={actual_sum}, Root={actual_root}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']} (n={tc['n']})")
            print(f"       -> Expected: Sum={tc['exp_sum']}, Root={tc['exp_root']}")
            print(f"       -> Got:      Sum={actual_sum}, Root={actual_root}")

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
