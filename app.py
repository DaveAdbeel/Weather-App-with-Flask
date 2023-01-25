import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=18a5a253d56db143739cd76ab8ea8fd3'
    city = "Las Vegas"

    res = requests.get(url.format(city)).json()
    
    temp = res['main']['temp']
    desc = res['weather'][0]['description']
    icon = res['weather'][0]['icon']

    weather = {
        "city": city,
        "temp": temp,
        "desc": desc,
        "icon": icon,  
    }

    return render_template('weather.html', weather=weather)
