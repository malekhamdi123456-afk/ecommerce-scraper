# E-Commerce Scraper

A Python script using Selenium that automates logging into saucedemo.com, 
sorting products by different criteria, and scraping product data into a CSV file.

## What it does

1. Opens Chrome and navigates to https://www.saucedemo.com/
2. Logs in with test credentials (standard_user / secret_sauce)
3. Selects 2 sort options from the product dropdown (Name Z-A, Price low-high)
4. Scrapes the first 3 products after each sort — 6 total rows across both sorts
5. Writes results to prod.csv, semicolon-delimited, 4 columns (Sort Option, Product Name, Price, Status)
6. Logs every action to scraping.log with timestamps
7. Saves a timestamped screenshot on any of 4 possible error points (login, password, dropdown, scraping)
8. Uses a 10-second explicit wait for page elements before timing out

## Requirements

- Python 3
- selenium (`pip install selenium`)
- Chrome + matching ChromeDriver

## How to run

python ecommerce_scraper.py

## Output files

- prod.csv — 1 header row + 6 data rows
- scraping.log — 1 entry for login, 2 for sort selections, 6 for successful scrapes, plus any errors
- error_*.png — one screenshot per failure, filename includes exact timestamp (YYYYMMDD_HHMMSS)
