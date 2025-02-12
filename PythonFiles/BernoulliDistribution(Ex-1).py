import random

# Given probability
p_buying = 0.71  # Probability of buying coffee
p_not_buying = 1 - p_buying  # Probability of NOT buying coffee

# Bernoulli trial function
def bernoulli_trial(p):
    """Returns 1 (buys coffee) with probability p and 0 (does not buy) with probability (1 - p)."""
    return 1 if random.random() < p else 0

# Simulate 10 days of coffee purchasing behavior
trials = 10
results = [bernoulli_trial(p_buying) for _ in range(trials)]

# Compute empirical probability
success_count = sum(results)
empirical_p = success_count / trials

# Display results
print(f"Simulated Coffee Buying Behavior Over {trials} Days: {results}")
print(f"Observed Probability of Buying Coffee: {empirical_p:.2f}")
print(f"Probability of NOT Buying Coffee: {p_not_buying:.2f}")
