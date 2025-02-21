import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm, binom, bernoulli

# Fetch stock data (Example: AAPL)
stock = "AAPL"
df = yf.download(stock, start="2023-01-01", end="2024-01-01")

# Compute daily returns
df["Daily Return"] = df["Close"].pct_change().dropna()

# --- 1. Normal Distribution: Stock Returns ---
mu, sigma = df["Daily Return"].mean(), df["Daily Return"].std()
x = np.linspace(df["Daily Return"].min(), df["Daily Return"].max(), 100)
pdf = norm.pdf(x, mu, sigma)

# Matplotlib Plot: Normal Distribution
plt.figure(figsize=(10, 5))
plt.hist(df["Daily Return"], bins=50, density=True, alpha=0.6, color="blue", edgecolor="black")
plt.plot(x, pdf, color="red", label="Normal Distribution Fit")
plt.axvline(mu, color="green", linestyle="dashed", label=f"Mean: {mu:.4f}")
plt.axvline(mu + sigma, color="orange", linestyle="dashed", label=f"+1 Std Dev")
plt.axvline(mu - sigma, color="orange", linestyle="dashed", label=f"-1 Std Dev")
plt.title("Stock Returns Distribution (Normal)")
plt.xlabel("Daily Return")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()

# --- 2. Binomial Distribution: Price Jumps ---
n_days = 252  # Number of trading days in a year
p_jump = 0.02  # Probability of a large jump in price per day

# Simulate binomial events (1=Jump, 0=No Jump)
binomial_data = binom.rvs(n=1, p=p_jump, size=n_days)

# Seaborn: Binomial Distribution
plt.figure(figsize=(8, 5))
sns.histplot(binomial_data, discrete=True, color="purple", bins=3)
plt.title("Binomial Distribution: Stock Price Jumps")
plt.xlabel("Jump Event (1=Jump, 0=No Jump)")
plt.ylabel("Frequency")
plt.show()

# --- 3. Bernoulli Distribution: Buy/Sell Decisions ---
p_buy = 0.6  # Probability of buying stock

# Simulate investor decisions (1=Buy, 0=Sell)
buy_sell_decisions = bernoulli.rvs(p=p_buy, size=n_days)

# Plotly: Bernoulli Distribution
fig = px.histogram(x=buy_sell_decisions, nbins=2, title="Bernoulli Distribution: Buy/Sell Decisions",
                   labels={'x': "Decision (1=Buy, 0=Sell)", 'y': "Frequency"},
                   color_discrete_sequence=['blue'])

fig.show()

# --- 4. Portfolio Vector Representation ---
# Assume a portfolio of 3 stocks with given weights
portfolio_weights = np.array([0.5, 0.3, 0.2])  # 50% AAPL, 30% MSFT, 20% TSLA
portfolio_returns = np.array([0.07, 0.05, 0.09])  # Expected returns of stocks

# Compute portfolio return as a dot product
expected_portfolio_return = np.dot(portfolio_weights, portfolio_returns)

print(f"Expected Portfolio Return: {expected_portfolio_return:.2f}")

# Matplotlib: Portfolio Weights
stocks = ["AAPL", "MSFT", "TSLA"]
plt.figure(figsize=(7, 5))
plt.bar(stocks, portfolio_weights, color=["blue", "green", "red"])
plt.title("Stock Portfolio Weights")
plt.xlabel("Stock")
plt.ylabel("Weight in Portfolio")
plt.show()