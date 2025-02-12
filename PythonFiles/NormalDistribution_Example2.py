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

# Blood pressure readings of 10 patients
bp_readings = [118, 120, 122, 125, 130, 135, 140, 125, 130, 128]

mean, median, mode = compute_statistics(bp_readings)

print(f"Mean Blood Pressure: {mean:.2f}")
print(f"Median Blood Pressure: {median}")
print(f"Mode Blood Pressure: {mode}")

# Check if the dataset follows normal distribution
if mean == median == mode:
    print("✅ The dataset is perfectly normally distributed!")
else:
    print("❌ The dataset is NOT perfectly normally distributed!")
