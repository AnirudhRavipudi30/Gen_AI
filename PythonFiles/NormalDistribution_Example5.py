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

# ------------------------------------
# Example: Bolt Diameter Measurements (in mm)
# ------------------------------------
bolt_diameters = [10.1, 10.2, 10.3, 10.4, 10.5, 10.5, 10.5, 10.4, 10.3, 10.2]

# Compute statistics
mean, median, mode = compute_statistics(bolt_diameters)

# Print results
print("\n🔩 Bolt Diameter Analysis:")
print(f"Mean Diameter: {mean:.2f} mm")
print(f"Median Diameter: {median} mm")
print(f"Mode Diameter: {mode} mm")

# Check normal distribution
if mean == median == mode:
    print("✅ The bolt diameters follow a perfect normal distribution!")
else:
    print("❌ The bolt diameters are NOT perfectly normally distributed!")
