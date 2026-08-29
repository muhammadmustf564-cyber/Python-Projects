# Website Logs Data Processing

A Python-based project that uses **Pandas** to clean, process, and analyze website log data.

## 📌 About

This project processes website logs stored in a CSV file. It cleans the data, identifies frequently visited pages, finds 404 errors, and analyzes the most active IP addresses.

## 🔧 What This Project Does

* Loads website logs from a CSV file
* Combines date and time into a `datetime` column
* Removes duplicate records
* Converts status codes to numeric values
* Finds the most visited pages
* Identifies pages with **404 errors**
* Finds the most active IP addresses
* Saves the cleaned data into a new CSV file

## 🛠️ Technologies Used

* Python
* Pandas
* CSV

## 📂 Files

* `website_logs.py` — Python script for data processing and analysis
* `website_logs.csv` — Original website log dataset
* `website_logs_clean.csv` — Cleaned and processed data

## 🎯 Learning Goal

Learn how to use **Python and Pandas** for data cleaning, processing, and basic analysis.

## 💡 Purpose

To practice working with CSV datasets and develop practical data-processing skills using Python.

## ▶️ How to Run

Make sure Python and Pandas are installed, then run:

```bash
python website_logs.py
```

The program will process the log data and generate `website_logs_clean.csv`.

## 📊 Key Analysis

The project analyzes:

* Top visited pages
* 404 error pages
* Most active IP addresses
* Cleaned website log records

## 📚 Skills Practiced

* Pandas DataFrames
* CSV file handling
* Data cleaning
* Duplicate removal
* Data filtering
* Value counting
* Date and time conversion
* Basic data analysis
