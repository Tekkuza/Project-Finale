import requests
import pandas as pd

    # """
    # API Key: ee2563866b5a51cc57cf4a7ade8bac7a
    # API Passcode 
    # Data provided by Financial Modeling Prep at https://financialmodelingprep.com/developer/docs/
    #Reference https://medium.com/swlh/automating-your-stock-portfolio-research-with-python-for-beginners-912dc02bf1c2
    # """

#API Log-in
api_token = 'ee2563866b5a51cc57cf4a7ade8bac7a'
api_url = 'https://financialmodelingprep.com/api/v3/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

class stock_ticker:
    def __init__(self):
        self.df = None
#Scraper feature - Collects data from Financial Modeling Prep.
    def getdata(self, stock):
        company_quote = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock}?apikey={api_token}")
        company_quote = company_quote.json()
        share_price = float("{0:.2f}".format(company_quote[0]['price']))

        BS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{stock}?period=quarter&apikey={api_token}")
        BS = BS.json()

        #Total Debt Calculation
        debt = float("{0:.2f}".format(float(BS['financials'][0]['Total debt'])/10**9))
        #Total Cash
        cash = float("{0:.2f}".format(float(BS['financials'][0]['Cash and short-term investments'])/10**9))
    #For pulling stock data from website.

        #Income statements
        IS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}?period=quarter&apikey={api_token}")
        IS = IS.json()   
        #Recent Quarterly Revenue
        qRev = float("{0:.2f}".format(float(IS['financials'][0]['Revenue'])/10**9))

        # Company Profile Group of Items
        company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}?apikey={api_token}")
        company_info = company_info.json()

        # Chief Executive Officer
        ceo = company_info['profile']['ceo']

        return(share_price, debt, cash, qRev, ceo)
    
    def complete_dataframe(self):
        disorg_ticks = ('AAPL', 'MSFT', 'TSLA', 'AMZN', 'FB', 'NVDA')
        tickers = sorted(disorg_ticks)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()


    def aapl_dataframe(self):
        tickers = ('AAPL',)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()


    def msft_dataframe(self):
        disorg_ticks = ('MSFT',)
        tickers = sorted(disorg_ticks)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()


    def tsla_dataframe(self):
        tickers = ('TSLA',)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()


    def amzn_dataframe(self):
        tickers = ('AMZN',)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()

    def fb_dataframe(self):
        tickers = ('Facebook')
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()    

    def nvda_dataframe(self):
        tickers = ('NVDA',)
        data = map(self.getdata, tickers)
        df = pd.DataFrame(data,
            columns=['Share Price', 'Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
            index=tickers)
        self.df = df #Saves API calls.
        print(df)
        menu_restart = input("Would you like to return to the menu?: \n Y/N")
        if menu_restart.lower() == "Y":
            mainframe.menu_list()
        if menu_restart.lower() == "N":
            mainframe.menu_list()
# Stock.complete_dataframe()

#Type stock ticker symbol.

class Terminal(stock_ticker):
    def __init__(self):
        self.terminal = None
        super().__init__()

    def menu_list(self):    

        print("Welcome to Financial Modeling Prep.") 
        #Login command()
        print("---------------------------")
        print(f"Your API token is {api_token}\n What would you like to do today?")
        print("1. View shortlisted stocks")
        print("2. View Apple Stock")
        print("3. View Microsoft Stock")
        print("4. View Tesla Stock")
        print("5. View Amazon Stock")
        print("6. Log out")
        print("---------------------------")
        menu_options = int(input("What would you like to do today? "))
        
        if menu_options != 0:
            if menu_options == 1:
                #Lists all stock options shortlisted
                print("Checking current stock list..")
                mainframe.complete_dataframe()
        
            #Selects Apple stock for viewing
            elif menu_options == 2:
                print("Fetching Apple Inc List..")
                mainframe.aapl_dataframe()
        
            #Selects Microsoft stock for viewing
            elif menu_options == 3:
                print("Fetching Microsoft Corp. List..")
                mainframe.msft_dataframe()
            
            #Selects Tesla stock for viewing
            elif menu_options == 4:
                print("Fetching Tesla Inc. List..")
                mainframe.tsla_dataframe()
            
            #Selects Amazon stock for viewing.
            elif menu_options == 5:
                print(": Fetching Amazon.com Inc. List..")
                mainframe.amzn_dataframe()
            #Log out
            elif menu_options == 6:
                print("Thank you for using Financial Modeling Prep.")
            else:
                print("Error.\nThis option is unavailable.\nPlease select any option from 1 to 6.")
                mainframe.menu_list()
                
mainframe = Terminal()
mainframe.menu_list()
