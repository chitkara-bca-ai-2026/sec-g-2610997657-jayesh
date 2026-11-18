# Question 05: Recursive Sum of Digits & Digital Root

> **Test:** Functions Practice Test  
> **Topic:** Recursion, Base Cases & Mathematical Algorithms  
> **Difficulty:** Medium | **Max Marks:** 10

---

## 📌 Problem Statement
Write two recursive functions to compute the sum of digits and the digital root of a non-negative integer.

### Functions to Implement:
1. `sum_of_digits(n)`:
   - Takes a non-negative integer `n`.
   - Returns the sum of its individual digits computed **recursively** (do not use `str()`).
   - Example: `sum_of_digits(9875)` = 9 + 8 + 7 + 5 = `29`.

2. `digital_root(n)`:
   - The digital root is the single-digit value obtained by iteratively summing digits until a single digit remains.
   - Must be computed **recursively** using `sum_of_digits()`.
   - Example: `digital_root(9875)` -> `sum_of_digits(9875)` is 29 -> `sum_of_digits(29)` is 11 -> `sum_of_digits(11)` is `2`. Returns `2`.

---

## 📥 Function Signatures
```python
def sum_of_digits(n):
    # Base case: if n < 10, return n
    # Recursive case: (n % 10) + sum_of_digits(n // 10)
    pass

def digital_root(n):
    # Base case: if n < 10, return n
    # Recursive case: digital_root(sum_of_digits(n))
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:** `n = 9875`
- **First Sum:** `29`
- **Digital Root:** `2`

### Sample 2:
- **Input:** `n = 7`
- **First Sum:** `7`
- **Digital Root:** `7`
