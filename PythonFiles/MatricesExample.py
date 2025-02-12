# PageRank Algorithm for Ranking Social Media Influencers

import numpy as np

# Step 1: Define the link matrix (who mentions whom)
L = np.array([
    [0, 0.5, 0.5, 0],
    [0.5, 0, 0, 1],
    [0.5, 0.5, 0, 0],
    [0, 0, 0.5, 0]
])

# Step 2: Initialize rank vector (equal importance at start)
R = np.array([1, 1, 1, 1])

# Step 3: Define a stopping threshold (epsilon)
epsilon = 0.0001
difference = 1  # Start with a large value
iterations = 0  # Count iterations

# Step 4: Iterative PageRank Calculation
while difference > epsilon:
    new_R = np.dot(L, R)  # Multiply link matrix by rank vector
    difference = np.linalg.norm(new_R - R, 1)  # Compute change in rank
    R = new_R  # Update rank
    iterations += 1

# Step 5: Print Results
print(f"PageRank stabilized after {iterations} iterations.\n")
print("Final Influencer Ranks:")
for i, rank in enumerate(R):
    print(f"Influencer {chr(65 + i)}: {rank:.4f}")  # Convert 0 -> A, 1 -> B, etc.