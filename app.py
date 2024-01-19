import requests

api_key = '6de88e06fa7a4b4c420a3a6140f20b35'

user_input = input("Enter the city name: ")



weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found")
    exit()
else:
#print(weather_data.json())
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    #print (weather, temp)
    print(f"The weather in {user_input} is {weather} with a temperature of {temp} degrees Celsius.")