#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python3 Py104_Ch2_realtime_weather.py

from sys import argv, exit
import requests, json

# testing blocks
#weather_dict = {'q':'city_name', 'APPID':'33f65ff60f2eb1575caa188775e86c28'}
#r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=weather_dict)
#print(r.url)

history_list = []

def user_guide():
    print("""
    Type q or quit to exit the program
    Type s or history to see search history
    Type h or help for user guide
    Type city name to search for the weather
    """)

def user_quit():
    print('Thankyou for using Xiaoming Weather')
    exit(0)

def user_history():
    print("You have looked into the following cities: ")
    for history_entry in history_list:
        print(history_entry)



def weather_query(user_input):
    query_url = str(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&APPID=33f65ff60f2eb1575caa188775e86c28')
    r = requests.get(query_url)
    weather_response = r.json()

    weather_condition = weather_response['weather'][0]['main']

    weather_broadcasting = str(f'{user_input}: {weather_condition}')

    history_list.append(weather_broadcasting)

    print(weather_broadcasting)

def start():
    print("Welcome to Xiaoming Weather,please type in city name directly or enter 'h' for help: ")

    while True:
        user_input = input("> ")

        if user_input == 'h' or user_input == 'help':
            user_guide()

        elif user_input == 'q' or user_input == 'quit':
            user_quit()


        elif user_input == 'history' or user_input == 's':
            user_history()

        else:
            try:
                weather_query(user_input)
            except KeyError:
                print("Maybe it's not a city, check your typo or enter 'h' for help.")
#                continue


start()
