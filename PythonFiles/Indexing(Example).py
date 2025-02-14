import yfinance as yf
import numpy as np
import pandas as pd

# Dictionary to store stock risk scores
stock_risk_index = {}

def fetch_stock_data(stock_ticker, period="1mo"):
    """Fetch stock market data from Yahoo Finance."""
    stock = yf.Ticker(stock_ticker)
    df = stock.history(period=period)
    return df['Close'] if not df.empty else None

def predict_risk(stock_ticker):
    """Estimate stock investment risk using real market data and store it in an index."""
    stock_prices = fetch_stock_data(stock_ticker)
    
    if stock_prices is None or len(stock_prices) < 2:
        return f"Not enough data to compute risk for {stock_ticker}."

    # Compute daily price changes
    daily_returns = stock_prices.pct_change().dropna()

    # Count how many days stock went up
    up_days = (daily_returns > 0).sum()
    total_days = len(daily_returns)

    # Binomial Risk Calculation
    risk_score = 1 - (up_days / total_days)  # More down days → Higher risk
    risk_score = round(risk_score, 2)

    # Store in index
    stock_risk_index[stock_ticker] = risk_score
    
    return f"Stock Market Risk for {stock_ticker}: {risk_score} ({up_days} up days in {total_days} days)"

def get_risk_score(stock_ticker):
    """Retrieve risk score for a specific stock."""
    return stock_risk_index.get(stock_ticker, "Stock not found")

def get_all_risk_scores():
    """Return all stock risk scores as a structured DataFrame."""
    return pd.DataFrame(stock_risk_index.items(), columns=["Stock", "Risk Score"])

# ✅ Example Usage: Predict Risk for Multiple Stocks
stocks = ["TSLA", "AAPL", "GOOGL", "MSFT"]

for stock in stocks:
    print(predict_risk(stock))

# Retrieve a specific stock's risk score
print("\nFetching risk score for AAPL:")
print(get_risk_score("AAPL"))

# Display all risk scores in a structured format
print("\nAll Stock Risk Scores:")
print(get_all_risk_scores())