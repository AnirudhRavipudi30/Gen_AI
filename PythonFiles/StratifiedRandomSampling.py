import random
# Male and Female patient groups
male_patients = [f"M{i}" for i in range(1, 201)]  # 200 male patients
female_patients = [f"F{i}" for i in range(1, 201)]  # 200 female patients

# Select 50 random males and 50 random females
selected_males = random.sample(male_patients, 50)
selected_females = random.sample(female_patients, 50)

# Display results
print("📌 Selected Male Patients:", selected_males)
print("📌 Selected Female Patients:", selected_females)
