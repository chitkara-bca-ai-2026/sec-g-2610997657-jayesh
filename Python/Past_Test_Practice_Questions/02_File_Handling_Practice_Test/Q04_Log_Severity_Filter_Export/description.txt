# Question 04: Log Severity Filter & Export

> **Test:** File Handling Practice Test  
> **Topic:** Reading & Writing Simultaneously, Substring Matching  
> **Difficulty:** Medium | **Max Marks:** 10

---

## 📌 Problem Statement
A server monitor saves continuous operational logs. You are tasked with developing a filter utility that extracts only logs matching a specified severity tag (e.g. `[ERROR]`, `[INFO]`, or `[WARN]`) into a separate export file.

Implement the function:
```python
def filter_log_by_tag(source_filename, target_filename, tag):
```

### Function Specifications:
1. Open `source_filename` in **read mode (`'r'`)**.
2. Open `target_filename` in **write mode (`'w'`)**.
3. For each line in `source_filename`, check if the string `tag` is present in the line.
4. If `tag` is found, write the line to `target_filename` (ensure newline is preserved).
5. Return the total count (int) of matching lines exported.

---

## 📥 Function Signature
```python
def filter_log_by_tag(source_filename, target_filename, tag):
    # Writes lines containing tag from source to target, returns count
    pass
```

---

## 🧪 Sample Case
- **Source File (`server.log`):**
  ```text
  [INFO] Server booted successfully
  [ERROR] Database connection timed out
  [INFO] User request received
  [ERROR] Out of memory on worker 3
  ```
- **Call:** `filter_log_by_tag("server.log", "errors.txt", "[ERROR]")`
- **Target File (`errors.txt`):**
  ```text
  [ERROR] Database connection timed out
  [ERROR] Out of memory on worker 3
  ```
- **Return Value:** `2`
