import random

# Given probability
p_approved = 0.88  # Probability of transaction approval
p_denied = 1 - p_approved  # Probability of transaction denial

# Bernoulli trial function
def bernoulli_trial(p):
    """Returns 1 (approved) with probability p and 0 (denied) with probability (1 - p)."""
    return 1 if random.random() < p else 0

# Simulate 1,000 foreign transactions
trials = 1000
results = [bernoulli_trial(p_approved) for _ in range(trials)]

# Compute empirical probability
approved_count = sum(results)
denied_count = trials - approved_count
empirical_p_approved = approved_count / trials
empirical_p_denied = denied_count / trials

# Display results
print(f"Simulated Credit Card Transactions Over {trials} Trials: {results[:50]} ...")  # First 50 transactions for readability
print(f"Observed Probability of Approval: {empirical_p_approved:.4f}")
print(f"Observed Probability of Denial: {empirical_p_denied:.4f}")
print(f"Expected Probability of Denial: {p_denied:.4f}")
