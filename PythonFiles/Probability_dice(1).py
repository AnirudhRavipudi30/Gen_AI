# PMF for Rolling a Die (Discrete Probability)
def pmf_die_roll():
    die_faces = range(1, 7)  # Possible outcomes (1 to 6)
    pmf_values = [1/6] * 6  # Each outcome has 1/6 probability
    for face, prob in zip(die_faces, pmf_values):
        print(f"P(X={face}) = {prob:.2f}")

# CDF for Rolling a Die (Cumulative Probability)
def cdf_die_roll():
    die_faces = range(1, 7)  # Possible outcomes (1 to 6)
    pmf_values = [1/6] * 6  # Each outcome has 1/6 probability
    cdf_values = []
    cumulative_sum = 0
    for prob in pmf_values:
        cumulative_sum += prob
        cdf_values.append(cumulative_sum)
    for face, cum_prob in zip(die_faces, cdf_values):
        print(f"P(X<={face}) = {cum_prob:.2f}")

# Probability of rolling a specific category (even, odd, prime, composite) or a specific number
def dice_probability(category, sides=6):
    numbers = list(range(1, sides + 1))
    
    if category == "even":
        favorable = [n for n in numbers if n % 2 == 0]
    elif category == "odd":
        favorable = [n for n in numbers if n % 2 != 0]
    elif category == "prime":
        favorable = [n for n in numbers if is_prime(n)]
    elif category == "composite":
        favorable = [n for n in numbers if is_composite(n)]
    elif category.isdigit():
        favorable = [int(category)] if int(category) in numbers else []
    else:
        return "Invalid category. Choose from: even, odd, prime, composite, or a specific number."
    
    probability = len(favorable) / sides
    return probability

# Helper functions for prime and composite checks
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_composite(n):
    return n > 1 and not is_prime(n)

# Display results
print("PMF for Rolling a Die:")
pmf_die_roll()
print("\nCDF for Rolling a Die:")
cdf_die_roll()

# Get user input for dice probability
category = input("Enter the category (even, odd, prime, composite, or a number): ").strip().lower()
sides = int(input("Enter the number of sides on the die: ").strip())

probability = dice_probability(category, sides)
print(f"The probability of rolling a {category} number on a {sides}-sided die is: {probability:.2%}")
 