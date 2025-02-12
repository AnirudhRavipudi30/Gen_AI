import random
# Cities and their households
cities = {
    "New York": ["H1", "H2", "H3", "H4", "H5"],
    "Los Angeles": ["H6", "H7", "H8", "H9", "H10"],
    "Chicago": ["H11", "H12", "H13", "H14", "H15"],
    "Houston": ["H16", "H17", "H18", "H19", "H20"],
    "Miami": ["H21", "H22", "H23", "H24", "H25"]
}

# Select 3 random cities
selected_cities = random.sample(list(cities.keys()), 3)

# Get all households from selected cities
selected_households = []
for city in selected_cities:
    selected_households.extend(cities[city])

# Display results
print("📌 Selected Cities:", selected_cities)
print("📌 Surveyed Households (Cluster Sampling):", selected_households)
