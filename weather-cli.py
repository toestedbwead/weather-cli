import urllib.request
import json
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather-cli.py <city>")
        # print("\nExample: python weather-cli.py quezon-city")
        return
    
    city_name = sys.argv[1]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=8bfc491414bdb6b94393f87b01b5a0ce"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            # print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    if not data:
        print("{city_name} cannot be found.")
        return
    
    # Weather for New York:
# - Temperature: 72°F (22°C)
# - Conditions: Partly cloudy
# - Humidity: 65%
# - Wind: 8 mph
# - Pressure: 1013 hPa

    city = data['name']
    temperature = data['main']['temp_max']
    weather_condition = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    pressure = data['main']['pressure']

    # convert kelvin temp to celcius

    temperature = temperature - 273.15

    print(f"Weather for {city} City")
    print(f"Temperature: {temperature}")
    print(f"Weather Condition is: {weather_condition}")
    print(f"Humidity: {humidity}")
    print(f"Wind: {wind}")
    print(f"Pressure: {pressure}")


    


if __name__ == "__main__":
    main()