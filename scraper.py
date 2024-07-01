import requests
from bs4 import BeautifulSoup
import pandas as pd

# For data cleaning
import numpy as np

def fetch_page_content(url):
    """
    Fetch the content of the webpage.

    Parameters:
    url (str): URL of the webpage to fetch content from.

    Returns:
    BeautifulSoup object: Parsed HTML content of the webpage.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage content. Status code: {response.status_code}")
    return BeautifulSoup(response.content, 'html.parser')

def extract_tables(soup):
    """
    Extract all tables from the parsed HTML content.

    Parameters:
    soup (BeautifulSoup): Parsed HTML content.

    Returns:
    list of DataFrame: List of pandas DataFrames containing table data.
    """
    tables = soup.find_all('table')
    dataframes = []
    for table in tables:
        df = pd.read_html(str(table))[0]
        dataframes.append(df)
    return dataframes

def clean_data(dataframes):
    """
    Clean the extracted data.

    Parameters:
    dataframes (list of DataFrame): List of pandas DataFrames to clean.

    Returns:
    list of DataFrame: List of cleaned pandas DataFrames.
    """
    cleaned_dfs = []
    for df in dataframes:
        # Drop rows where all elements are NaN
        df.dropna(how='all', inplace=True)
        
        # Drop columns where all elements are NaN
        df.dropna(axis=1, how='all', inplace=True)
        
        # Convert numerical columns to appropriate data types
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        
        cleaned_dfs.append(df)
    return cleaned_dfs

def save_to_csv(dataframes, prefix='table'):
    """
    Save the cleaned data to CSV files.

    Parameters:
    dataframes (list of DataFrame): List of cleaned pandas DataFrames.
    prefix (str): Prefix for the CSV filenames.
    """
    for i, df in enumerate(dataframes):
        df.to_csv(f"data/{prefix}_{i+1}.csv", index=False)
        
def main(url):
    """
    Main function to orchestrate the web scraping process.

    Parameters:
    url (str): URL of the webpage to scrape data from.
    """
    soup = fetch_page_content(url)
    dataframes = extract_tables(soup)
    cleaned_dataframes = clean_data(dataframes)
    save_to_csv(cleaned_dataframes)

if __name__ == "__main__":
    url = "https://fbref.com/en/comps/195/Eredivisie-Vrouwen-Stats"
    main(url)