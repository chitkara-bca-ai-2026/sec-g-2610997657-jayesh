# Question 05: Dual Shift File Merger & Consolidator

> **Test:** File Handling Practice Test  
> **Topic:** Multiple File Reads, Header Insertion, Consolidation  
> **Difficulty:** Medium | **Max Marks:** 10

---

## 📌 Problem Statement
A manufacturing factory runs two daily shifts: Shift A (Morning) and Shift B (Evening). At the end of each day, production logs from both shift files must be merged into a single consolidated daily file.

Implement the function:
```python
def merge_shift_files(shift1_filename, shift2_filename, consolidated_filename):
```

### Function Specifications:
1. Read all lines from `shift1_filename`.
2. Read all lines from `shift2_filename`.
3. Open `consolidated_filename` in **write mode (`'w'`)**.
4. Write the exact header line at the very top:
   ```text
   --- CONSOLIDATED LOG ---\n
   ```
5. Follow the header by writing all lines from `shift1_filename`, followed by all lines from `shift2_filename`.
6. Return the total count (int) of merged shift records (do NOT count the header line).

---

## 📥 Function Signature
```python
def merge_shift_files(shift1_filename, shift2_filename, consolidated_filename):
    # Merges shift1 and shift2 into consolidated with header, returns record count
    pass
```

---

## 🧪 Sample Case
- **Shift 1 (`shift_a.txt`):**
  ```text
  Unit 101 - Assembled
  Unit 102 - Assembled
  ```
- **Shift 2 (`shift_b.txt`):**
  ```text
  Unit 103 - Inspected
  ```
- **Consolidated File (`daily_summary.txt`):**
  ```text
  --- CONSOLIDATED LOG ---
  Unit 101 - Assembled
  Unit 102 - Assembled
  Unit 103 - Inspected
  ```
- **Return Value:** `3`
