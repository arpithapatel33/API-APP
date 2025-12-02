import requests

city = input("Enter city name: ")

api_key = "YOUR_API_KEY"   # put your API key here
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("\nWeather in", city)
print("Temperature:", data["main"]["temp"], "°C")
print("Feels like:", data["main"]["feels_like"], "°C")
print("Weather:", data["weather"][0]["description"])
