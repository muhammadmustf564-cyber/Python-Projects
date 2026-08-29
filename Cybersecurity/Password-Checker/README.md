# 🔑 Password Checker

A simple Python program that checks whether a password meets basic strength requirements.

## 📌 About

The program evaluates a user-entered password based on its length and character types. A password is considered strong if it contains at least **9 characters**, including an uppercase letter, lowercase letter, digit, and special character.

## ⚙️ Requirements

A strong password must contain:

* At least 9 characters
* One uppercase letter
* One lowercase letter
* One digit
* One special character

## 🛠️ Concepts Used

* User input
* `len()`
* `any()`
* String methods
* Conditional statements
* Basic password validation

## ▶️ How to Run

```bash
python password_checker.py
```

Enter a password when prompted.

## 💻 Example

```text
Enter password: Hello@12345
Hello@12345 => strong password
```

```text
Enter password: hello123
hello123 => weak password
```
## 🎯 Purpose

This project demonstrates how Python can be used to validate basic password-strength requirements.

