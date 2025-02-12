import random

def accident_probability(speed, weather, *args, traffic_density="medium", driver_behavior="normal", **kwargs):
    """
    Predicts the probability of a car accident based on multiple factors.

    Arguments:
    speed (int): Speed of the vehicle in km/h.
    weather (str): Current weather condition (e.g., 'clear', 'rain', 'snow', 'fog').
    *args: Additional past accident records (optional).
    traffic_density (str, optional): Level of traffic ('low', 'medium', 'high'). Default is 'medium'.
    driver_behavior (str, optional): Driving style ('normal', 'aggressive', 'drowsy'). Default is 'normal'.
    **kwargs: Additional risk factors (e.g., road_condition='wet', time_of_day='night').

    Returns:
    float: Probability of an accident (between 0 and 1).
    """

    # Base probability
    base_prob = 0.05  # Assume 5% base probability of an accident

    # Increase probability based on speed
    if speed > 100:
        base_prob += 0.15  # High speed increases risk
    elif speed > 80:
        base_prob += 0.10
    elif speed > 60:
        base_prob += 0.05

    # Weather conditions impact
    weather_risk = {"clear": 0, "rain": 0.10, "snow": 0.20, "fog": 0.15}
    base_prob += weather_risk.get(weather, 0)

    # Traffic density impact
    traffic_risk = {"low": 0, "medium": 0.05, "high": 0.10}
    base_prob += traffic_risk.get(traffic_density, 0)

    # Driver behavior impact
    behavior_risk = {"normal": 0, "aggressive": 0.15, "drowsy": 0.20}
    base_prob += behavior_risk.get(driver_behavior, 0)

    # Additional risk factors from **kwargs
    for key, value in kwargs.items():
        if key == "road_condition" and value == "wet":
            base_prob += 0.10  # Wet roads increase risk
        elif key == "time_of_day" and value == "night":
            base_prob += 0.07  # Night driving increases risk

    # Ensure probability is between 0 and 1
    accident_prob = min(base_prob, 1.0)

    return round(accident_prob, 2)

# Example Usage
prob1 = accident_probability(90, "rain", traffic_density="high", driver_behavior="aggressive", road_condition="wet")
prob2 = accident_probability(60, "clear", time_of_day="night")

print(f"Accident Probability 1: {prob1}")  # Expected higher probability due to aggressive driving in rain
print(f"Accident Probability 2: {prob2}")  # Expected lower probability due to good weather but night-time risk