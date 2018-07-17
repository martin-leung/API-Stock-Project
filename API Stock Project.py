import json
import urllib.parse
import urllib.request

url_base = "https://api.iextrading.com/1.0/"

def ticker_lookup():
    print("TICKER LOOK UP")
    while True:
        try:
            ticker = input("What symbol do you want to look up? (AAPL, MSFT, etc.) or 'Q' to quit: ")
            if ticker.upper() == "Q":
                print("\nQuitting Ticker Look Up")
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
            ticker = input("Ticker (AAPL, MSFT, etc.) News: ")
            if ticker.upper() == "Q":
                print("Quitting Ticker News")
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
            ticker = input("Ticker (AAPL, MSFT, etc.) Chart: ")
            if ticker.upper() == "Q":
                print("Quitting Ticker News")
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

if __name__ == "__main__":

    ticker_lookup()
    ticker_news()
    ticker_chart()
    

