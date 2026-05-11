import requests

def get_location():
    try:
        print("Checking Location...")
        response = requests.get('http://ip-api.com/json/', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            print(f"✅ Found: {data['city']}")
            return data['city'], data['regionName'], float(data['lat']), float(data['lon'])
    except Exception as e:
        print(f"❌ Location API Failed: {e}")
    
    return "Location Error", "Check Internet", 13.0, 80.0