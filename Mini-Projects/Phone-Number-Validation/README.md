# Python Phone Number Validator

A simple Python mini project that validates a 10-digit phone number using **Regular Expressions (Regex)**.

## 📌 Project Overview

This program takes a phone number as input and checks whether it follows the required format.

The number must:

* Contain exactly **10 digits**
* Start with **7, 8, or 9**
* Contain digits only

## 🛠️ Technologies Used

* Python
* Regular Expressions (`re` module)

## 💻 How It Works

The program uses the following regex pattern:

```python
r'^[789]\d{9}$'
```

### Regex Breakdown

| Pattern | Meaning                        |
| ------- | ------------------------------ |
| `^`     | Start of the string            |
| `[789]` | First digit must be 7, 8, or 9 |
| `\d`    | Any digit from 0–9             |
| `{9}`   | Exactly 9 more digits          |
| `$`     | End of the string              |

Therefore, the complete number must have **10 digits**.

## ▶️ Example

### Valid Input

```text
Enter a number: 9876543210
Yes
```

### Invalid Input

```text
Enter a number: 1234567890
No
```

## 🎯 Learning Objectives

* Understand Python's `re` module
* Learn basic Regex syntax
* Perform input validation
* Practice conditional statements

