# ==============================================================================
# QUESTION 01: Prime Number Validator & Filter
# ==============================================================================
# INSTRUCTIONS:
# Implement the two functions below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

def is_prime(n):
    """
    Takes an integer n.
    Returns True if n is prime, False otherwise.
    Note: Numbers <= 1 are NOT prime. 2 is prime.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


def filter_primes(numbers):
    """
    Takes a list of integers 'numbers'.
    Returns a new list containing only the prime numbers in their original order.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {"desc": "Sample 1 (Mixed Numbers)", "input": [10, 3, 4, 7, 15, 19, 20], "expected": [3, 7, 19]},
        {"desc": "Sample 2 (No Primes)", "input": [4, 6, 8, 9], "expected": []},
        {"desc": "Edge Case (All Primes including 2)", "input": [2, 3, 5, 7, 11], "expected": [2, 3, 5, 7, 11]},
        {"desc": "Edge Case (0 and 1)", "input": [0, 1], "expected": []},
        {"desc": "Edge Case (Negative & Single Prime)", "input": [-5, -2, 0, 1, 2], "expected": [2]},
        {"desc": "Edge Case (Large Primes)", "input": [97, 100, 101], "expected": [97, 101]},
        {"desc": "Edge Case (Empty List)", "input": [], "expected": []}
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Prime Number Validator & Filter")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        actual = filter_primes(tc["input"])
        if actual == tc["expected"]:
            print(f"[{i}/{total}] PASS: {tc['desc']}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Input:    {tc['input']}")
            print(f"       -> Expected: {tc['expected']}")
            print(f"       -> Got:      {actual}")

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
