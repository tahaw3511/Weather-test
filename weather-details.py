from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample weather data for different cities with extended information
weather_data = {
    "New York": {
        "temperature": 18,
        "description": "Cloudy",
        "humidity": 80,
        "wind_speed": 15,  # in km/h
        "next_day_forecast": {
            "temperature": 20,
            "description": "Partly Cloudy"
        }
    },
    "Los Angeles": {
        "temperature": 25,
        "description": "Sunny",
        "humidity": 50,
        "wind_speed": 10,
        "next_day_forecast": {
            "temperature": 27,
            "description": "Sunny"
        }
    },
    "Chicago": {
        "temperature": 10,
        "description": "Rainy",
        "humidity": 90,
        "wind_speed": 20,
        "next_day_forecast": {
            "temperature": 12,
            "description": "Showers"
        }
    },
    "Houston": {
        "temperature": 30,
        "description": "Hot",
        "humidity": 60,
        "wind_speed": 5,
        "next_day_forecast": {
            "temperature": 32,
            "description": "Hot"
        }
    },
    "San Francisco": {
        "temperature": 17,
        "description": "Foggy",
        "humidity": 75,
        "wind_speed": 8,
        "next_day_forecast": {
            "temperature": 19,
            "description": "Clear"
        }
    }
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
