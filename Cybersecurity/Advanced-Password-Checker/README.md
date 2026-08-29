# 🔐 Advanced Password Checker

A Python-based password validation tool that evaluates password strength and provides feedback about missing security requirements.

## 📌 About

The program checks a password against multiple security requirements, including a minimum length of **8 characters**, uppercase and lowercase letters, digits, and special characters.

Based on the number of missing requirements, the password is classified as **Strong, Medium, or Weak**. The program also displays the specific requirements that are missing.

The user has **three attempts** to enter a strong password. After three unsuccessful attempts, the program displays **Account Locked**.

## ⚙️ Features

* Minimum 8-character requirement
* Uppercase and lowercase character checks
* Digit validation
* Special character validation
* Strong, Medium, and Weak classification
* Displays missing requirements
* Maximum of 3 attempts
* Account lockout

## 🛠️ Concepts Used

* `for` loop
* Lists
* `append()`
* `any()`
* String methods
* Conditional statements
* User input
* Password validation
* Attempt tracking

## ▶️ How to Run

```bash
python advanced_password_checker.py
```

Enter a password when prompted.

## 💻 Example

```text
Enter password: hello123

Weak Password
Reason:
- missing uppercase letter
- missing special letter
```

For a password meeting all requirements:

```text
Enter password: Hello@123

Strong password
```

## 🎯 Purpose

This project demonstrates a detailed approach to password-strength validation by classifying passwords, identifying missing security requirements, and providing useful feedback to the user.



