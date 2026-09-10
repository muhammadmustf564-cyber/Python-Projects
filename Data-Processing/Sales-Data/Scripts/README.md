# Sales-Data — Scripts

This folder contains the Python script used to clean and process a dirty sales dataset using **Pandas**.

## Files

* `sales_cleaning.py` — Python script that loads the dirty sales data, cleans it, calculates total amounts, and exports the cleaned data.
* `sales_dirty_data.csv` — Raw sales dataset containing duplicate and missing values.

## Data Cleaning Operations

The script performs the following tasks:

* Removes duplicate records
* Fills missing `Price` values with the mean price
* Fills missing `Quantity` values with the mode
* Creates a `Total_Amount` column
* Exports cleaned data to CSV
* Exports cleaned data to Excel
* Displays the cleaned dataset in the terminal

## Output Files

After running the script, it creates:

* `sales_clean_data.csv`
* `sales_clean_data.xlsx`

## Technologies Used

* Python
* Pandas

## Purpose

This project demonstrates practical **data cleaning and processing using Python and Pandas**, including handling missing values, removing duplicates, creating calculated columns, and exporting cleaned datasets.
