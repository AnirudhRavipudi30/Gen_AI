import random

# List of 300 passengers (represented as "P1", "P2", ..., "P300")
passengers = [f"P{i}" for i in range(1, 301)]

# Selecting 50 random passengers
sample_size = 50
random_sample = random.sample(passengers, sample_size)

# Display results
print("📌 Selected Passengers for Survey (Simple Random Sampling):")
print(random_sample)
