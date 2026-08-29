## ```Python-Student-Programs```

Simple Python programs for processing student data using dictionaries, loops, conditions, and basic data structures.

## 📚 Programs

* **Students-Above-2-Fail** — Finds students with more than two failed subjects.
* **Fail-Count-Students** — Counts failed subjects based on student marks.



## ```Student-Result-Calculator```
A Python file-handling project that reads student marks from a text file, calculates total marks, obtained marks, average, and percentage, and generates a formatted result file.



# Student Result Calculator

A simple **Python file-handling project** that reads student names and marks from a text file, calculates their academic results, and saves the formatted results into a separate output file.

## 📌 Project Overview

This project takes student data from `student_marks.txt`, processes the marks using Python, and generates a complete result table in `results.txt`.

For each student, the program calculates:

* Total Marks
* Obtained Marks
* Average
* Percentage

The program also supports multiple students and multiple subjects.

## 📂 Project Structure

```text
Student-Result-Calculator/
│
├── student_marks.txt
├── student_result.py
├── results.txt
└── README.md
```

## 📄 Files Description

### `student_marks.txt`

Contains the input data of students and their marks.

Example:

```text
Ali 23 45 43 45 50
Asim 45 35 48 34 47
Ahmed 40 42 35 34 39
```

### `student_result.py`

Python program that:

1. Reads student data from the input file.
2. Stores names and marks in a dictionary.
3. Calculates total marks.
4. Calculates obtained marks.
5. Calculates average.
6. Calculates percentage.
7. Writes the final results to `results.txt`.

### `results.txt`

Contains the generated results in a structured table format.

Example:

```text
Student Name    Subject 1   Subject 2   Subject 3   Subject 4   Subject 5   Total Marks    Obtained Marks    Average     Percentage
Ali             23.0        45.0        43.0        45.0        50.0        250            206.0             41.20       82.40%
Asim            45.0        35.0        48.0        34.0        47.0        250            209.0             41.80       83.60%
Ahmed           40.0        42.0        35.0        34.0        39.0        250            190.0             38.00       76.00%
```

## 🧮 Calculations

**Obtained Marks**

```text
Sum of all subject marks
```

**Total Marks**

```text
Number of Subjects × 50
```

**Average**

```text
Obtained Marks ÷ Number of Subjects
```

**Percentage**

```text
(Obtained Marks ÷ Total Marks) × 100
```

## 🛠️ Concepts Practiced

* Python Dictionaries
* Lists
* Loops
* File Handling
* String Processing
* `split()`
* `sum()`
* `len()`
* `f-string Formatting`
* Basic Data Processing
* Calculations and Output Formatting

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python student_result.py
```

The program will read data from `student_marks.txt` and generate/update `results.txt`.

## 🎯 Learning Goal

The main goal of this project is to practice **Python file handling and basic data processing** by working with real-world student data and generating a structured result report.







