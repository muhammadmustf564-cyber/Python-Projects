
# 🎯 Number Guessing Game

A simple command-line number guessing game built with Python.

## 📌 About

In this game, the computer randomly selects a number between **1 and 100**. The player has to guess the number.

After each guess, the program gives a hint:

* **Too High** — the guess is greater than the correct number.
* **Too Low** — the guess is smaller than the correct number.
* **Correct! You Win** — the player guessed the number correctly.

At the end, the program displays the total number of attempts.

## 🛠️ Concepts Used

* Python `random` module
* `random.randint()`
* `while` loop
* `if / elif / else`
* User input
* Variables
* f-strings
* Basic game logic

## ▶️ How to Run

Run the following command:

```bash
python number_guessing_game.py
```

Then enter a number between **1 and 100** when prompted.

## 💻 Example

```text
Guess a number between 1 and 100: 50
Too High, Try another guess

Guess a number between 1 and 100: 25
Too Low, Try another guess

Guess a number between 1 and 100: 32
Correct! You Win

You guessed in 3 attempts
```

## 🎯 Purpose

This project was created to practice Python loops, conditional statements, random number generation, user input, and basic problem-solving.
