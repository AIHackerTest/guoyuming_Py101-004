#  python3 search_weather.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def weather_query(user_input):
    weather_dict = {'key':'kooevgqw7vj6lcro', 'location':'user_input',
    'language':'zh-Hans', 'unit':'c'
    }
#    user_input = '北京'
    weather_dict['location'] = user_input
    r = requests.get('https://api.seniverse.com/v3/weather/now.json', params = weather_dict)
    weather_response = r.json()

    # Error_message = 'status'
    # if Error_message in weather_response:
    #     return weather_response['status']
    #
    # else:
    weather_condition = weather_response['results'][0]['now']['text']
    temperature = weather_response['results'][0]['now']['temperature']

    weather_broadcasting = str(f'{user_input}的天气情况: {weather_condition}, 气温{temperature}摄氏度')

    return user_input, weather_condition, temperature
