# python3 Py104_Ch2_realtime_weather2.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit
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
    unique_data = set(history_list)
    for entry in unique_data:
        print(entry)



def weather_query(user_input):
    weather_dict = {'key':'kooevgqw7vj6lcro', 'location':'user_input',
    'language':'zh-Hans', 'unit':'c'
    }

    weather_dict['location'] = user_input
    r = requests.get('https://api.seniverse.com/v3/weather/now.json', params = weather_dict)
    weather_response = r.json()

    Error_message = 'status'

    if Error_message in weather_response:
        print(weather_response['status'])
    else:
        weather_condition = weather_response['results'][0]['now']['text']
        temperature = weather_response['results'][0]['now']['temperature']

        weather_broadcasting = str(f'{user_input}的天气情况: {weather_condition}, 气温{temperature}摄氏度')

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
            weather_query(user_input)
"""
抓去返回异常status之后，此方法无用
            except KeyError:
                print("Maybe it's not a city, check your typo or enter 'h' for help.")
                continue
"""

start()

"""
## Changelog
此版本实现了国内城市天气中文查询，已迭代：
1. 更简单的url组装
2. 中文查询外国城市天气，API是否有权限，编码如何转换？API无权限，暂且搁置
3. 从json中取出更多的值，比如播报时间、风向

教练建议：
API 有提供查询不到结果的返回，可以判断一下再进行赋值
用 try...except... 来捕获 KeyError 是一个办法，但如果可以根据 API 文档对各种情况的返回进行处理，就更好了

## 下一步行动：
进阶任务
历史记录中过滤重复查询的城市，无查询记录时的反馈
"""
