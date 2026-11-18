# ==============================================================================
# QUESTION 05: Dual Shift File Merger & Consolidator
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

import os

def merge_shift_files(shift1_filename, shift2_filename, consolidated_filename):
    """
    1. Reads all lines from 'shift1_filename'.
    2. Reads all lines from 'shift2_filename'.
    3. Writes to 'consolidated_filename':
         First line: '--- CONSOLIDATED LOG ---\n'
         Followed by shift1 lines, then shift2 lines.
    4. Returns total merged record count (int), excluding header.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    f_shift1 = "test_shift1.txt"
    f_shift2 = "test_shift2.txt"
    f_out = "test_consolidated.txt"

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Dual Shift File Merger & Consolidator")
    print("=" * 65)

    test_cases = [
        {
            "desc": "Standard 2+1 Records",
            "s1": ["Unit 101 - Assembled", "Unit 102 - Assembled"],
            "s2": ["Unit 103 - Inspected"],
            "expected_count": 3
        },
        {
            "desc": "Shift 1 Empty, Shift 2 Has Records",
            "s1": [],
            "s2": ["Batch Alpha Started", "Batch Alpha Finished"],
            "expected_count": 2
        },
        {
            "desc": "Both Shifts Empty",
            "s1": [],
            "s2": [],
            "expected_count": 0
        }
    ]

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        with open(f_shift1, "w", encoding="utf-8") as f1:
            for l in tc["s1"]:
                f1.write(l + "\n")

        with open(f_shift2, "w", encoding="utf-8") as f2:
            for l in tc["s2"]:
                f2.write(l + "\n")

        if os.path.exists(f_out):
            os.remove(f_out)

        actual_count = merge_shift_files(f_shift1, f_shift2, f_out)

        file_ok = os.path.exists(f_out)
        header_ok = False
        content_ok = False
        if file_ok:
            with open(f_out, "r", encoding="utf-8") as f:
                lines = [l.strip() for l in f if l.strip()]
            if lines and lines[0] == "--- CONSOLIDATED LOG ---":
                header_ok = True
                content_ok = (lines[1:] == (tc["s1"] + tc["s2"]))

        if actual_count == tc["expected_count"] and header_ok and content_ok:
            print(f"[{i}/{total}] PASS: {tc['desc']} (Merged Count={actual_count})")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Expected Count: {tc['expected_count']}, Got: {actual_count}")
            print(f"       -> File exists: {file_ok}, Header correct: {header_ok}, Records match: {content_ok}")

        for p in [f_shift1, f_shift2, f_out]:
            if os.path.exists(p):
                os.remove(p)

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
