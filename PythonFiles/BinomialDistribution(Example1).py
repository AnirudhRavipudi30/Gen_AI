# Function to compute factorial
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Function to compute binomial probability
def binomial_probability(n, k, p):
    """Computes binomial probability P(X = k)"""
    def n_choose_k(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Given values
n = 8  
p = 0.9  
k = 6  

# Compute probability
probability = binomial_probability(n, k, p)
print(f"P(Exactly {k} patients test positive) = {probability:.4f}")
