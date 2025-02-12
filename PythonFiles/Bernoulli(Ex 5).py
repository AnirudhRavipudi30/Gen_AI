import random

# Given probability
p_made = 0.59  # Probability of making the shot
p_missed = 1 - p_made  # Probability of missing the shot

# Bernoulli trial function
def bernoulli_trial(p):
    """Returns 1 (shot made) with probability p, else 0 (shot missed)."""
    return 1 if random.random() < p else 0

# Simulate 1,000 shot attempts
trials = 1000
results = [bernoulli_trial(p_made) for _ in range(trials)]

# Compute empirical probability
made_count = sum(results)
missed_count = trials - made_count
empirical_p_made = made_count / trials
empirical_p_missed = missed_count / trials

# Display results
print(f"Simulated Basketball Shots Over {trials} Attempts: {results[:50]} ...")  # Showing first 50 for readability
print(f"Observed Probability of Making the Shot: {empirical_p_made:.4f}")
print(f"Observed Probability of Missing the Shot: {empirical_p_missed:.4f}")
print(f"Expected Probability of Missing the Shot: {p_missed:.4f}")
