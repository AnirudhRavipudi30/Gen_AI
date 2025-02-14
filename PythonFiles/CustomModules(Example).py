# main.py - Importing and Using the Custom Math Module

import math_utils  # Import the user-defined module

# Using the factorial function
num = 5
print(f"Factorial of {num}: {math_utils.factorial(num)}")  # Output: 120

# Using the is_prime function
test_num = 29
print(f"Is {test_num} a prime number? {math_utils.is_prime(test_num)}")  # Output: True

# Using the GCD function
a, b = 48, 18
print(f"GCD of {a} and {b}: {math_utils.gcd(a, b)}")  # Output: 6