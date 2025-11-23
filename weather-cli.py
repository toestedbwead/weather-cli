import urllib.request
import json
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather-cli.py <city>")
        print("\nExample: python weather-cli.py quezon-city")
        return
    
    city_name = sys.argv[1]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=8bfc491414bdb6b94393f87b01b5a0ce"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            print(f"Weather for {city_name}")
            # print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    if not data:
        print("{city_name} cannot be found.")
        return
    
    for city in data:
        weather = weather['main']
        temperature = main['temp']
        pass

    # get temperature (far to celcius), conditions: partly cloudy, humidity, wind and pressure

    # if else statements - analyze the json response 

    # find out how to access the datas in the json response like the code above. i feel like it's not being accessed.
    


if __name__ == "__main__":
    main()