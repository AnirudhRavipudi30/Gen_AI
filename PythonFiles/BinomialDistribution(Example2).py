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
        return factorial(n) // (factorial(k) * factorial(n - k))  # Binomial coefficient
    
    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Example: Soccer Penalty Shots
n = 5  # Total penalty shots
p = 0.75  # Probability of scoring
k = 4  # We want exactly 4 goals

# Compute probability
probability = binomial_probability(n, k, p)

# Print result
print(f"P(Exactly {k} goals) = {probability:.4f}")
