from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '6de88e06fa7a4b4c420a3a6140f20b35'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        user_input = request.form.get('city')
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

        if weather_data.json()['cod'] != '404':
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            weather = f"The weather in {user_input} is {weather} with a temperature of {temp} degrees Celsius."

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)