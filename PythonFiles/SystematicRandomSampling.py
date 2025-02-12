# List of 1,000 smartphones
smartphones = [f"Phone{i}" for i in range(1, 1001)]

# Selecting every 10th smartphone
step = 10
systematic_sample = smartphones[::step]

# Display results
print("📌 Selected Smartphones for Quality Check (Systematic Sampling):")
print(systematic_sample)
