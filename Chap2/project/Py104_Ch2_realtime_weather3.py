# python3 Py104_Ch2_realtime_weather3.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## 亮点即刻意练习到的点：
1. 探索pass two variables to a function,变量层层传到，详尽办法减少代码行数，发现要学面向对象的方法
2. 因为同一服务商的api，直接推倒如何取出所需json字段，而没有拆解字典了
3. 历史记录去重复
4. 思考如何调用函数的函数，如何尽可能封装，未果，但之后一个方向
5. 循环之内的循环，如何切换，加深理解了while和continue
7. 合并同类项，删去过渡变量，代码减少两行

## 可改进的地方
1. 似乎告知用户 今天、明天、后天 比给出日期更直观，但要多谢好多if
2. 思考如何把同类项尽可能提取，封装
3. 涉及时间、城市二次选择，所以循环分两层，两层命令无相互打通，
要＃来切换菜单层级。如果选择变多，路径变更长，如何优化这点，减少用户输入
4. 卡包所说，C和F温表相互切换
"""

import requests
import json

history_list = []

def user_guide():
    print("""
    输入1、2、3，对应查询今、明、后天的天气
    输入 h 或 帮助，查看用户指南
    输入 s 或 历史，查看查询记录
    输入 q 或 退出，退出程序
    """)

def user_exit():
    print("不管窗外如何，心中一片艳阳天")
    exit(0)

def abnormal():
    print("换个命令试试，输入1、2、3或帮助")

def user_history():
    unique_data = set(history_list)
    for entry in unique_data:
        print(entry)

def weather_query(input_city, input_date):
    weather_dict = {'key':'kooevgqw7vj6lcro', 'location':'input_city', 'language':'zh-Hans',
    'unit':'c', 'start':'0', 'days':'input_date'
    }

    weather_dict['location'] = input_city
    weather_dict['days'] = input_date
    url = 'https://api.seniverse.com/v3/weather/daily.json'
    weather_response = requests.get(url, params = weather_dict).json()

    if 'status' in weather_response: # all error message return json data with this word
        alert = weather_response['status']
        print(f"错误提示:{alert} 请检查城市名称，或输入'#'返回主菜单")
    else:
        which_day = int(input_date) - int(1) # 今日最佳行
        ask_day = weather_response['results'][0]['daily'][which_day]['date']
        condition = weather_response['results'][0]['daily'][which_day]['text_day']
        high = weather_response['results'][0]['daily'][which_day]['high']
        low = weather_response['results'][0]['daily'][which_day]['low']
        c = u'°C'

        weather_broadcasting = str(f"{input_city}{ask_day}天气：{condition}, 最高气温{high}{c}, 最低气温{low}{c}")

        history_list.append(weather_broadcasting)

        print(weather_broadcasting)


def start():

    print("""
    欢迎来到小明天气，你可以查询今、明、后三天的天气：
    输入 1 查询今日天气
    输入 2 查询明天天气
    输入 3 查询后天天气
    输入 h，查看用户指南
    """)
    while True:
        input_date = input('> ')

        if input_date == '1':
            print("查询今日天气，请输入城市名称，或输入 ‘＃’，返回主菜单：")
            while True:
                input_city = input('> ')
                if input_city == '#':
                    start()
                else:
#                    input_date = '1'
                    weather_query(input_city, input_date)

        elif input_date == '2':
            print("查询明天天气，请输入城市名称，或输入 ‘＃’，返回主菜单：")
            while True:
                input_city = input('> ')
                if input_city == '#':
                    start()
                else:
#                    input_date = '2'
                    weather_query(input_city, input_date)

        elif input_date == '3':
            print("查询后天天气，请输入城市名称，或输入 ‘＃’，返回主菜单：：")
            while True:
                input_city = input('> ')
                if input_city == '#':
                    start()
                else:
#                    input_date = '3'
                    weather_query(input_city, input_date)

        elif input_date in ['h', '帮助']:
            user_guide()

        elif input_date in ['q', '退出']:
            user_exit()

        elif input_date in ['s', '历史']:
            user_history()

        else:
            abnormal()



start()
