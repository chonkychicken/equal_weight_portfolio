# RMK: if this isn't working in VSCode, go to settings `Ctrl + ,` 
# and change `Execute in File Dir` also make sure your portfolio.xlsx isn't open

import downloader as dw

def main():
    df = dw.read_tickers("tickers.csv")
    df = dw.validate_tickers(df)

    df["Price"] = dw.get_prices(df["Ticker"])
    df = df.dropna(subset=["Price"])

    portfolio_size = float(input("Portfolio value: "))
    df = dw.calculate_portfolio(df, portfolio_size)

    dw.export(df, "portfolio.xlsx")
    #print(df)

if __name__ == "__main__":
    main()