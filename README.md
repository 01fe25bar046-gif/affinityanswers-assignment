# AffinityAnswers Internship Assignment

This repository contains solutions for the coding tasks provided as part of the AffinityAnswers internship application.

## Task 1 - MDComputers Product Scraper

A Python script that searches MDComputers for a given product and extracts product details such as:

- Product name
- Price
- Availability
- Product URL

### Requirements

Install the required Python packages:

pip install -r requirements.txt

### Usage

python mdcomputers_scraper.py "external harddrive"

You can replace "external harddrive" with any search term.

## Task 2 - S&P 500 Company Data Shell Script

A shell script that downloads the S&P 500 constituents CSV and outputs:

- Company name
- Headquarters location
- Founding year

The results are sorted by founding year.

### Usage

On Linux/WSL:

chmod +x sp500_companies.sh
./sp500_companies.sh

## Files

- `mdcomputers_scraper.py` - MDComputers web scraper
- `sp500_companies.sh` - S&P 500 CSV processing script
- `requirements.txt` - Python dependencies
