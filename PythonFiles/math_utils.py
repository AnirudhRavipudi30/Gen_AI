# math_utils.py - User-Defined Custom Module

def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) using recursion."""
    if b == 0:
        return a
    return gcd(b, a % b)