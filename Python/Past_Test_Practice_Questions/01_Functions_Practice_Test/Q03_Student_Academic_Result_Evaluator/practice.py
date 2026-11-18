# ==============================================================================
# QUESTION 03: Student Academic Result Evaluator
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

def evaluate_student(record):
    """
    Takes a dictionary: {"name": str, "marks": list_of_ints}
    Returns a dictionary:
    {
        "name": str,
        "total": int,
        "average": float,
        "status": str ("DISTINCTION" | "FIRST CLASS" | "SECOND CLASS" | "FAIL")
    }
    Rules:
      - Any mark < 40 => "FAIL"
      - Else:
          avg >= 75.0 => "DISTINCTION"
          avg >= 60.0 => "FIRST CLASS"
          else        => "SECOND CLASS"
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {
            "desc": "Distinction (> 75)",
            "input": {"name": "Aman", "marks": [85, 90, 80]},
            "expected_total": 255, "expected_avg": 85.0, "expected_status": "DISTINCTION"
        },
        {
            "desc": "Fail (< 40 in one subject)",
            "input": {"name": "Rohan", "marks": [80, 35, 90]},
            "expected_total": 205, "expected_avg": 68.333, "expected_status": "FAIL"
        },
        {
            "desc": "First Class (60 - 74.9)",
            "input": {"name": "Priya", "marks": [60, 65, 70]},
            "expected_total": 195, "expected_avg": 65.0, "expected_status": "FIRST CLASS"
        },
        {
            "desc": "Second Class (< 60)",
            "input": {"name": "Amit", "marks": [45, 50, 55]},
            "expected_total": 150, "expected_avg": 50.0, "expected_status": "SECOND CLASS"
        },
        {
            "desc": "Boundary 75.0 Distinction",
            "input": {"name": "Sneha", "marks": [75, 75, 75]},
            "expected_total": 225, "expected_avg": 75.0, "expected_status": "DISTINCTION"
        }
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Student Academic Result Evaluator")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        actual = evaluate_student(tc["input"])
        is_correct = (
            isinstance(actual, dict) and
            actual.get("name") == tc["input"]["name"] and
            actual.get("total") == tc["expected_total"] and
            abs(actual.get("average", 0.0) - tc["expected_avg"]) < 0.01 and
            actual.get("status") == tc["expected_status"]
        )

        if is_correct:
            print(f"[{i}/{total}] PASS: {tc['desc']} -> Status: {actual.get('status')}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Input:    {tc['input']}")
            print(f"       -> Expected: Total={tc['expected_total']}, Avg={tc['expected_avg']:.2f}, Status={tc['expected_status']}")
            print(f"       -> Got:      {actual}")

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
