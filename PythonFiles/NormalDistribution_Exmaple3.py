# Function to compute mean, median, and mode manually
def compute_statistics(data):
    """Computes mean, median, and mode manually for a dataset."""
    n = len(data)
    
    # Mean
    mean = sum(data) / n
    
    # Median
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    
    # Mode (most frequent value)
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    mode = max(frequency, key=frequency.get)

    return mean, median, mode

# Stock returns data (% daily change)
stock_returns = [-0.5, 0.2, 0.8, 1.0, 1.5, -0.3, 0.7, 0.9, 1.1, 0.4]

# Compute statistics
mean, median, mode = compute_statistics(stock_returns)

# Print results
print(f"Mean Daily Return: {mean:.2f}%")
print(f"Median Daily Return: {median}%")
print(f"Mode Daily Return: {mode}%")

# Check if distribution is normal
if mean == median == mode:
    print("✅ Stock returns follow a normal distribution!")
else:
    print("❌ Stock returns are NOT normally distributed!")
