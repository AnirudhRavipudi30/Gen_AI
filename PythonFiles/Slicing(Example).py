import yfinance as yf
import numpy as np
import pandas as pd

# Dictionary to store stock risk scores
stock_risk_index = {}

def fetch_stock_data(stock_ticker, period="1mo", days=None):
    """Fetch stock market data from Yahoo Finance, with optional slicing."""
    stock = yf.Ticker(stock_ticker)
    df = stock.history(period=period)
    
    if df.empty:
        return None

    stock_prices = df['Close']

    # 🔥 Apply slicing if `days` parameter is provided
    if days:
        stock_prices = stock_prices[-days:]  # Select only the last 'days' values

    return stock_prices

def predict_risk(stock_ticker, days=None):
    """Estimate stock investment risk using real market data and store it in an index."""
    stock_prices = fetch_stock_data(stock_ticker, days=days)
    
    if stock_prices is None or len(stock_prices) < 2:
        return f"Not enough data to compute risk for {stock_ticker}."

    # Compute daily price changes
    daily_returns = stock_prices.pct_change().dropna()

    # Count how many days stock went up
    up_days = (daily_returns > 0).sum()
    total_days = len(daily_returns)

    # Compute risk score
    risk_score = 1 - (up_days / total_days)  # More down days → Higher risk
    risk_score = round(risk_score, 2)

    # 🔥 Store in index
    stock_risk_index[stock_ticker] = risk_score  

    return f"Stock Market Risk for {stock_ticker}: {risk_score} ({up_days} up days in {total_days} days)"

def get_risk_score(stock_ticker):
    """Retrieve risk score for a specific stock."""
    return stock_risk_index.get(stock_ticker, "Stock not found")

def get_all_risk_scores():
    """Returns all stock risk scores as a DataFrame for structured analysis."""
    df = pd.DataFrame(stock_risk_index.items(), columns=["Stock", "Risk Score"])
    return df.sort_values(by="Risk Score", ascending=False)  # Sort by risk level

def get_top_n_risky_stocks(n):
    """Get the top N riskiest stocks using slicing."""
    df = get_all_risk_scores()
    return df.iloc[:n]  # 🔥 Slicing to get top N rows

def get_bottom_n_safe_stocks(n):
    """Get the bottom N safest stocks using slicing."""
    df = get_all_risk_scores()
    return df.iloc[-n:]  # 🔥 Slicing to get last N rows