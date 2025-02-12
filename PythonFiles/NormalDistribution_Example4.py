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

test_scores = [900, 950, 1020, 1050, 1100, 1150, 1050, 1080, 1070, 1040]

# Compute statistics
mean, median, mode = compute_statistics(test_scores)

# Print results
print("\n📚 Test Scores Analysis:")
print(f"Mean Test Score: {mean:.2f}")
print(f"Median Test Score: {median}")
print(f"Mode Test Score: {mode}")

# Check normal distribution
if mean == median == mode:
    print("✅ Test scores follow a normal distribution!")
else:
    print("❌ Test scores are NOT normally distributed!")
