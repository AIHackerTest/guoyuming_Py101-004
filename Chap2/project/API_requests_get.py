#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

imoprt requests 

weather_dict = {'q':'city_name', 'APPID':'33f65ff60f2eb1575caa188775e86c28'}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=weather_dict)
print(r.url)

city_name = input
query_url = str(f'https://api.openweathermap.org/data/2.5/weather?q= {city_name} &APPID=33f65ff60f2eb1575caa188775e86c28'
r2 = requests.get(query_url)
print(r2)