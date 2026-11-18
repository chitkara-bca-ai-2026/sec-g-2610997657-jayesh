# ==============================================================================
# QUESTION 02: Palindrome Word Extractor
# ==============================================================================
# INSTRUCTIONS:
# Implement the two functions below.
# When ready, simply RUN THIS FILE to test your solution with the driver code!
# ==============================================================================

def is_palindrome(word):
    """
    Takes a string 'word'.
    Returns True if word is a palindrome (case-insensitive), False otherwise.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


def find_palindromes(sentence):
    """
    Takes a string 'sentence'.
    Returns a sorted list of unique lowercase palindrome words found in sentence.
    """
    # --- WRITE YOUR CODE HERE ---
    pass


# ==============================================================================
# DRIVER CODE & AUTOMATED SELF-EVALUATION TEST RUNNER (DO NOT MODIFY)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        {"desc": "Sample 1 (Standard Sentence)", "input": "Madam drove the racecar at noon", "expected": ["madam", "noon", "racecar"]},
        {"desc": "Sample 2 (No Palindromes)", "input": "Hello world from python programming", "expected": []},
        {"desc": "Multiple Duplicates", "input": "Kayak kayak radar level radar", "expected": ["kayak", "level", "radar"]},
        {"desc": "All Palindromes", "input": "Deed rotor level civic radar", "expected": ["civic", "deed", "level", "radar", "rotor"]},
        {"desc": "Single Letters & Empty", "input": "I saw a cat at noon", "expected": ["a", "i", "noon"]},
        {"desc": "Empty String", "input": "", "expected": []}
    ]

    print("=" * 65)
    print("  RUNNING SELF-EVALUATION: Palindrome Word Extractor")
    print("=" * 65)

    passed = 0
    total = len(test_cases)

    for i, tc in enumerate(test_cases, 1):
        actual = find_palindromes(tc["input"])
        if actual == tc["expected"]:
            print(f"[{i}/{total}] PASS: {tc['desc']}")
            passed += 1
        else:
            print(f"[{i}/{total}] FAIL: {tc['desc']}")
            print(f"       -> Input:    {repr(tc['input'])}")
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
