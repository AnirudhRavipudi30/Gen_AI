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
n = 6  # Total flights
p = 0.85  # Probability of on-time arrival
k_values = [0, 1, 2, 3, 4]  # We want P(X ≤ 4)

# Compute cumulative probability P(X ≤ 4)
cumulative_probability = sum(binomial_probability(n, k, p) for k in k_values)

# Print result
print(f"P(At most 4 flights on time) = {cumulative_probability:.4f}")
