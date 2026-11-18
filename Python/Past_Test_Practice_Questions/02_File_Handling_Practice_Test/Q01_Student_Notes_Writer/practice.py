# ==============================================================================
# QUESTION 01: Student Notes File Writer & Counter
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

import os

def write_notes_to_file(filename, notes_list):
    """
    1. Opens 'filename' in write mode ('w') with utf-8 encoding.
    2. Writes each note from 'notes_list' on a new line.
    3. Re-opens the file in read mode ('r') and returns the total line count (int).
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {
            "desc": "Standard 3 Notes",
            "file": "test_notes_1.txt",
            "notes": ["Python variables", "Control Flow Statements", "Function Definition"],
            "expected_count": 3
        },
        {
            "desc": "Empty Notes List",
            "file": "test_notes_empty.txt",
            "notes": [],
            "expected_count": 0
        },
        {
            "desc": "4 Technical Subject Notes",
            "file": "test_notes_ai.txt",
            "notes": ["Machine Learning", "Neural Networks", "NLP", "Computer Vision"],
            "expected_count": 4
        }
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Student Notes File Writer & Counter")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        filename = tc["file"]
        if os.path.exists(filename):
            os.remove(filename)

        actual_count = write_notes_to_file(filename, tc["notes"])

        # Disk verification: verify file exists and content matches
        file_valid = os.path.exists(filename)
        content_matches = False
        if file_valid:
            with open(filename, "r", encoding="utf-8") as f:
                lines = [l.rstrip("\r\n") for l in f]
            content_matches = (lines == tc["notes"])

        if actual_count == tc["expected_count"] and file_valid and content_matches:
            print(f"[{i}/{total}] PASS: {tc['desc']} (Count={actual_count}, Disk Verified)")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Expected Count: {tc['expected_count']}, Actual: {actual_count}")
            print(f"       -> File on disk exists: {file_valid}, Content matches: {content_matches}")

        # Cleanup
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
