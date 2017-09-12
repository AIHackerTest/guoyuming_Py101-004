#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit

script, filename = argv

weather_dict = {}
with open(filename) as data_file:
    for line in data_file:
        key, value = line.strip().split(',')        
        weather_dict[key] = value


history_list = []

def user_guide():
    print("""直接输入城市名称查询对应天气，
        输入'帮助'，查看如何使用
        输入‘历史’，查看搜索记录
        输入'退出'，退出程序
        """)



def user_quit():
    print("不管窗外如何，心中一片艳阳，谢谢查询")
    exit(0)

def user_history():
    print("你查询过以下城市：")
    for history_entry_saved in history_list:
        print(history_entry_saved)

    
def user_search(user_input):    
    weather_result = weather_dict[user_input]
    history_entry = str(f"{user_input} 的天气状况为 {weather_result}") # 神来之笔
    history_list.append(history_entry)
    print(history_entry)
    
    
def user_abnormal():
    print("进入未知天气领域，可能你输入的不是城市名称哦，如需更多指引，请输入‘帮助’来查看\n")

 


def start():
    print("欢迎来到小明天气，输入城市名称直接查询天气,或输入‘帮助’查看用户指南")   
    
    while True:
        user_input = input("> ")
    
        if user_input == '帮助':
            user_guide()

    
        elif user_input == '退出':
            user_quit()
        
        elif user_input == '历史':
            user_history()

    
        elif user_input in weather_dict.keys():
            user_search(user_input)

    
        else:
            user_abnormal()

start()

# 卡住的两处：1 用户输入之后，loop迭代停不下来；好吧，我已经忘记当时代码状态了，改变代码之后，def 一个主程序，将user_input 放入主程序，如此实现用户持续输入，直到exit(0)条件满足；2: 问题1解决之后，输入各个指令正常，除了查询功能，输入任何城市名称都跑“异常输入”程序；尝试把构建字典放进def，报其他错误；str()输入字段，没变化，因为用户输入本身就是str类型数据。最后将def user_search():  改成def user_search(user_input): if 括号中同样加上user_input，跑通。因为def user_search()函数本身需要包含变量，所以括号中要有变量名称，否则定义不完整，同时无法触发函数。