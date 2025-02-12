# PMF for Rolling a Die (Discrete Probability)
def pmf_die_roll():
    die_faces = range(1, 7)  # Possible outcomes (1 to 6)
    pmf_values = [1/6] * 6  # Each outcome has 1/6 probability
    for face, prob in zip(die_faces, pmf_values):
        print(f"P(X={face}) = {prob:.2f}")

# PMF for a Biased Coin Toss
def pmf_biased_coin():
    outcomes = ['Heads', 'Tails']
    probabilities = [0.7, 0.3]  # Assuming a biased coin
    for outcome, prob in zip(outcomes, probabilities):
        print(f"P(X={outcome}) = {prob:.2f}")

# PMF for a Fair Coin Toss
def pmf_fair_coin():
    outcomes = ['Heads', 'Tails']
    probabilities = [0.5, 0.5]  # Fair coin probability
    for outcome, prob in zip(outcomes, probabilities):
        print(f"P(X={outcome}) = {prob:.2f}")

# Display results
print("PMF for Rolling a Die:")
pmf_die_roll()
print("\nPMF for a Fair Coin Toss:")
pmf_fair_coin()
print("\nPMF for a Biased Coin Toss:")
pmf_biased_coin()


