import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Watchlist of companies
tickers = ["UI", "KITT", "IBM", "LAC", "PLTR", "META", "MSFT", "JOBY", "RGTI", "AVAV", "RDW"]

data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    price = info.get('currentPrice', 'N/A')
    prev_close = info.get('previousClose', 'N/A')
    name = info.get('shortName', 'N/A')
    
    if price != 'N/A' and prev_close != 'N/A':
        change_pct = round(((price - prev_close) / prev_close) * 100, 2)
    else:
        change_pct = 'N/A'
    
    data.append({
        'Ticker': ticker,
        'Company': name,
        'Price ($)': price,
        'Prev Close ($)': prev_close,
        'Change (%)': change_pct
    })

df = pd.DataFrame(data)
print(df.sort_values(by='Change (%)', ascending=False))

# Chart
df_sorted = df.sort_values(by='Change (%)', ascending=False)
colors = ['green' if x >= 0 else 'red' for x in df_sorted['Change (%)']]

plt.figure(figsize=(10, 6))
plt.barh(df_sorted['Ticker'], df_sorted['Change (%)'], color=colors)
plt.xlabel('Change (%)')
plt.title('Daily % Change - Portfolio Watchlist')
plt.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()
