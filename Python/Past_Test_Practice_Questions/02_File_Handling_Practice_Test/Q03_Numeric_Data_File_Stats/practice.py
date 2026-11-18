# ==============================================================================
# QUESTION 03: Numeric Data File Reader & Stats
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

import os

def calculate_file_stats(filename):
    """
    Reads integer scores (one per line) from 'filename'.
    Returns tuple: (count, total, average)
    If file has no numbers, returns: (0, 0, 0.0)
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {
            "desc": "Standard 5 Scores",
            "file": "test_scores_1.txt",
            "content": "85\n90\n75\n90\n60\n",
            "expected": (5, 400, 80.0)
        },
        {
            "desc": "Empty File Edge Case",
            "file": "test_scores_empty.txt",
            "content": "",
            "expected": (0, 0, 0.0)
        },
        {
            "desc": "Single Score",
            "file": "test_scores_single.txt",
            "content": "100\n",
            "expected": (1, 100, 100.0)
        },
        {
            "desc": "3 Scores with Trailing Spaces",
            "file": "test_scores_spaces.txt",
            "content": " 10 \n 20 \n 30 \n",
            "expected": (3, 60, 20.0)
        }
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Numeric Data File Reader & Stats")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        filename = tc["file"]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(tc["content"])

        actual = calculate_file_stats(filename)

        is_match = (
            isinstance(actual, (tuple, list)) and len(actual) == 3 and
            actual[0] == tc["expected"][0] and
            actual[1] == tc["expected"][1] and
            abs(actual[2] - tc["expected"][2]) < 0.01
        )

        if is_match:
            print(f"[{i}/{total}] PASS: {tc['desc']} -> Count={actual[0]}, Sum={actual[1]}, Avg={actual[2]:.2f}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Expected: Count={tc['expected'][0]}, Sum={tc['expected'][1]}, Avg={tc['expected'][2]}")
            print(f"       -> Got:      {actual}")

        if os.path.exists(filename):
            os.remove(filename)

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
