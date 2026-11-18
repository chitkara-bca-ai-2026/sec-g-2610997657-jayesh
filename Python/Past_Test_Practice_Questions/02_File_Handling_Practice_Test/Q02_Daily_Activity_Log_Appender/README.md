# Question 02: Daily Activity Log Appender

> **Test:** File Handling Practice Test  
> **Topic:** Append Mode ('a'), Preserving Existing Content  
> **Difficulty:** Easy | **Max Marks:** 10

---

## 📌 Problem Statement
Develop a function for an audit log management system that records timestamps and student activities into an existing log book.

Implement the following function:
```python
def append_log_entry(filename, timestamp, activity):
```

### Function Specifications:
1. Open the file named `filename` in **append mode (`'a'`)** with `utf-8` encoding.
2. Append a single formatted line in this exact format:
   ```text
   [{timestamp}] {activity}\n
   ```
3. Return `True` upon successful append.
4. **Critical:** Opening in append mode must NOT overwrite or erase any lines already existing in the file!

---

## 📥 Function Signature
```python
def append_log_entry(filename, timestamp, activity):
    # Appends "[{timestamp}] {activity}\n" to filename and returns True
    pass
```

---

## 🧪 Sample Case
- **Existing File Content:**
  ```text
  [09:00 AM] System boot completed
  ```
- **Function Call:**
  `append_log_entry("daily_log.txt", "10:15 AM", "User student_01 logged in")`
- **Updated File Content on Disk:**
  ```text
  [09:00 AM] System boot completed
  [10:15 AM] User student_01 logged in
  ```
- **Return Value:** `True`
