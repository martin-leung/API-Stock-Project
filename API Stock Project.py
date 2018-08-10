import json
import urllib.parse
import urllib.request
import os
from ast import literal_eval

url_base = "https://api.iextrading.com/1.0/"

#####################
#TICKER RELATED CODE#
#####################
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
            #print(ticker_url)
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
            print("\nLatest Headlines: \n")
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
            print("Table of last 5 days: \n")
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
        print("\nERROR: Invalid Command")
        ticker_menu()
####################
#END OF TICKER CODE#
####################

################
#PORTFOLIO CODE#
################
def portfolio_menu():
    print("\nPortfolio Manager\n")
    command = input("Options:\n    'V' - View Portoflio\n    'A' - Add Ticker\n    'D' - Delete Ticker\n    'Q' - Quit Portfolio\nCommand: ")
    if command.upper() == "V":
        view_portfolio()
    elif command.upper() == "A":
        #print("\nAdding to Portfolio\n")
        add_portfolio()
    elif command.upper() == "D":
        delete_port()
    elif command.upper() == "Q":
        main_menu()
    else:
        print("ERROR: Invalid Command")
        portfolio_menu()

def view_portfolio():
    print("\nCuurent Portfolio")
    with open('test.txt', 'r') as f:
        datastore = json.load(f)
    print("")
    for i in datastore:
        ticker_url = url_base +"stock/" + i + "/book"
        response = urllib.request.urlopen(ticker_url)
        data = json.loads(response.read())
        print(str(i).upper() + ": ")
        print("Total Shares: " + str((datastore[i]['total_shares']))+"   ")
        print("Total Price: " + str(round(float(datastore[i]['total_shares'])*data['quote']['latestPrice'],2))+"\n")
    portfolio_menu()
    
def add_helper():
    try:
        ticker = input("What ticker would you like to add to your portfolio? ")
        ticker_url = url_base +"stock/" + ticker + "/book"
        response = urllib.request.urlopen(ticker_url)
        data = json.loads(response.read())
        print("\nWould you like to add the following company? \n")
        print("Ticker: " + data['quote']['symbol'])
        print("Company Name: " + data['quote']['companyName'])
        print("Latest Price: " + str(data['quote']['latestPrice'])+"\n")
        while True:
            command = input("Yes (Y) or No (N): ")
            if command.upper() == "Y":
                return ticker
                break
            elif command.upper() == "N":
                return add_helper()
                break
            else:
                print("ERROR: Invalid Command")
    except:
        print("ERROR: Invalid Ticker")
        return add_helper()

def ammount_shares(ticker):
    while True:
        try:
            ammount = input("How many shares of " + ticker.upper()+ " do you want? ")
            if int(ammount) >= 1:
                return ammount
                break
            else:
                print("\nInvalid Ammount: Must be a integer and greater than 0\n")
        except:
            print("\nInvalid Ammount: Must be a integer and greater than 0\n")

def check_if_empty():
    #check if text file is empty and puts a {} in if it is
    if os.stat("test.txt").st_size == 0:
        new_file = {}
        with open('test.txt', 'w') as outfile:
            json.dump(new_file, outfile)
            
def add_json(ticker, ammount, price):
    check_if_empty()
    with open('test.txt', 'r') as f:
        datastore = json.load(f)

    if ticker not in datastore:
        new = {'total_shares' : ammount , 'total_price' : price, 'shares':[{'shares':
                ammount, 'price': price, 'total_ammount': float(price)*float(ammount)}]}
        datastore[ticker] = new
    else:
        datastore[ticker]['total_shares'] += ammount
        datastore[ticker]['total_price'] = datastore[ticker]['total_price'] + float(ammount)*float(price)
        new = {'shares':ammount, 'price': price, 'total_ammount': float(price)*float(ammount)}
        datastore[ticker]['shares'].append(new)
    with open('test.txt', 'w') as outfile:
        json.dump(datastore, outfile)
    outfile.close()
    
def add_portfolio():
    print("Add Shares:\n")
    ticker = add_helper()
    ammount = ammount_shares(ticker)
    ticker_url = url_base +"stock/" + ticker + "/book"
    response = urllib.request.urlopen(ticker_url)
    data = json.loads(response.read())
    while True:
        try:
            price = input("\nAt what price would you like to add these shares at? Current Price($" + str(data['quote']['latestPrice']) + ")- 'C' or your choice value: ")
            if price == "C" or price == "c":
                price = data['quote']['latestPrice']
                add_json(ticker, ammount, price)
                print("\n" + str(ammount) + " shares were added to portfolio for a total of $" + str(float(ammount)*float(price))+ ".\n")
                break
            elif float(price) >= 0:
                print("\n" + str(ammount) + " shares were added to portfolio for a total of $" + str(float(ammount)*float(price))+ ".\n")
                add_json(ticker, ammount, price)
                break
        except:
            print("ERROR: Invalid Command")
    portfolio_menu()

def delete_helper():
    try:
        ticker = input("What ticker would you like to delete from your portfolio? ")
        ticker_url = url_base +"stock/" + ticker + "/book"
        response = urllib.request.urlopen(ticker_url)
        data = json.loads(response.read())
        print("\nWould you like to add the following company? \n")
        print("Ticker: " + data['quote']['symbol'])
        print("Company Name: " + data['quote']['companyName'])
        print("Latest Price: " + str(data['quote']['latestPrice'])+"\n")
        while True:
            command = input("Yes (Y) or No (N): ")
            if command.upper() == "Y":
                return ticker
                break
            elif command.upper() == "N":
                return delete_helper()
                break
            else:
                print("ERROR: Invalid Command")
    except:
        print("ERROR: Invalid Ticker")
        return delete_helper()
    
def delete_port():
    print("Remove Shares:\n")
    check_if_empty()
    with open('test.txt', 'r') as f:
        datastore = json.load(f)
    while True:
        ticker = delete_helper()
        if ticker in datastore:
            print()
            ammount = ammount_shares(ticker)
            if int(ammount) > int(datastore[ticker]['total_shares']):
                print("You only have",str(datastore[ticker]['total_shares']),ticker.upper(), "shares in your portfolio\n", sep = " ")
            else:
                temp = int(datastore[ticker]['total_shares'])
                datastore[ticker]['total_shares'] = str(temp - int(ammount))
                print("\nDeleted " + ammount + " " + ticker.upper() + " from portfolio")
                print(datastore[ticker]['total_shares']+ " " + ticker.upper() + " left in portfolio\n")
                with open('test.txt', 'w') as outfile:
                    json.dump(datastore, outfile)
                outfile.close()
                portfolio_menu()
                break
        else:
            print("\nTicker doesn't exist in portfolio\n")

########################
#END OF PORTOFOLIO CODE#
########################


###########################
#MAIN MENU / STARTING MENU#
###########################
def main_menu():
    print("\nMAIN MENU\n")
    command =  input("Options: \n    'L' - Lookup Ticker\n    'P' - Portfolio\n    'Q' - Quit Program\nCommand: ")
    if command.upper() == "L":
        ticker_menu()
    elif command.upper() == "P":
        portfolio_menu()
    elif command.upper() == "Q":
        print("\nClosing App")
    else:
        print("\nERROR: Invalid Command")
        main_menu()

if __name__ == "__main__":
    print("Welcome to your Portfolio Manager")
    print("Portfolio Manager is still in progress.")
    main_menu()

