"""BTC RSI Predictor

Reads historical closing prices from a CSV file and computes the 
Relative Strength Index (RSI). Based on the latest RSI value it
prints a simple buy/sell/hold recommendation.

Usage: python btc_rsi_predictor.py data/btc_prices_sample.csv
If no path is provided, the sample data is used.
"""

import csv
import sys
from typing import List

def load_prices(path: str) -> List[float]:
    """Return list of closing prices from a CSV file."""
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        prices = [float(row["close"]) for row in reader]
    return prices

def rsi(prices: List[float], period: int = 14) -> float:
    """Compute the RSI for a list of prices.

    Returns the last RSI value calculated over the given period.
    """
    if len(prices) <= period:
        raise ValueError("Not enough price points to calculate RSI")

    gains = []
    losses = []
    for i in range(1, period + 1):
        change = prices[i] - prices[i - 1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(-change)
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    for i in range(period + 1, len(prices)):
        change = prices[i] - prices[i - 1]
        gain = change if change > 0 else 0
        loss = -change if change < 0 else 0
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

    if avg_loss == 0:
        rs = float("inf")
    else:
        rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/btc_prices_sample.csv"
    prices = load_prices(path)
    latest_rsi = rsi(prices)
    if latest_rsi > 70:
        signal = "SELL"
    elif latest_rsi < 30:
        signal = "BUY"
    else:
        signal = "HOLD"
    print(f"Latest RSI: {latest_rsi:.2f}")
    print(f"Signal: {signal}")

if __name__ == "__main__":
    main()
