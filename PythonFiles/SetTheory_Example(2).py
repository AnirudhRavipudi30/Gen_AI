# 🔹 Set Theory Explanation:
# - Union (A ∪ B): Students in at least one of the courses.
# - Intersection (A ∩ B): Students in both Science and Arts.
# - Difference (A - B or B - A): Students in only one course.
# - Complement: Students in neither course.

# Given data
total_students = 250
science_students = 150
arts_students = 100
both_courses = 40  # Students enrolled in both Science & Arts

# Compute set operations
only_science = science_students - both_courses  # Science but NOT Arts
only_arts = arts_students - both_courses  # Arts but NOT Science
union = science_students + arts_students - both_courses  # At least one course
neither = total_students - union  # Students in neither Science nor Arts

# Display results
print("🔹 Set Theory: University Course Enrollment 🔹\n")

print(f"Total students: {total_students}")
print(f"Students in Science: {science_students}")
print(f"Students in Arts: {arts_students}")
print(f"Students in both Science & Arts (Intersection): {both_courses}\n")

print(f"Union (At least one course) |S ∪ A|: {union}")
print(f"Only Science (S - A): {only_science}")
print(f"Only Arts (A - S): {only_arts}")
print(f"Complement (Neither Science nor Arts) |S^c ∩ A^c|: {neither}")
