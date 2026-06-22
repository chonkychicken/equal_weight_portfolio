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
