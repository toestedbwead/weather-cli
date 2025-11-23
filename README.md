# Weather CLI Tool

Build a command-line application to fetch and display current weather information for any city.

## Requirements

The application should run from the command line, accept a city name as an argument, fetch the current weather using a weather API, and display it in the terminal. The user should be able to:

- Provide the city name as an argument when running the CLI
- Fetch current weather data from a weather API
- Display formatted weather information in the terminal
- Handle errors gracefully (invalid cities, API failures, network issues)

## Example Usage

```bash
# Basic usage
weather-cli "New York"

# Output:
# Weather for New York:
# - Temperature: 72°F (22°C)
# - Conditions: Partly cloudy
# - Humidity: 65%
# - Wind: 8 mph
# - Pressure: 1013 hPa

API Endpoints
You can use any of these free weather APIs:

OpenWeatherMap (recommended - generous free tier):

text
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial
Weatherstack (simple, no key required for testing):

text
http://api.weatherstack.com/current?access_key={API_KEY}&query={city}
Required Features
City Input: Accept city name as command-line argument

Temperature Display: Show temperature in both Fahrenheit and Celsius

Weather Conditions: Display current weather conditions (sunny, rainy, etc.)

Additional Metrics: Show humidity, wind speed, and atmospheric pressure

Error Handling:

Invalid city names

API rate limits

Network connectivity issues

Missing API credentials

Weather Properties
Each weather response should display:

Temperature (Fahrenheit and Celsius)

Weather conditions description

Humidity percentage

Wind speed

Atmospheric pressure

Location name

Getting Started
Choose an API: Sign up for a free API key from OpenWeatherMap or Weatherstack

Setup: Store your API key securely (environment variables recommended)

Implementation:

Start with basic API connectivity

Add weather data parsing

Implement error handling

Add formatting and display

Constraints
Use only Python standard library for HTTP requests (urllib)

Handle all common error cases gracefully

Provide clear, user-friendly error messages

Format output for easy readability

Bonus Features (Optional)
Add support for country codes (e.g., "London,UK")

Implement temperature unit preference (metric/imperial)

Add weather icons using ASCII art

Cache results to avoid API rate limits

Add 5-day forecast functionality

This project will help you practice API keys, query parameters, nested JSON parsing, and more complex error handling - all building on your GitHub API experience!


