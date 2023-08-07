# Welcome to my market winners and losers twitter (now known as X) bot. Every day when the market closes,
# this main.py file will run automatically using an online service called "Python Anywhere". This program uses the Alpha Advantage Top
# Gainers and Losers API, the Alpha Advantage Ticker Search API, along with Twitter API v2.0 to do this.
# The Twitter account is @MarketWandL

#NOTE: I HAVE CHANGED ALL API KEY VALUES FOR THIS PUBLIC VERSION HOSTED ON GIT HUB

import requests  # requests is a package that allows for sending HTTP requests in python
import tweepy  # tweepy is a 3rd party package that is designed to allow communication with the Twitter API
import datetime  # because the market isn't open on saturdays or sundays, and Python Anywhere can only be set to operate daily,
# we have to check the day of the week using this package

# the today variable is the actual date, and we use that variable to then get the specific day of the week. dayOfWeek it can either be 0, 1, 2, 3, 4, 5, or 6. 5 represents saturday and 6 represents sunday
today = datetime.date.today()
dayOfWeek = today.weekday()
print(dayOfWeek)

# this if statement is made to check if the day is either saturday or sunday. If it isn't, it will run the rest of the code
if dayOfWeek != 5 and dayOfWeek != 6:
    # This url is used to call the api, the parameters for this include the title of the API "TOP_GAINERS_LOSERS", and the api key
    urlCompanyData = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=ALPHA_ADVANTAGE_KEY'
    # This function call returns as a JSON file
    rData = requests.get(urlCompanyData)
    print(rData.status_code)

    # These four variables get the winner and loser data, specifically the percentages and Tickers for each of them
    winPercent = rData.json()["top_gainers"][0]["change_percentage"]
    winTick = rData.json()["top_gainers"][0]["ticker"]
    losePercent = rData.json()["top_losers"][0]["change_percentage"]
    loseTick = rData.json()["top_losers"][0]["ticker"]

    # This part uses another API within alpha advantage called "Ticker Search" to figure out the actual names of the company based on the tickers provided in the last API
    # This is url and api call is for the winner
    urlCompanyName = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={winTick}&apikey=ALPHA_ADVANTAGE_KEY'
    rName = requests.get(urlCompanyName)
    # rName is again a JSON file
    winName = rName.json()["bestMatches"][0]["2. name"]

    # Same thing except it's getting the name for the loser company
    urlCompanyName = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={loseTick}&apikey=ALPHA_ADVANTAGE_KEY'
    rName = requests.get(urlCompanyName)
    loseName = rName.json()["bestMatches"][0]["2. name"]

    # These five variables are important keys that are required for using the Twitter API
    bearer = "fake_bearer_key"
    consumer = "fake_consumer_key"
    consumer_secret = "fake_consumer_secret_key"
    access = "fake_access_key"
    access_secret = "fake_access_secret_key"

    # This API call is used to verify yourself before making any further calls
    client = tweepy.Client(consumer_key=consumer, consumer_secret=consumer_secret, access_token=access,
                           access_token_secret=access_secret)

    # This string is the text that will be tweeted out
    tweet_text = f"Today's big market winner is {winName} ({winTick}), with the company ending the day up {winPercent}. As for the biggest loser, {loseName} ({loseTick}) finished the day down {losePercent} during today's market."

    # This API call will post the string to @MarketWandL
    requests = client.create_tweet(text=tweet_text)
