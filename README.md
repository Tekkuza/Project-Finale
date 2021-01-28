# Stocker Prep

## Description:

This tool uses the Financial Modeling Prep API to scrape and collect stock information. This requires the creation of an account, and use of an API token to collect data. 

### Plans:
- Resolve automation and csv storage of shortlisted companies.
- Perform percentage calculations of stock change (Every 3-6 hours, +/-, e.g. Stock A -10.5%)
  - Will implement write feature to store stock data for reference.

### Classes:
1) Stock scraper:
- This class collects and requests data from the API. This is where you can select the type of information to scrape.
2) Menu:
- This class ultimately was to become a selection area allowing you to choose the API searches to perform, as well as calculations. 
3) Storage / Calculation:
- This class aimed to execute csv storage and calculation, but due to time constraints, it wasn't completed. This will be followed up.
