import random
# States, Cities, and Citizens
states = {
    "California": {
        "Los Angeles": ["P1", "P2", "P3", "P4", "P5"],
        "San Diego": ["P6", "P7", "P8", "P9", "P10"],
        "San Francisco": ["P11", "P12", "P13", "P14", "P15"]
    },
    "Texas": {
        "Houston": ["P16", "P17", "P18", "P19", "P20"],
        "Austin": ["P21", "P22", "P23", "P24", "P25"],
        "Dallas": ["P26", "P27", "P28", "P29", "P30"]
    },
    "Florida": {
        "Miami": ["P31", "P32", "P33", "P34", "P35"],
        "Orlando": ["P36", "P37", "P38", "P39", "P40"],
        "Tampa": ["P41", "P42", "P43", "P44", "P45"]
    }
}

# Step 1: Select 2 random states
selected_states = random.sample(list(states.keys()), 2)

# Step 2: Select 3 random cities from each selected state
selected_cities = {}
for state in selected_states:
    selected_cities[state] = random.sample(list(states[state].keys()), 3)

# Step 3: Select 5 random people from each selected city
selected_people = []
for state, cities in selected_cities.items():
    for city in cities:
        selected_people.extend(random.sample(states[state][city], 5))

# Display results
print("📌 Selected States:", selected_states)
print("📌 Selected Cities per State:", selected_cities)
print("📌 Selected People (Multi-Stage Sampling):", selected_people)
