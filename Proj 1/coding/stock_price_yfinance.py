# filename: stock_price_yfinance.py

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import date

# Fetch data from Yahoo Finance
start = date(date.today().year, 1, 1)  # start date (Year-to-Date)

nvda = yf.download('NVDA', start)
tsla = yf.download('TSLA', start)

# Create a dataframe with daily returns
data = pd.DataFrame({
    'NVDA': nvda['Adj Close'].pct_change(),
    'TSLA': tsla['Adj Close'].pct_change()
})

# Generate a cumulative returns graph
cumulative_returns = (1 + data.fillna(0)).cumprod()
cumulative_returns.plot()

plt.title('YTD Cumulative Returns for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Growth of $1 investment')
plt.grid(True)
plt.show()