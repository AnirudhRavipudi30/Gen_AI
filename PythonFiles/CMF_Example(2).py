# 🔹 Cumulative Mass Function (CMF) Explanation:
# - CMF represents the probability of a package being delivered "within X days or less."
# - We compute it as the cumulative sum of the PMF.

# Given data
delivery_days = [1, 2, 3, 4, 5]  # Delivery times in days
package_counts = [10, 20, 30, 25, 15]  # Number of packages delivered in each time frame

# Compute total deliveries
total_packages = sum(package_counts)

# Compute PMF
pmf_values = [count / total_packages for count in package_counts]

# Compute CMF
cmf_values = []
cumulative_sum = 0

for pmf in pmf_values:
    cumulative_sum += pmf
    cmf_values.append(cumulative_sum)

# Display CMF
print("\n🔹 Cumulative Mass Function (CMF): Probability of Delivering Within X Days 🔹\n")
for x, cmf in zip(delivery_days, cmf_values):
    print(f"P(X ≤ {x} days) = {cmf:.4f}")
