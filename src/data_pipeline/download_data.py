import yfinance as yf
from pathlib import Path

def download_prices(tickers, start="2010-01-01", end=None):
    data = yf.download(tickers, start=start, end=end)
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    data.to_csv("data/raw/prices.csv")
    return data
