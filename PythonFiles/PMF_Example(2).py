# 🔹 Probability Mass Function (PMF) Explanation:
# - PMF gives the probability of a specific number of cars arriving per minute.
# - We compute P(X = x) as (Frequency of X) / (Total Minutes Observed).

# Given data
cars_per_minute = [0, 1, 2, 3, 4, 5, 6]  # Number of cars arriving
frequency = [3, 7, 15, 25, 30, 12, 8]  # Observed minutes for each case

# Compute total minutes observed
total_minutes = sum(frequency)

# Compute PMF
pmf_values = [count / total_minutes for count in frequency]

# Display PMF
print("\n🔹 Probability Mass Function (PMF): Cars Arriving at a Toll Booth 🔹\n")
for x, pmf in zip(cars_per_minute, pmf_values):
    print(f"P(X = {x}) = {pmf:.4f}")
