# Question 01: Student Notes File Writer & Counter

> **Test:** File Handling Practice Test  
> **Topic:** File Writing ('w'), File Reading ('r'), UTF-8 Encoding  
> **Difficulty:** Easy | **Max Marks:** 10

---

## 📌 Problem Statement
A school department is developing an automated notes manager to store and verify student subject notes in text files.

Your task is to implement the following function:
```python
def write_notes_to_file(filename, notes_list):
```

### Function Specifications:
1. Open the file named `filename` in **write mode (`'w'`)** using `utf-8` encoding.
2. Write each note from `notes_list` to the file on a **new line** (ensure every line ends with `\n`).
3. Close the file (or use a `with open(...)` block).
4. Reopen the file in **read mode (`'r'`)**, count the total number of lines saved in the file, and return this count as an integer.

---

## 📥 Function Signature
```python
def write_notes_to_file(filename, notes_list):
    # 1. Write notes_list entries to filename with '\n'
    # 2. Re-read filename and return line count
    pass
```

---

## 🧪 Sample Cases

### Sample 1:
- **Input:**
  `filename = "notes.txt"`
  `notes_list = ["Python variables", "Control Flow Statements", "Function Definition"]`
- **Output:** Returns integer `3`.
- **File on Disk (`notes.txt`):**
  ```text
  Python variables
  Control Flow Statements
  Function Definition
  ```
