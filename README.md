# TwitterWinAndLosePublic

This repository contians the main.py file for my stock market winners and losers twitter bot. Every weekday when the market closes, the bot will tweet the stocks that
gained and lost the most value during that day's trading period. This includes the name of the company, the ticker, and the percentage change in the stock. 

This was accomplished using two API's: Alpha Advantage, which holds the stock information, and Twitter (X) API v2.0, for posting it to twitter.

My computer has a task scheduled for 1:00pm pacific time that runs an executable version of main.py. The code handles if the data should be posted based on the day of the week.

The twitter account is @MarketWandL, and you can see it by pressing this link [here](https://twitter.com/MarketWandL)

The main.py file was coded in entirely in Python.

Thanks for taking the time to read this, make sure to like and follow @MarketWandL!

*NOTE: The version here on GitHub is not the exact file that is being run, I did this to conciel the API keys from the public.
