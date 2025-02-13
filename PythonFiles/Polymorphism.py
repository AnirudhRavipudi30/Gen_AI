import random

# Parent Class (Base AI Model)
class AIModel:
    def predict_probability(self):
        """Generic probability prediction (to be overridden)."""
        return 0.5  # Default probability

# Child Class: AI for Text Analysis (Fake News Detector)
class TextAI(AIModel):
    def predict_probability(self):
        """Predict probability of text being real using a confidence score."""
        confidence_score = random.uniform(0.5, 0.9)  # AI-generated score
        return round(confidence_score, 2)

# Child Class: AI for Weather Prediction
class WeatherAI(AIModel):
    def predict_probability(self):
        """Predict probability of rain using Bayesian Probability."""
        prior_prob = 0.3  # Assume 30% prior chance of rain
        humidity_factor = random.uniform(0.6, 0.9)  # High humidity → more rain chance
        updated_prob = (prior_prob * humidity_factor) / ((prior_prob * humidity_factor) + ((1 - prior_prob) * (1 - humidity_factor)))
        return round(updated_prob, 2)

# Child Class: AI for Stock Market Prediction
class StockAI(AIModel):
    def predict_probability(self):
        """Predict probability of stock price increase using AI confidence."""
        market_trend = random.uniform(0.4, 0.8)  # AI prediction of market trend
        volatility = random.uniform(-0.1, 0.1)  # Small adjustments for uncertainty
        return round(min(1, max(0, market_trend + volatility)), 2)  # Ensuring probability is between 0-1

# Using Polymorphism: Running Predictions from Different AI Models
ai_models = [TextAI(), WeatherAI(), StockAI()]

for model in ai_models:
    print(f"{model.__class__.__name__} predicted probability: {model.predict_probability()}")