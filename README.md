# Python CSV Data Cleaner

A Python script that cleans and processes messy CSV data and exports the cleaned results to a new CSV file.

## Features

- Removes extra whitespace from names and emails
- Standardizes name capitalization
- Converts email addresses to lowercase
- Detects missing email addresses
- Handles invalid or missing age values
- Removes duplicate rows
- Exports cleaned data to a new CSV file
- Displays a summary of the cleaning process

## Example

Input:

Name,Email,Age
 razan ,RAZAN@GMAIL.COM,20
Sara, sara@gmail.com ,22

Output:

Name,Email,Age
Razan,razan@gmail.com,20
Sara,sara@gmail.com,22

## Technologies

- Python
- CSV module

## How to Run

1. Place the CSV file in the project folder and name it `messy_data.csv`.
2. Run:

python data_cleaner.py

3. The cleaned data will be saved as `cleaned_data.csv`.

## What I Learned

This project helped me practice working with CSV files, data cleaning, exception handling, duplicate detection, and reading and writing files with Python.