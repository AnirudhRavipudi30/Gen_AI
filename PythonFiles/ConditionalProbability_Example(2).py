# 🔹 Conditional Probability Explanation:
# - P(A | B) = Probability of A occurring given B has happened.
# - Example: P(Approved | High Credit) = Applicants with high credit AND approved / Applicants with high credit.

# Given data
total_applicants = 1000
high_credit_score = 600
loan_approved = 400
both_high_credit_and_approved = 350

# Compute conditional probabilities
P_approved_given_credit = both_high_credit_and_approved / high_credit_score  # P(A | B)
P_credit_given_approved = both_high_credit_and_approved / loan_approved  # P(B | A)

# Display results
print("\n🔹 Conditional Probability: Loan Approval & Credit Score 🔹\n")

print(f"Total loan applicants: {total_applicants}")
print(f"Applicants with high credit score: {high_credit_score}")
print(f"Applicants approved for loan: {loan_approved}")
print(f"Applicants with high credit AND approved: {both_high_credit_and_approved}\n")

print(f"Probability of Approval given High Credit Score P(A | B): {P_approved_given_credit:.2f}")
print(f"Probability of High Credit Score given Approval P(B | A): {P_credit_given_approved:.2f}")
