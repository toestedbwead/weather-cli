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

https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial
Weatherstack (simple, no key required for testing):

http://api.weatherstack.com/current?access_key={API_KEY}&query={city}

Required Features
1. City Input: Accept city name as command-line argument
2. Temperature Display: Show temperature in both Fahrenheit and Celsius
3. Weather Conditions: Display current weather conditions (sunny, rainy, etc.)
4. Additional Metrics: Show humidity, wind speed, and atmospheric pressure

Error Handling:
1. Invalid city names
2. API rate limits
3. Network connectivity issues
4. Missing API credentials
5. Weather Properties

Each weather response should display:
1. Temperature (Fahrenheit and Celsius)
2. Weather conditions description
3. Humidity percentage
4. Wind speed
5. Atmospheric pressure
6. Location name

Getting Started
1. Choose an API: Sign up for a free API key from OpenWeatherMap or Weatherstack
2. Setup: Store your API key securely (environment variables recommended)

Implementation:
1. Start with basic API connectivity
2. Add weather data parsing
3. Implement error handling
4. Add formatting and display
5. Constraints
6. Use only Python standard library for HTTP requests (urllib)
7. Handle all common error cases gracefully
8. Provide clear, user-friendly error messages
9. Format output for easy readability

Bonus Features (Optional)
1. Add support for country codes (e.g., "London,UK")
2. Implement temperature unit preference (metric/imperial)
3. Add weather icons using ASCII art
4. Cache results to avoid API rate limits
5. Add 5-day forecast functionality


'This project will help you practice API keys, query parameters, nested JSON parsing, and more complex error handling - all building on your GitHub API experience!


