import pandas as pd
import yfinance as yf
import numpy as np

def read_tickers(filename):
    '''
    reads a .csv file with stock symbols (tickers)

    example: 
    Ticker
    AAPL
    MSFT
    SPCX
    '''
    return pd.read_csv(filename)

def validate_tickers(df):
    df = df.dropna(subset=["Ticker"]).drop_duplicates(subset=["Ticker"])
    if df.empty:
        raise ValueError("No valid tickers found")
    #print(tickers)
    return df

def get_prices(tickers):
    prices = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            price = stock.fast_info.get("lastPrice", np.nan)

            if price is None:
                price = np.nan

            prices.append(price)
        except Exception:
            prices.append(np.nan)
    return prices
    
def calculate_portfolio(df, portfolio_size):
    df = df.copy()
    n = len(df)
    if portfolio_size <= 0:
        raise ValueError("Portfolio value must be positive.")
    if n == 0:
        raise ValueError("No valid tickets after filtering")
    
    # the equal weights part
    allocation = portfolio_size/n
    df["Allocation"] = allocation
    df["Shares"] = np.floor(df["Allocation"]/df["Price"])
    df["Cost"] = df["Shares"]*df["Price"]
    df["Cash Left"] = df["Allocation"]-df["Cost"]
    print(f"Total Cash Spent: {round(df["Cost"].sum(), 2)}")
    print(f"Total Cash Leftover: {round(df["Cash Left"].sum(),2)}")
    #print(df)
    return df

def export(df, filename):
    df.to_excel(filename, index=False)
    #print(df)
