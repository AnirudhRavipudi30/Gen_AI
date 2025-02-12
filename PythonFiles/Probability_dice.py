def dice_probability(sides=6, outcome=1):
    if 1 <= outcome <= sides:
        return 1 / sides
    else:
        return 0 


sides = 6 
outcome = 3  got
probability = dice_probability(sides, outcome)
print(f"The probability of rolling a {outcome} on a {sides}-sided die is: {probability:.2%}")
