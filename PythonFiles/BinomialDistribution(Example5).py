# Function to compute factorial
def factorial(num):
    """Computes factorial of a number."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Function to compute binomial probability
def binomial_probability(n, k, p):
    """Computes binomial probability P(X = k)."""
    def n_choose_k(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))
    
    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Given values
n = 12  # Total vehicles
p = 0.82  # Probability of a vehicle crashing
k_values = [0, 1, 2, 3]  # We need P(X ≤ 3)

# Compute cumulative probability P(X ≤ 3)
cumulative_probability = sum(binomial_probability(n, k, p) for k in k_values)

# Compute P(X > 3)
probability_greater_than_3 = 1 - cumulative_probability

# Print results
print(f"P(At most 3 vehicles crash) = {cumulative_probability:.4f}")
print(f"P(More than 3 vehicles crash) = {probability_greater_than_3:.4f}")
