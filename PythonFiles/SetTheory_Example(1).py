# Given data
total_customers = 200  # Total number of customers surveyed
phones = 120  # Customers who bought phones
laptops = 80  # Customers who bought laptops
both = 40  # Customers who bought both phones and laptops

# Compute set operations
only_phones = phones - both  # Customers who bought only phones
only_laptops = laptops - both  # Customers who bought only laptops
union = phones + laptops - both  # Customers who bought at least one product
neither = total_customers - union  # Customers who bought neither

# Display results
print("🔹 Set Theory Calculations for Customers Buying Phones & Laptops 🔹\n")

# Individual Sets
print(f"Total customers surveyed: {total_customers}")
print(f"Customers who bought Phones: {phones}")
print(f"Customers who bought Laptops: {laptops}")
print(f"Customers who bought both Phones & Laptops (Intersection): {both}\n")

# Union (Customers who bought at least one product)
print(f"Union (Customers who bought at least one product) |P ∪ L|: {union}")

# Difference (Only Phones and Only Laptops)
print(f"Only Phones (P - L): {only_phones}")
print(f"Only Laptops (L - P): {only_laptops}")

# Complement (Customers who bought neither Phones nor Laptops)
print(f"Complement (Neither Phones nor Laptops) |P^c ∩ L^c|: {neither}")
