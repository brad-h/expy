"""Grabbing the weather"""

import os
import urllib.request
import json
import datetime
import module18

_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def _get_weather(zip_code, api_key):
    """Given a zip_code and an Open Weather Map API key
    Produce a parsed JSON payload with weather information for that zip_code
    """
    url = '{}zip={},us&appid={}&units=imperial'.format(_BASE_URL, zip_code, api_key)
    with urllib.request.urlopen(url) as response:
        body = response.read()
    return json.loads(body)

def _format_datetime_from_unix(unix_time):
    """Given a unix time integer (number of seconds since epoch - January 1970)
    return a string formatted as YYYY-MM-DD HH:MM:SS
    """
    date = datetime.datetime.fromtimestamp(unix_time)
    return date.strftime('%Y-%m-%d %H:%M:%S')

def ex48(api_key):
    """api_key: an Open Weather Map API key
    Prompt for zip_code, display temperature
    """
    # so much easier by ZIP code, not going to bother with trying
    # to do a fuzzy reverse lookup by a city and possibly state
    zip_code = int(input('What ZIP code are you in? '))
    content = _get_weather(zip_code, api_key)
    print('{} weather:'.format(content['name']))
    temp_f = content['main']['temp']
    temp_c = module18.fahrenheit_to_celsius(temp_f)
    print('{} degrees Fahrenheit; {} degrees Celsius'.format(temp_f, temp_c))
    print('Description: {}'.format(', '.join(x['description'] for x in content['weather'])))
    print('Sunrise: {}'.format(_format_datetime_from_unix(content['sys']['sunrise'])))
    print('Sunset: {}'.format(_format_datetime_from_unix(content['sys']['sunset'])))

if __name__ == '__main__':
    OPEN_WEATHER_MAP_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')
    ex48(OPEN_WEATHER_MAP_API_KEY)
