# ==============================================================================
# QUESTION 02: Daily Activity Log Appender
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

import os

def append_log_entry(filename, timestamp, activity):
    """
    1. Opens 'filename' in append mode ('a') with utf-8 encoding.
    2. Writes a single line: '[{timestamp}] {activity}\n'.
    3. Returns True upon success.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_file = "test_daily_log.txt"

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Daily Activity Log Appender")
    print("=" * 65)

    if os.path.exists(test_file):
        os.remove(test_file)

    passed = 0
    total = 3

    # Test 1: Append to brand new file
    res1 = append_log_entry(test_file, "09:00 AM", "Lab system started")
    with open(test_file, "r", encoding="utf-8") as f:
        lines1 = [l.strip() for l in f]

    if res1 is True and lines1 == ["[09:00 AM] Lab system started"]:
        print("[1/3] PASS: Append to new file")
        passed += 1
    else:
        print(f"[1/3] FAIL: Append to new file (Got: {lines1})")

    # Test 2: Append 2nd entry (verify existing content was NOT overwritten)
    res2 = append_log_entry(test_file, "10:30 AM", "Student logged into PC-04")
    with open(test_file, "r", encoding="utf-8") as f:
        lines2 = [l.strip() for l in f]

    if res2 is True and len(lines2) == 2 and lines2[0] == "[09:00 AM] Lab system started":
        print("[2/3] PASS: Append to existing file (Preserved prior entries)")
        passed += 1
    else:
        print(f"[2/3] FAIL: Prior content was overwritten or missing! (Got: {lines2})")

    # Test 3: Append 3rd entry
    res3 = append_log_entry(test_file, "12:00 PM", "Lab session concluded")
    with open(test_file, "r", encoding="utf-8") as f:
        lines3 = [l.strip() for l in f]

    if res3 is True and len(lines3) == 3 and lines3[2] == "[12:00 PM] Lab session concluded":
        print("[3/3] PASS: Multiple consecutive appends verified")
        passed += 1
    else:
        print(f"[3/3] FAIL: 3rd entry verification failed! (Got: {lines3})")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
