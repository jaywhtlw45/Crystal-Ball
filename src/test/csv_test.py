import yfinance as yf
from datetime import datetime
import pandas as pd

# Define the specific date range
start_date = datetime(2024, 6, 3)
end_date = datetime(2024, 6, 4)

# Download historical data
ticker_symbol = 'AAPL'
data = yf.download(ticker_symbol, start=start_date, end=end_date)

print(data.head())

file_path = 'data.csv'

with open(file_path, 'w') as file:
    data.to_csv(file, mode='a', index=True)
