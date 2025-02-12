import random

# Given probability
p_false_negative = 0.65  # Probability of false negative
p_false_positive = 1 - p_false_negative  # Probability of false positive

# Bernoulli trial function
def bernoulli_trial(p):
    """Returns 1 (false negative) with probability p and 0 (false positive) with probability (1 - p)."""
    return 1 if random.random() < p else 0

# Simulate 1,000 medical test results
trials = 1000
results = [bernoulli_trial(p_false_negative) for _ in range(trials)]

# Compute empirical probability
false_negative_count = sum(results)
false_positive_count = trials - false_negative_count
empirical_p_false_negative = false_negative_count / trials
empirical_p_false_positive = false_positive_count / trials

# Display results
print(f"Simulated Medical Test Results Over {trials} Trials: {results[:50]} ...")  # First 50 for readability
print(f"Observed Probability of False Negative: {empirical_p_false_negative:.4f}")
print(f"Observed Probability of False Positive: {empirical_p_false_positive:.4f}")
print(f"Expected Probability of False Positive: {p_false_positive:.4f}")
