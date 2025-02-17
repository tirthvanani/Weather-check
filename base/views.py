from django.shortcuts import render
import requests

# Function to get weather data
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = 'b1206708e5c8f9b06abb7f6b5b51427f'  
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def home(request):
    city = request.GET.get('city')
    icon_url = 'https://openweathermap.org/img/wn/10d@2x.png' 

    weather = "N/A"
    weather_description = "No Data"
    country = "N/A"
    wind_speed = 0
    pressure = 0
    humidity = 0
    temperature = 0

    if city:
        weather_data_result = get_weather(city)
        if weather_data_result:
            icon_id = weather_data_result['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"

            weather = weather_data_result['weather'][0]['main']
            weather_description = weather_data_result['weather'][0]['description']
            city = weather_data_result['name']
            country = weather_data_result['sys']['country']
            wind_speed = weather_data_result['wind']['speed']
            pressure = weather_data_result['main']['pressure']
            humidity = weather_data_result['main']['humidity']
            temperature = weather_data_result['main']['temp']
        else:
            return render(request, 'index.html', {'error': "City not found! Please enter a valid city name."})

    context={
        'icon_url': icon_url,
        'weather': weather,
        'weather_description': weather_description,
        'city': city,
        'country': country,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'humidity': humidity,
        'temperature': temperature,
    }
    return render(request, 'index.html',context)