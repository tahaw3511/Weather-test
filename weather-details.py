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

if __name__ == '__main__':
    app.run(debug=True)
