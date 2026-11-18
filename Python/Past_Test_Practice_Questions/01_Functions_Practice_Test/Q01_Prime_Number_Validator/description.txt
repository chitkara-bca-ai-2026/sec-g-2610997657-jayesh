# Question 01: Prime Number Validator & Filter

> **Test:** Functions Practice Test  
> **Topic:** Modular Helper Functions & List Processing  
> **Difficulty:** Medium | **Max Marks:** 10

---

## 📌 Problem Statement
Write a modular Python program to filter out all prime numbers from a given list of integers.

You must implement two functions:
1. `is_prime(n)`:
   - Takes an integer `n`.
   - Returns `True` if `n` is a prime number, otherwise returns `False`.
   - Remember: Numbers less than or equal to 1 are NOT prime. `2` is the smallest and only even prime number.

2. `filter_primes(numbers)`:
   - Takes a list of integers `numbers`.
   - Uses `is_prime()` to filter and return a new list containing only the prime numbers in their original order.
   - If no prime numbers exist in the list, return an empty list `[]`.

---

## 📥 Function Signatures
```python
def is_prime(n):
    # Returns True if n is prime, False otherwise
    pass

def filter_primes(numbers):
    # Returns list of prime numbers from numbers list
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:** `[10, 3, 4, 7, 15, 19, 20]`
- **Expected Return:** `[3, 7, 19]`
- **Explanation:** 3, 7, and 19 are prime numbers. 10, 4, 15, and 20 are composite numbers.

### Sample 2:
- **Input:** `[4, 6, 8, 9]`
- **Expected Return:** `[]`
- **Explanation:** No prime numbers exist in the list.

---

## 💡 Edge Cases to Consider
- Numbers `<= 1` (e.g. `0`, `1`, negative integers) are **not** prime.
- The number `2` is prime!
- Large prime numbers (e.g. `97`, `101`).
