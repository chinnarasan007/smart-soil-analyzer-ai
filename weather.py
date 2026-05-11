import requests

def get_weather(city_name):
    # Your API Key remains the same
    api_key = "2c6e64084668f9cae60703b7ac387b80" 
    
    # We change the URL to use 'q' (query) instead of lat and lon
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        print(f"Checking Weather for {city_name}...")
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            hum = data['main']['humidity']
            desc = data['weather'][0]['description']
            print(f"✅ Weather Found for {city_name}: {temp}°C")
            return temp, hum, desc
        else:
            # This helps if the user types a city name that doesn't exist
            print(f"❌ Weather API Error: {data.get('message')}")
            return 25.0, 50.0, "Weather data unavailable"
            
    except Exception as e:
        print(f"❌ Weather Connection Failed: {e}")
        return 25.0, 50.0, "Connection Error"