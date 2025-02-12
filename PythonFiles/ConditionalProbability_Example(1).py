# Given data
total_employees = 500
training_completed = 300
promoted = 200
both_training_and_promotion = 180

# Compute conditional probabilities
P_p_given_t = both_training_and_promotion / training_completed  # P(P | T)
P_t_given_p = both_training_and_promotion / promoted  # P(T | P)

# Display results
print("🔹 Conditional Probability Calculations 🔹\n")

print(f"Total employees surveyed: {total_employees}")
print(f"Employees who completed training: {training_completed}")
print(f"Employees who got promoted: {promoted}")
print(f"Employees who completed training AND got promoted: {both_training_and_promotion}\n")

print(f"Probability of Promotion given Training Completion P(P | T): {P_p_given_t:.2f}")
print(f"Probability of Training Completion given Promotion P(T | P): {P_t_given_p:.2f}")
