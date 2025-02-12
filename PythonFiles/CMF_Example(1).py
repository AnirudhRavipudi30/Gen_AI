# Define customer counts and number of hours observed
customer_counts = [0, 5, 10, 15, 20, 25, 30]
hours_observed = [5, 10, 20, 30, 20, 10, 5]

# Compute Total Hours Observed
total_hours = sum(hours_observed)

# Compute PMF (Probability Mass Function)
pmf_values = [count / total_hours for count in hours_observed]

# Compute CMF (Cumulative Mass Function)
cmf_values = []
cumulative_sum = 0

for pmf in pmf_values:
    cumulative_sum += pmf
    cmf_values.append(cumulative_sum)

# Display PMF
print("Probability Mass Function (PMF):")
for x, pmf in zip(customer_counts, pmf_values):
    print(f"P(X = {x}) = {pmf:.2f}")

# Display CMF
print("\nCumulative Mass Function (CMF):")
for x, cmf in zip(customer_counts, cmf_values):
    print(f"P(X ≤ {x}) = {cmf:.2f}")
