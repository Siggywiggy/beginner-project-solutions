#! python3
# a progam that pulls data from openweathermap.org

from api_credentials import openweathermap_api_key as api_key
import requests
from datetime import datetime
import webbrowser


def location_to_geocode(location, api_key):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
    }
    base_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
    limit = 'limit=1'
    response_from_api = requests.get(base_url + location + '&' + limit + '&' + 'appid=' + api_key, headers)

    return response_from_api.json()[0]['lat'], response_from_api.json()[0]['lon']


def five_day_forecast(latitude, longitude, api_key):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
    }
    base_url = 'http://api.openweathermap.org/data/2.5/forecast?lat='
    units = 'metric'
    try:
        response_from_api = requests.get(
            base_url + str(latitude) + '&lon=' + str(longitude) + '&units=' + units + '&appid=' + api_key,
            headers=headers)

    except requests.exceptions.RequestException as exc:
        print(f"Something went wrong: {exc}")
        print(exc.response.status_code)

    if response_from_api.status_code == 200:
        sunrise = datetime.fromtimestamp(response_from_api.json()['city']['sunrise'])
        sunset = datetime.fromtimestamp(response_from_api.json()['city']['sunset'])
        print(f'The sun rises at {sunrise.strftime("%H:%M")} and sets at {sunset.strftime("%H:%M")}')

        # open and start the .html file
        with open('weather_forecast.html', 'a') as html_file:
            html_file.write('<!DOCTYPE html>\n')
            html_file.write('<html>\n')
            html_file.write('<body>\n')
            html_file.write(
                f'<h2> The sun rises at {sunrise.strftime("%H:%M")} and sets at {sunset.strftime("%H:%M")}</h2>\n')
            html_file.write('<h1>The weather forecast for the next 5 days is:</h1>\n')
        # loop trough all the 3 hour data intervals
        for i in range(0, 40):
            time_1 = datetime.fromtimestamp(response_from_api.json()['list'][i]['dt'])
            temperature = response_from_api.json()['list'][i]['main']['temp']
            humidity = response_from_api.json()['list'][i]['main']['humidity']
            clouds = response_from_api.json()['list'][i]['weather'][0]['description']
            windspeed = response_from_api.json()['list'][i]['wind']['speed']
            direction = response_from_api.json()['list'][i]['wind']['deg']

            print(
                f'On {time_1.strftime("%A, %d. %B,")} from {time_1.strftime("%H:%M")} hours the weather is as follows:')

            print(
                f'Temperature is {temperature} C, relative humidity is {humidity} %, percipitation and clouds: {clouds},\nwind is blowing {windspeed} m/s and wind direction is {direction} degrees.')

            # create a text file with the firecast data
            with open('weather_forecast.txt', 'a') as forecast_file:
                forecast_file.write(
                    f'On {time_1.strftime("%A, %d. %B,")} from {time_1.strftime("%H:%M")} hours the weather is as follows:\n')
                forecast_file.write(
                    f'Temperature is {temperature} C, relative humidity is {humidity} %, percipitation and clouds: {clouds},\nwind is blowing {windspeed} m/s and wind direction is {direction} degrees.\n')
            # write hourly forecast data to .html file
            with open('weather_forecast.html', 'a') as html_file:
                html_file.write(
                    f'<p>On {time_1.strftime("%A, %d. %B,")} from {time_1.strftime("%H:%M")} hours the weather is as follows:\n</p>')
                html_file.write(
                    f'<p>Temperature is {temperature} C, relative humidity is {humidity} %, percipitation and clouds: {clouds},\nwind is blowing {windspeed} m/s and wind direction is {direction} degrees.\n</p>')
        # finish the .html file
        with open('weather_forecast.html', 'a') as html_file:
            html_file.write('</body>\n')
            html_file.write('</html>\n')

        webbrowser.open_new_tab('weather_forecast.html')


latitude, longitude = location_to_geocode('Tallinn', api_key)
five_day_forecast(latitude, longitude, api_key)