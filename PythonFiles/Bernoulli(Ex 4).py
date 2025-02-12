import random

# Given probability
p_external_factors = 0.91  # Probability that stock price is influenced by external factors
p_not_influenced = 1 - p_external_factors  # Probability that stock price is NOT influenced

# Bernoulli trial function
def bernoulli_trial(p):
    """Returns 1 (influenced by external factors) with probability p, else 0 (not influenced)."""
    return 1 if random.random() < p else 0

# Simulate 1,000 stock price movements
trials = 1000
results = [bernoulli_trial(p_external_factors) for _ in range(trials)]

# Compute empirical probability
influenced_count = sum(results)
not_influenced_count = trials - influenced_count
empirical_p_influenced = influenced_count / trials
empirical_p_not_influenced = not_influenced_count / trials

# Display results
print(f"Simulated Stock Price Movements Over {trials} Days: {results[:50]} ...")  # Showing first 50 for readability
print(f"Observed Probability of External Influence: {empirical_p_influenced:.4f}")
print(f"Observed Probability of NO External Influence: {empirical_p_not_influenced:.4f}")
print(f"Expected Probability of NO External Influence: {p_not_influenced:.4f}")
