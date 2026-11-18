# Question 03: Numeric Data File Reader & Stats

> **Test:** File Handling Practice Test  
> **Topic:** File Reading ('r'), Type Conversion, Mathematical Aggregation  
> **Difficulty:** Easy-Medium | **Max Marks:** 10

---

## 📌 Problem Statement
An educational research team stores exam scores in plain text files, with each line containing a single integer score.

Write a function `calculate_file_stats(filename)` to analyze the file and return statistical metrics.

### Function Specifications:
1. Open the file `filename` in **read mode (`'r'`)**.
2. Read all lines, strip leading/trailing whitespace, and parse non-empty lines into integers.
3. If the file is **empty** (or contains no valid lines), return `(0, 0, 0.0)`.
4. Otherwise, compute:
   - `count`: total number of scores (int)
   - `total`: sum of all scores (int)
   - `average`: `total / count` (float)
5. Return the tuple `(count, total, average)`.

---

## 📥 Function Signature
```python
def calculate_file_stats(filename):
    # Returns (count, total, average)
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **File Content (`scores.txt`):**
  ```text
  85
  90
  75
  90
  60
  ```
- **Calculation:**
  - Count = 5
  - Total = 85 + 90 + 75 + 90 + 60 = 400
  - Average = 400 / 5 = 80.0
- **Expected Return:** `(5, 400, 80.0)`

### Sample 2 (Empty File):
- **File Content (`empty.txt`):** (0 bytes)
- **Expected Return:** `(0, 0, 0.0)`
