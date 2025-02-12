# Define delay categories and probabilities
delay_categories = ["On-time", "Slight Delay", "Moderate Delay", "Canceled due to a delay"]
pmf_values = [0.51, 0.22, 0.17, 0.10]

# Print PMF values
print("Probability Mass Function (PMF) for Flight Delays:")
for x, p in zip(delay_categories, pmf_values):
    print(f"P(X = {x}) = {p:.2f}")

# Compute expected delay
expected_delay = sum(x * p for x, p in enumerate(pmf_values))
print(f"\nExpected Delay Category: {expected_delay:.2f}")
