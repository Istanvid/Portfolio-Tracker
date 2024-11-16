# portfolio_tracker.py

portfolio = {"AAPL": 5, "TSLA": 2, "AMZN": 1}
prices = {"AAPL": 150, "TSLA": 700, "AMZN": 3000}

def calculate_portfolio_value():
    return sum(portfolio[stock] * prices[stock] for stock in portfolio)

# Sample usage
print("Portfolio value:", calculate_portfolio_value())
