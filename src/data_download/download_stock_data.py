# import yfinance as yf
# import pandas as pd
# from datetime import datetime
# import os

# # Define the stock ticker
# ticker_symbol = 'AAPL'  # Example: Apple Inc.

# # Define the specific date range
# start_date = datetime(2024, 6, 3)
# end_date = datetime(2024, 6, 4)  # 28

# # Download historical data
# data = yf.download(ticker_symbol, start=start_date, end=end_date)

# path = f'../data/{ticker_symbol}'
# if not os.path.exists(path):
#     os.makedirs(path)

# data_type = 'open_close'
# if not os.path.exists(f'{path}/{data_type}'):
#     os.makedirs(f'{path}/{data_type}')

# # Save data to a CSV file with a comment header
# filename = f'../data/{ticker_symbol}/{data_type}/{start_date.strftime("%Y-%m-%d")}_to_{end_date.strftime("%Y-%m-%d")}.csv'
# with open(filename, 'w') as file:
#     file.write(data.to_csv())
# print(f"Data saved to {filename}")


import os
import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the stock ticker and date range
ticker_symbol = 'AAPL'
start_date = datetime(2024, 6, 3)
end_date = datetime(2024, 6, 28)
data_type = 'open_close'

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the folder for downloads relative to the script's location
download_folder = os.path.join(script_dir, f'../data/{ticker_symbol}/{data_type}')

# Create the download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Download historical data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Construct the filename and save path
filename = f'{ticker_symbol}_{start_date.strftime("%Y-%m-%d")}_to_{end_date.strftime("%Y-%m-%d")}.csv'
file_path = os.path.join(download_folder, filename)

# Save data to CSV
with open(file_path, 'w') as file:
    data.to_csv(file, mode='a', index=True)

print(f"Data saved to {file_path}")
