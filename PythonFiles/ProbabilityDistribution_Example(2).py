# 🔹 Probability Distribution Explanation:
# - Probability Distribution assigns probabilities to different outcomes (score ranges).
# - We compute: P(X = x) = (Frequency of X) / (Total Observations).
# - Cumulative Distribution shows the probability of scoring "at most" a certain value.

# Given data
score_ranges = ["0-20", "21-40", "41-60", "61-80", "81-100"]
frequency = [5, 15, 25, 35, 20]  # Number of students in each range

# Compute total students
total_students = sum(frequency)

# Compute Probability Distribution
probability_distribution = [count / total_students for count in frequency]

# Compute Cumulative Distribution (CDF)
cumulative_distribution = []
cumulative_sum = 0

for prob in probability_distribution:
    cumulative_sum += prob
    cumulative_distribution.append(cumulative_sum)

# Display Probability Distribution
print("\n🔹 Probability Distribution: Student Exam Scores 🔹\n")
for score, prob in zip(score_ranges, probability_distribution):
    print(f"P(X = {score}) = {prob:.2f}")

# Display Cumulative Distribution
print("\n🔹 Cumulative Distribution: Probability of Scoring At Most X 🔹\n")
for score, cdf in zip(score_ranges, cumulative_distribution):
    print(f"P(X ≤ {score}) = {cdf:.2f}")
