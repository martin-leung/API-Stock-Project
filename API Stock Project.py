import json
import urllib.parse
import urllib.request

url_base = "https://api.iextrading.com/1.0/"

def ticker_lookup():
    while True:
        try:
            ticker = input("What symbol do you want to look up? (AAPL, MSFT, ETC.) or 'Q' to quit: ")
            if ticker.upper() == "Q":
                print("Quitting Ticker Look Up")
                break
            ticker_url = url_base +"stock/" + ticker + "/book"
            #print(ticker_url)
            response = urllib.request.urlopen(ticker_url)
            data = json.loads(response.read())
            print()
            print("Ticker: " + data['quote']['symbol'])
            print("Company Name: " + data['quote']['companyName'])
            print("Latest Price: " + str(data['quote']['latestPrice'])+"\n")
        except:
            print("Invalid Ticker")



if __name__ == "__main__":
    ticker_lookup()
    

