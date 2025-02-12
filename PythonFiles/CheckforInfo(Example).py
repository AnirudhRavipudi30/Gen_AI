import math
import statistics

# Given data: Flight delays in minutes
delays = [15, 30, 45, 30, 50, 60, 30, 20]

# Step 1: Compute Mean (Average Delay)
mean_delay = statistics.mean(delays)

# Step 2: Compute Mode (Most Frequent Delay)
mode_delay = statistics.mode(delays)

# Step 3: Compute Variance (Spread of Delays)
variance_delay = statistics.variance(delays)

# Step 4: Compute Range (Max - Min Delay)
range_delay = max(delays) - min(delays)

# Step 5: Compute Standard Deviation (How Much Delays Deviate from Mean)
std_dev_delay = statistics.stdev(delays)

# Print the results
print(f"Mean Delay: {mean_delay:.2f} minutes")
print(f"Mode Delay: {mode_delay} minutes")
print(f"Variance in Delays: {variance_delay:.2f} min²")
print(f"Range of Delays: {range_delay} minutes")
print(f"Standard Deviation of Delays: {std_dev_delay:.2f} minutes")