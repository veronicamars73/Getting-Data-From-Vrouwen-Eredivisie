# Eredivisie Vrouwen Stats Web Scraper

This repository contains a Python program to scrape, clean, and save data from the Eredivisie Vrouwen Stats page on FBref.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [Authorship](#authorship)

## Introduction

The Eredivisie Vrouwen Stats Web Scraper extracts all tables from the Eredivisie Vrouwen Stats page on FBref, cleans the data by handling missing values and converting data types, and saves the cleaned data to CSV files for future analysis.

## Requirements

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, `pandas`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/eredivisie-vrouwen-stats-scraper.git
    cd eredivisie-vrouwen-stats-scraper
    ```

2. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the script:

    ```sh
    python web_scrape.py
    ```

3. The cleaned data will be saved to CSV files in the current directory.

## Functionality

### Functions

- `fetch_page_content(url)`: Fetches and parses the webpage content using BeautifulSoup.
- `extract_tables(soup)`: Extracts all tables from the webpage and converts them into pandas DataFrames.
- `clean_data(dataframes)`: Cleans the extracted data by handling missing values, removing columns with no information, and converting data types.
- `save_to_csv(dataframes, prefix='table')`: Saves the cleaned DataFrames to CSV files.

### Main Function

- `main(url)`: Orchestrates the entire web scraping process by calling the above functions in sequence.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.

## Authorship

Repository developed by Lisandra Melo (<lisandramelo34@gmail.com>).