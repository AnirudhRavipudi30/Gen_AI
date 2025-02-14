import time
import random

# Decorator to log execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Stock price prediction function with a decorator
@timing_decorator
def predict_stock_price(stock_symbol):
    print(f"Predicting price for {stock_symbol}...")
    time.sleep(2)  # Simulate computation time
    predicted_price = round(random.uniform(100, 500), 2)  # Mock prediction
    print(f"Predicted price for {stock_symbol}: ${predicted_price}")
    return predicted_price

# Test the function
predict_stock_price("TSLA")