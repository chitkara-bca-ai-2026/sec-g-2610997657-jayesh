# ==============================================================================
# QUESTION 04: Log Severity Filter & Export
# ==============================================================================
# INSTRUCTIONS:
# Implement the function below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

import os

def filter_log_by_tag(source_filename, target_filename, tag):
    """
    1. Reads each line from 'source_filename'.
    2. Writes lines containing 'tag' to 'target_filename'.
    3. Returns the total count (int) of matching lines exported.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    src_file = "test_source.log"
    tgt_file = "test_target.log"

    sample_log = (
        "[INFO] System started\n"
        "[ERROR] Database timeout\n"
        "[INFO] Request handled\n"
        "[WARN] High memory usage\n"
        "[ERROR] Port already bound\n"
    )

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Log Severity Filter & Export")
    print("=" * 65)

    test_cases = [
        {"desc": "Filter [ERROR] (2 Matches)", "tag": "[ERROR]", "expected_count": 2},
        {"desc": "Filter [INFO] (2 Matches)", "tag": "[INFO]", "expected_count": 2},
        {"desc": "Filter [WARN] (1 Match)", "tag": "[WARN]", "expected_count": 1},
        {"desc": "Filter [CRITICAL] (0 Matches)", "tag": "[CRITICAL]", "expected_count": 0}
    ]

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        with open(src_file, "w", encoding="utf-8") as f:
            f.write(sample_log)
        if os.path.exists(tgt_file):
            os.remove(tgt_file)

        actual_count = filter_log_by_tag(src_file, tgt_file, tc["tag"])

        # Check target file content
        file_ok = os.path.exists(tgt_file)
        if file_ok:
            with open(tgt_file, "r", encoding="utf-8") as f:
                lines = [l.strip() for l in f if l.strip()]
            all_have_tag = all(tc["tag"] in l for l in lines)
            count_matches = (len(lines) == tc["expected_count"])
        else:
            all_have_tag = False
            count_matches = False

        if actual_count == tc["expected_count"] and count_matches and all_have_tag:
            print(f"[{i}/{total}] PASS: {tc['desc']} (Exported Count={actual_count})")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Expected Count: {tc['expected_count']}, Got: {actual_count}")
            print(f"       -> File created: {file_ok}, All lines match tag: {all_have_tag}")

        for f_path in [src_file, tgt_file]:
            if os.path.exists(f_path):
                os.remove(f_path)

    print("-" * 65)
    score_pct = (passed / total) * 100
    print(f"Summary: {passed}/{total} Test Cases Passed ({score_pct:.1f}%)")
    if passed == total:
        print("🎉 EXCELLENT! Your solution is 100% correct.")
    else:
        print("⚠️  Some tests failed. Check your logic and re-run!")
    print("=" * 65)
