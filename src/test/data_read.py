import pandas as pd

# Load the data back into a DataFrame
data = pd.read_csv("data.csv", index_col=0, parse_dates=True)

# Display the first few rows to verify
print(data.head())
