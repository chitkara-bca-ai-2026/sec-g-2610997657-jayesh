# Question 02: Palindrome Word Extractor

> **Test:** Functions Practice Test  
> **Topic:** String Manipulation, Sets & Sorting  
> **Difficulty:** Easy | **Max Marks:** 10

---

## 📌 Problem Statement
Write a modular Python program to extract all unique palindrome words from a given sentence.

You must implement two functions:
1. `is_palindrome(word)`:
   - Takes a string `word`.
   - Returns `True` if `word` reads the same forwards and backwards (case-insensitive), otherwise returns `False`.
   - Single-character words (e.g. `'a'`) are considered palindromes.

2. `find_palindromes(sentence)`:
   - Takes a string `sentence`.
   - Splits the sentence into words.
   - Finds all words that are palindromes.
   - Returns a **sorted list of unique lowercase palindrome words**.
   - If no palindromes exist or the sentence is empty, return an empty list `[]`.

---

## 📥 Function Signatures
```python
def is_palindrome(word):
    # Returns True if word is a palindrome (case-insensitive)
    pass

def find_palindromes(sentence):
    # Returns a sorted list of unique lowercase palindrome words
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:** `"Madam drove the racecar at noon"`
- **Expected Return:** `['madam', 'noon', 'racecar']`
- **Explanation:**
  - "Madam" -> "madam" (palindrome)
  - "racecar" -> (palindrome)
  - "noon" -> (palindrome)
  - Result is unique, lowercase, and sorted alphabetically: `['madam', 'noon', 'racecar']`.

### Sample 2:
- **Input:** `"Hello world from python programming"`
- **Expected Return:** `[]`
- **Explanation:** No palindrome words exist.

---

## 💡 Edge Cases to Consider
- Case-insensitivity: `"Madam"` and `"madam"` are the same word and must be deduplicated into lowercase `"madam"`.
- Duplicates: `"radar kayak radar"` should only contain `['kayak', 'radar']`.
- Empty sentence: Return `[]`.
