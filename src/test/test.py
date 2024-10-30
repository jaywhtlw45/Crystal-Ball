import yfinance as yf
from datetime import datetime

ticker_symbol = 'MSFT'
msft = yf.Ticker(ticker_symbol)

start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 1, 31)

# get stock info
data = yf.download(ticker_symbol, start = start_date, end = end_date)
print(type(data))
# print(data)
