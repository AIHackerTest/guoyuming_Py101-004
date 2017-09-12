#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, file1 = argv

weather_dict = {} # create a dict variable
with open(file1) as data_file:
    for line in data_file:
        key, value = line.strip().split(',') 

# create a tuple and assign them with the strings splitted by ","? There is a problem, the output of dict has marks like {'北京': '晴\n', '海淀': '晴\n'..., the \n can bother? Then you add .strip() before the .split(), which removes all white space, returns. 

        weather_dict[key] = value # initiate the dict by assigning key and val respectively?

history_list = []

print("欢迎来到小明天气，输入城市名称直接查询天气,或输入‘帮助’查看用户指南")

while True:
    user_search = input('> ') # input放在while下面就让用户不断输入，再后面放if就是判断用户输入是否满足某些条件

    if user_search in weather_dict.keys(): # use dict.keys() rather than dict.items()
        weather_result = weather_dict[user_search]
        history_entry = str(f"{user_search} 的天气状况为 {weather_result}") # 神来之笔
        history_list.append(history_entry)
        print(history_entry)

# another successful way of print the search result is using:  print(weather_dict[user_search]), explore it later

    elif user_search == '帮助':
        print("""直接输入城市名称查询对应天气，
        输入'帮助'，查看如何使用
        输入‘历史’，查看搜索记录
        输入'退出'，退出程序
        """)

    elif user_search == '退出':
        print("不管窗外如何，心中一片艳阳，谢谢查询")
        break
    
    elif user_search == "历史":
        print(f"你查询过以下城市：{history_list}")
    
    else:
        print("进入未知天气领域，请试试输入其他内容哦\n")
    
    

