# 🔐 Login-System

A simple Python-based login system that allows a user to authenticate using a predefined username and password.

## 📌 About

This project demonstrates a basic authentication system in Python.

The program gives the user **three attempts** to enter the correct username and password. If the credentials are correct, access is granted. If all three attempts fail, the account is locked.

## ⚙️ Features

* Username and password authentication
* Maximum of 3 login attempts
* Access granted for correct credentials
* Account lockout after 3 failed attempts
* Basic authentication logic

## 🛠️ Concepts Used

* Python Functions
* `for` loop
* `if / else`
* User input
* Variables
* `return` statements
* Basic authentication logic

## ▶️ How to Run

Run the following command:

```bash
python login_system.py
```

Enter the username and password when prompted.

## 💻 Example

```text
Enter username: admin
Enter password: 123456
Access Granted
```

If incorrect credentials are entered:

```text
Enter username: user
Enter password: 1111
Wrong attempt

Enter username: user
Enter password: 2222
Wrong attempt

Enter username: user
Enter password: 3333
Wrong attempt

Account Locked
```

## 🎯 Purpose

This project was created to practice basic authentication concepts, loops, functions, conditional statements, and login attempt control in Python.

