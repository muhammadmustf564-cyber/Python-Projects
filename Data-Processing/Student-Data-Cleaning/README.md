
# Student Data Cleaning

A Python-based data cleaning and analysis project that uses **Pandas** to process student records, handle missing values, filter data, sort marks, and generate cleaned datasets.

## 📌 About

The project works with a student dataset containing information such as names, ages, marks, gender, and city.

The original dataset contains missing values in the **Age** and **Marks** columns. These missing values are handled using basic Pandas techniques before performing data analysis.

## 📂 Files

* `student_dirty_data.csv` — Original student dataset containing missing values.
* `student_data.py` — Python script used for data cleaning, filtering, sorting, and analysis.
* `student_clean_data.csv` — Cleaned student dataset in CSV format.
* `student_clean_data.xlsx` — Cleaned student dataset exported to Excel format.

## 🛠️ Operations Performed

* Cleaned column names by removing extra spaces.
* Filled missing **Age** values using the mode.
* Filled missing **Marks** values using the mean.
* Filtered students by city.
* Filtered students by gender.
* Found students with marks greater than 85.
* Sorted students by marks in ascending order.
* Identified the top 5 students.
* Identified the lowest 5 students.
* Exported the cleaned data to CSV and Excel formats.

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* CSV
* Excel

## 🎯 Purpose

This project provides practice with **data cleaning, missing-value handling, filtering, sorting, and basic data analysis using Pandas**.
