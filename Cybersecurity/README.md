## ```🔐 Secure-Login-System```

A Python-based login system that verifies user credentials, limits login attempts, and records login activity in a log file.

## 📌 About

This project is an improved version of a basic login system.

Instead of using a single hardcoded username and password, the program stores multiple users and their passwords in a Python dictionary. It also records successful and failed login attempts in a log file.

The user is given **three attempts** to log in. After three failed attempts, the account is locked.

## ⚙️ Features

* Multiple user authentication
* Username and password verification
* Maximum of 3 login attempts
* Account lockout after failed attempts
* Successful login logging
* Failed login logging
* Basic exception handling
* Login activity stored in `log.txt`

## 🛠️ Concepts Used

* Python Dictionaries
* `for` loop
* Conditional statements
* User input
* File handling
* `with open()`
* Append mode (`"a"`)
* `try / except`
* Authentication logic

## 📁 Files

```text
Secure-Login-System/
├── secure_login_system.py
├── log.txt
└── README.md
```

## ▶️ How to Run

Run the following command:

```bash
python secure_login_system.py
```

Enter a username and password when prompted.

## 💻 Example

```text
Enter username: ali
Enter password: 1234
login successful
```

For incorrect credentials:

```text
Enter username: ali
Enter password: 9999
wrong credentials
```

After three failed attempts:

```text
Account Locked
```

## 📝 Logging

The program records login attempts in `log.txt`.

Example:

```text
ali - success
ahmad - fail
adil - fail
```

This project demonstrates how authentication, login attempt limits, and activity logging can be implemented using Python.


  
## ```🔐 Login-System```

A basic Python authentication system that verifies a predefined username and password.

The user gets **three login attempts**. Correct credentials grant access, while three failed attempts result in the account being locked.

### Concepts Used

* Functions
* Loops
* Conditional statements
* User input
* Authentication logic
* Login attempt control

### Run

```bash
python login_system.py
```

This project demonstrates basic username/password authentication with limited login attempts.
