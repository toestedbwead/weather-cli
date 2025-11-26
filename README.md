# Weather CLI Tool

A command-line application to fetch and display current weather information for any city using the OpenWeatherMap API.

## Features

- Get current weather for any city worldwide
- Display temperature in both Celsius and Fahrenheit
- Show weather conditions, humidity, wind speed, and atmospheric pressure
- Clean, formatted output in the terminal
- Robust error handling for invalid cities and API issues
- Secure API key management using environment variables

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a .env file in the project root and add: 'WEATHER_API_KEY=your_key_here'
5. Get API key from OpenWeatherMap


## Usage

```bash
python weather-cli.py "City Name"
```

# Get weather for a city
python weather-cli.py "New York"
```
# Output:
# Weather for New York City
# Temperature: 22°C | 72°F
# Weather Condition is: partly cloudy
# Humidity: 65%
# Wind: 8mph
# Pressure: 1013hPa
```

# API
This project uses the OpenWeatherMap API:
Endpoint: https://api.openweathermap.org/data/2.5/weather
Free tier: available with registration
Returns: data in JSON format

# Technical Details
1. Built with Python standard library (urllib, json, sys)
2. Handles JSON parsing and data extraction
3. Implements temperature conversion (Kelvin to Celsius/Fahrenheit)
4. Robust error handling with specific HTTP status code checks
5. Secure environment variable configuration

# Development
This project helps practice:
1. API integration and API keys
2. HTTP requests with urllib
3. JSON parsing and data extraction
4. Error handling and edge cases
5. Command-line interface development
6. Temperature unit conversions
7. Environment Variable Security