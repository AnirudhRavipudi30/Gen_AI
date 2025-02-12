import math

# Given data for flights (Distance in km and Fuel Consumption in liters)
flights = [
    (200, 1500),
    (450, 3400),
    (600, 4600),
    (850, 6700),
    (1200, 9200),
    (1500, 11500),
    (1800, 13800),
    (2000, 15400)
]

# Step 1: Compute the means of Distance (X̄) and Fuel Consumption (Ȳ)
n = len(flights)
sum_X = sum(f[0] for f in flights)
sum_Y = sum(f[1] for f in flights)
mean_X = sum_X / n
mean_Y = sum_Y / n

# Step 2: Compute the summations required for Pearson correlation
sum_XY = sum((f[0] - mean_X) * (f[1] - mean_Y) for f in flights)
sum_X2 = sum((f[0] - mean_X) ** 2 for f in flights)
sum_Y2 = sum((f[1] - mean_Y) ** 2 for f in flights)

# Step 3: Compute Pearson correlation coefficient (r)
r = sum_XY / (math.sqrt(sum_X2) * math.sqrt(sum_Y2))

# Print the results
print(f"Mean Distance (X̄): {mean_X:.2f} km")
print(f"Mean Fuel Consumption (Ȳ): {mean_Y:.2f} liters")
print(f"Pearson Correlation Coefficient (r): {r:.3f}")
