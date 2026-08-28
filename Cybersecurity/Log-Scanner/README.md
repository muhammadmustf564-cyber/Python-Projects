# 📝 Log Scanner

A simple Python program that scans a log file and identifies lines containing specific keywords such as errors, failed attempts, and warnings.

## 📌 About

The program reads a log file line by line and searches for predefined keywords. When a matching keyword is found, it displays the line number and the corresponding log entry.

## 🛠️ Concepts Used

* File handling
* `with open()`
* Reading files
* `enumerate()`
* `any()`
* String methods
* List processing
* Conditional statements

## ▶️ How to Run

Make sure `log-file.txt` is in the same folder as the Python file, then run:

```bash
python log_scanner.py
```

## 💻 Example

```text
Line 2: Login failed for user
Line 5: Warning: Multiple login attempts
Line 8: System error detected
```


