from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample weather data for different cities
weather_data = {
    "New York": {"temperature": 18, "description": "Cloudy", "humidity": 80},
    "Los Angeles": {"temperature": 25, "description": "Sunny", "humidity": 50},
    "Chicago": {"temperature": 10, "description": "Rainy", "humidity": 90},
    "Houston": {"temperature": 30, "description": "Hot", "humidity": 60},
    "San Francisco": {"temperature": 17, "description": "Foggy", "humidity": 75}
}

# Route for getting the weather forecast for a city
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "City not provided"}), 400

    forecast = weather_data.get(city)

    if not forecast:
        return jsonify({"error": "City not found"}), 404

    return jsonify({
        "city": city,
        "forecast": forecast
    })

# Route for getting weather forecast for multiple cities
@app.route('/weather/multiple', methods=['GET'])
def get_weather_multiple():
    cities = request.args.getlist('cities')
    
    if not cities:
        return jsonify({"error": "No cities provided"}), 400

    forecasts = {city: weather_data.get(city, "City not found") for city in cities}

    return jsonify(forecasts)

# Route for adding/updating weather data for a city
@app.route('/weather', methods=['POST'])
def add_or_update_weather():
    data = request.json

    city = data.get('city')
    temperature = data.get('temperature')
    description = data.get('description')
    humidity = data.get('humidity')

    if not city or not temperature or not description or not humidity:
        return jsonify({"error": "Incomplete data provided"}), 400

    weather_data[city] = {
        "temperature": temperature,
        "description": description,
        "humidity": humidity
    }

    return jsonify({"message": f"Weather data for {city} added/updated successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

