import pandas as pd

NASDAQ_TICKERS_URL = "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt"

def fetch_nasdaq_tickers():
    df = pd.read_csv(NASDAQ_TICKERS_URL, sep='|')
    df = df[df['Symbol'] != 'File Creation Time']
    tickers = df['Symbol'].tolist()
    print(f"Fetched {len(tickers)} NASDAQ tickers.")
    return tickers

def save_tickers_to_csv(tickers, filename="nasdaq_tickers.csv"):
    df = pd.DataFrame(tickers, columns=['Ticker'])
    df.to_csv(filename, index=False)
    print(f"Saved tickers to {filename}")

if __name__ == "__main__":
    tickers = fetch_nasdaq_tickers()
    save_tickers_to_csv(tickers)
