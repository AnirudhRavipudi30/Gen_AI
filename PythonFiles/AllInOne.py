# Aviation Industry: Probability & Statistical Concepts Explained with Python

## 1. Probability Mass Function (PMF)


### **Example: PMF for Flight Delays**

def pmf_flight_delays():
    flight_delays = {0: 0.10, 1: 0.20, 2: 0.30, 3: 0.25, 4: 0.10, 5: 0.05}
    for delays, probability in flight_delays.items():
        print(f"P(X = {delays}) = {probability:.2f}")

pmf_flight_delays()

## 2. Cumulative Mass Function (CMF)


### **Example: CMF for Flight Delays**

def cmf_flight_delays():
    flight_delays = {0: 0.10, 1: 0.20, 2: 0.30, 3: 0.25, 4: 0.10, 5: 0.05}
    cumulative_probability = 0
    for delays, probability in flight_delays.items():
        cumulative_probability += probability
        print(f"P(X ≤ {delays}) = {cumulative_probability:.2f}")

cmf_flight_delays()

## 3. Probability Density Function (PDF)


### **Example: PDF for Flight Delays**

import math

def normal_distribution(x, mean, std_dev):
    exponent = math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
    return (1 / (math.sqrt(2 * math.pi) * std_dev)) * exponent

# Example: Flight delay follows N(20, 5^2)
x_value = 25
mean = 20
std_dev = 5
probability = normal_distribution(x_value, mean, std_dev)
print(f"P(X = {x_value}) ≈ {probability:.4f}")



## 4. Bernoulli Distribution


### **Example: Flight Delayed or On-Time**

def bernoulli_flight_delay(p):
    delayed = p
    on_time = 1 - p
    print(f"P(Delayed) = {delayed:.2f}, P(On Time) = {on_time:.2f}")

bernoulli_flight_delay(0.30)


## 5. Binomial Distribution


### **Example: Predicting Number of Delayed Flights per Day**

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def binomial_probability(n, k, p):
    comb = factorial(n) / (factorial(k) * factorial(n - k))
    return comb * (p ** k) * ((1 - p) ** (n - k))

n_flights = 10
k_delays = 4
p_delay = 0.30
prob = binomial_probability(n_flights, k_delays, p_delay)
print(f"P({k_delays} delays in {n_flights} flights) = {prob:.4f}")


## 6. Normal Distribution

### **Example: Flight Delay Time Distribution**

def normal_cdf(x, mean, std_dev):
    return (1 + math.erf((x - mean) / (std_dev * math.sqrt(2)))) / 2

prob_less_than_25 = normal_cdf(25, 20, 5)
print(f"P(Delay ≤ 25 min) = {prob_less_than_25:.4f}")


## 7. Correlation Analysis


### **Example: Correlation Between Delays and Missed Connections**

def pearson_correlation(x, y):
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    numerator = sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y))
    denominator_x = math.sqrt(sum((a - mean_x) ** 2 for a in x))
    denominator_y = math.sqrt(sum((b - mean_y) ** 2 for b in y))
    return numerator / (denominator_x * denominator_y)

delays = [10, 15, 12, 25, 30, 35, 40, 20, 22, 28]
missed_connections = [5, 8, 6, 18, 25, 30, 35, 12, 15, 20]
correlation = pearson_correlation(delays, missed_connections)
print(f"Correlation between delays and missed connections: r = {correlation:.2f}")



