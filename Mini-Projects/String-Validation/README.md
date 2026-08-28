# String Validation

A simple Python mini project that checks different properties of a given string using Python's built-in string methods.

## 📌 Project Overview

The program takes a string as input and checks whether it contains:

* At least one alphanumeric character
* At least one alphabetic character
* At least one digit
* At least one lowercase character
* At least one uppercase character

## 🛠️ Technologies Used

* Python

## 💻 How It Works

The program uses the `any()` function along with Python string methods:

```python
s = input()

print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))
```

### 🔍 Methods Used

| Method      | Purpose                                                          |
| ----------- | ---------------------------------------------------------------- |
| `isalnum()` | Checks for letters or numbers                                    |
| `isalpha()` | Checks for alphabetic characters                                 |
| `isdigit()` | Checks for digits                                                |
| `islower()` | Checks for lowercase letters                                     |
| `isupper()` | Checks for uppercase letters                                     |
| `any()`     | Returns `True` if at least one character satisfies the condition |

## ▶️ Example

### Input

```text
Hello123
```

### Output

```text
True
True
True
True
True
```

## 🎯 Learning Objectives

* Practice Python string methods
* Understand the `any()` function
* Learn character validation
* Improve Python fundamentals
* Practice working with strings
