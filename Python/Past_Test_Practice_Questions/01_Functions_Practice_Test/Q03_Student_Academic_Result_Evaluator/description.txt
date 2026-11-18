# Question 03: Student Academic Result Evaluator

> **Test:** Functions Practice Test  
> **Topic:** Dictionaries, List Processing & Conditional Grades  
> **Difficulty:** Easy-Medium | **Max Marks:** 10

---

## 📌 Problem Statement
Write a function `evaluate_student(record)` that evaluates a student's academic record and assigns an academic status.

The function accepts a dictionary `record` in the following format:
```python
{
    "name": "Student Name",
    "marks": [mark1, mark2, mark3, ...]
}
```

### Evaluation Criteria:
1. **Total:** The sum of all marks in the list.
2. **Average:** `total / len(marks)`.
3. **Academic Status:**
   - If the student scored **less than 40** in ANY subject, status is **`"FAIL"`** (regardless of average!).
   - Otherwise, evaluate by average:
     - Average >= 75.0 -> **`"DISTINCTION"`**
     - Average >= 60.0 -> **`"FIRST CLASS"`**
     - Otherwise -> **`"SECOND CLASS"`**

The function must return a dictionary with the following keys:
```python
{
    "name": str,
    "total": int,
    "average": float,
    "status": str
}
```

---

## 📥 Function Signature
```python
def evaluate_student(record):
    # Returns evaluation dictionary: {"name": ..., "total": ..., "average": ..., "status": ...}
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:** `{"name": "Aman", "marks": [85, 90, 80]}`
- **Expected Return:**
  ```python
  {"name": "Aman", "total": 255, "average": 85.0, "status": "DISTINCTION"}
  ```

### Sample 2:
- **Input:** `{"name": "Rohan", "marks": [80, 35, 90]}`
- **Expected Return:**
  ```python
  {"name": "Rohan", "total": 205, "average": 68.33, "status": "FAIL"}
  ```
- **Explanation:** Even though Rohan's average is 68.33, he scored 35 (< 40) in one subject, so status is FAIL.
