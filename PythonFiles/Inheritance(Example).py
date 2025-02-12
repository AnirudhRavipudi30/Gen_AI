import random

class WeatherModel:
    """Base class for probability-based weather predictions."""

    def __init__(self, initial_prob=0.3):  # Default 30% probability of rain
        self.probability = initial_prob

    def update_probability(self, factor):
        """Adjusts probability using a simple Bayesian update."""
        likelihood = random.uniform(0.1, 0.9) * factor
        self.probability = (self.probability * likelihood) / ((self.probability * likelihood) + ((1 - self.probability) * (1 - likelihood)))
        print(f"Updated rain probability to {self.probability:.2f}")

    def get_probability(self):
        """Returns the current probability of rain."""
        return round(self.probability, 2)
class TemperatureModel(WeatherModel):
    """Weather model that includes temperature as a factor."""

    def update_with_temperature(self, temperature):
        """Adjust probability based on temperature (lower temp → higher rain chance)."""
        factor = 1 - (temperature / 100)  # Inverse relation (colder weather → higher rain probability)
        self.update_probability(factor)

# Example Usage
temp_model = TemperatureModel()
temp_model.update_with_temperature(20)  # Low temperature → higher rain probability
print(f"Rain Probability (After Temperature Update): {temp_model.get_probability()}")

class HumidityModel:
    """Model that modifies probability based on humidity levels."""
    
    def humidity_factor(self, humidity):
        return humidity / 100  # Higher humidity → Higher rain probability

class WindModel:
    """Model that modifies probability based on wind speed."""
    
    def wind_factor(self, wind_speed):
        return wind_speed / 50  # Stronger winds → Higher rain probability

class HumidityWindModel(WeatherModel, HumidityModel, WindModel):
    """Advanced model that considers both humidity and wind speed for rain prediction."""

    def update_with_conditions(self, humidity, wind_speed):
        """Combines humidity and wind speed effects on rain probability."""
        factor = (self.humidity_factor(humidity) + self.wind_factor(wind_speed)) / 2
        self.update_probability(factor)

# Example Usage
humid_wind_model = HumidityWindModel()
humid_wind_model.update_with_conditions(80, 30)  # High humidity & moderate wind
print(f"Rain Probability (After Humidity & Wind Update): {humid_wind_model.get_probability()}")

class AdvancedWeatherModel(TemperatureModel):
    """More refined weather model with confidence level consideration."""

    def update_with_confidence(self, temperature, confidence):
        """Adjust probability based on AI confidence in prediction."""
        factor = (1 - (temperature / 100)) * confidence
        self.update_probability(factor)
        print(f"Rain Probability (After Confidence Update): {self.probability:.2f}")

# Example Usage
adv_weather = AdvancedWeatherModel()
adv_weather.update_with_confidence(18, 0.9)  # AI is 90% confident in prediction
print(f"Final Rain Probability: {adv_weather.get_probability()}")

class StormModel(WeatherModel):
    """Model predicting severe storms."""
    
    def update_for_storm(self, storm_alert):
        """Increase probability sharply if storm alert is active."""
        factor = 0.9 if storm_alert else 0.3
        self.update_probability(factor)

class LightRainModel(WeatherModel):
    """Model predicting light rain showers."""
    
    def update_for_light_rain(self, cloud_coverage):
        """Adjust probability based on cloud coverage percentage."""
        factor = cloud_coverage / 100
        self.update_probability(factor)

# Example Usage
storm_model = StormModel()
storm_model.update_for_storm(True)  # Storm alert active
print(f"Rain Probability (After Storm Alert): {storm_model.get_probability()}")

light_rain_model = LightRainModel()
light_rain_model.update_for_light_rain(60)  # 60% cloud coverage
print(f"Rain Probability (After Light Rain Update): {light_rain_model.get_probability()}")

class AIWeatherPredictionModel(AdvancedWeatherModel, HumidityModel, WindModel):
    """AI-powered weather prediction combining multiple factors."""

    def ai_weather_update(self, temperature, humidity, wind_speed, confidence):
        """Apply AI-driven probability adjustments based on multiple weather factors."""
        temp_factor = (1 - (temperature / 100)) * confidence
        humid_factor = self.humidity_factor(humidity)
        wind_factor = self.wind_factor(wind_speed)

        combined_factor = (temp_factor + humid_factor + wind_factor) / 3
        self.update_probability(combined_factor)
        print(f"AI Model Predicted Rain Probability: {self.get_probability()}")

# Example Usage
ai_weather = AIWeatherPredictionModel()
ai_weather.ai_weather_update(22, 75, 20, 0.85)  # AI considers all factors