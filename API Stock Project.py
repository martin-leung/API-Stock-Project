import json
import urllib.parse
import urllib.request

url_base = "https://api.iextrading.com/1.0/"

def ticker_lookup():
    print("\nTICKER LOOK UP")
    while True:
        try:
            ticker = input("What symbol do you want to look up? (AAPL, MSFT, etc.) or 'Q' to quit: ")
            if ticker.upper() == "Q":
                print("\nQuitting Ticker Look Up")
                ticker_menu()
                break
            ticker_url = url_base +"stock/" + ticker + "/book"
            print(ticker_url)
            response = urllib.request.urlopen(ticker_url)
            data = json.loads(response.read())
            #print(data)
            print()
            print("Ticker: " + data['quote']['symbol'])
            print("Company Name: " + data['quote']['companyName'])
            print("Latest Price: " + str(data['quote']['latestPrice'])+"\n")
        except:
            print("Invalid Ticker")


def ticker_news():
    print("\nTICKER NEWS SECTION:")
    while True:
        try:
            ticker = input("Ticker (AAPL, MSFT, etc.) News or 'Q' to quit: ")
            if ticker.upper() == "Q":
                print("Quitting Ticker News")
                ticker_menu()
                break
            ticker_url = url_base + "stock/" + ticker + "/news/last/3"
            response = urllib.request.urlopen(ticker_url)
            data = json.loads(response.read())
            print("Latest Headlines\n")
            #print(data)
            for each in data:
                print("Headline: " + '"' + each['headline'] + '"')
                print("URL: " + each['url'] + "\n")
        except:
            print("Invalid Ticker")

def ticker_chart():
    print("\nTICKER CHARTS:")
    while True:
        try:
            ticker = input("Ticker (AAPL, MSFT, etc.) Chart or 'Q' to quit: ")
            if ticker.upper() == "Q":
                print("Quitting Ticker News\n")
                ticker_menu()
                break
            ticker_url = url_base + "/stock/" + ticker + "/chart"
            response = urllib.request.urlopen(ticker_url)
            data = json.loads(response.read())
            #print(ticker_url)
            print()
            j = 0
            for i in data:
                if j >= 15:
                    print(data[j]['date'], end = "  |  ")
                j += 1
            print()
            j = 0
            for i in data:
                if j >= 15:
                    print("    " + str(data[j]['open']), end = "     ") 
                j += 1
            print()
        except:
            print("Invalid Ticker")

def ticker_calc():
    print("\nTICKER CALCULATOR:")
    while True:
        try:
            ticker = input("Ticker (AAPL, MSFT, etc.) Chart: ")
            if ticker.upper() == "Q":
                print("Quitting Calculator\n")
                break
        except:
            print("Invalid Ticker")

def ticker_menu():
    print("\nTicker Information Menu\n")
    command = input("Options:\n    'P' - Current Price\n    'N' - News\n    'C' - Charts\n    'Q' - Quit Lookup\nCommand: ")
    if command.upper() == "P":
        ticker_lookup()
    elif command.upper() == "N":
        ticker_news()
    elif command.upper() == "C":
        ticker_chart()
    elif command.upper() == "Q":
        main_menu()
    else:
        print("Ticker Menu ERROR")

def portfolio():
    print("\nPortfolio Manager (In-Progress) \n")
    command = input("Options:\n    'V' - View Portoflio\n    'A' - Add Ticker\n    'D' - Delete Ticker\n    'Q' - Quit\nCommand: ")
    

def main_menu():
    print("\nMAIN MENU\n")
    command =  input("Options: \n    'L' - Lookup Ticker\n    'P' - Portfolio\n    'Q' - Quit Program\nCommand: ")
    if command.upper() == "L":
        ticker_menu()
    elif command.upper() == "P":
        portfolio()
    elif command.upper() == "Q":
        print("\nClosing App")
    else:
        print("\nERROR: Invalid Command")
        main_menu()

if __name__ == "__main__":
    print("Welcome to your Portfolio Manager")
    main_menu()

