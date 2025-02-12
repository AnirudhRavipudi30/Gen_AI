# Function to calculate Z-score
def compute_z(x, mu, sigma):
    return (x - mu) / sigma

# Function to approximate the CDF of a standard normal distribution
def normal_cdf(z):
    """Approximate the CDF of a standard normal distribution using a polynomial."""
    # Abramowitz & Stegun approximation formula
    if z < 0:
        return 1 - normal_cdf(-z)
    
    b1, b2, b3, b4, b5 = 0.319381530, -0.356563782, 1.781477937, -1.821255978, 1.330274429
    p = 0.2316419
    t = 1 / (1 + p * z)
    
    poly = (b1 * t) + (b2 * t**2) + (b3 * t**3) + (b4 * t**4) + (b5 * t**5)
    cdf = 1 - (1 / (2.506628274631 * (2.718281828459**(-z**2 / 2)))) * poly
    
    return cdf

# Given values
mu = 500  # Mean
sigma = 50  # Standard deviation

# Compute Z-scores
z_450 = compute_z(450, mu, sigma)
z_550 = compute_z(550, mu, sigma)
z_600 = compute_z(600, mu, sigma)

# Compute probabilities using normal CDF approximation
p_450 = normal_cdf(z_450)
p_550 = normal_cdf(z_550)
p_600 = normal_cdf(z_600)

# Probability of 450 ≤ X ≤ 550
p_450_550 = p_550 - p_450

# Probability of X > 600
p_above_600 = 1 - p_600

# Display results
print(f"P(450 ≤ X ≤ 550) = {p_450_550:.4f}")
print(f"P(X > 600) = {p_above_600:.4f}")
