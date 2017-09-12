#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


while True:
    user_input = input('Please enter a number > ')
    
    if user_input == 'quit':
        exit(0)
    
    if user_input != 'quit':
        try:
            value = int(user_input)
        except ValueError:
            print("This is not a number")
            
        

    print(user_input)

# 直白思路：
# 数据验证部分：1. 用户总要输入，放一个输入功能；2. 用try来做数据类型验证，try ＝ to see if the data tpyed in is an integer, except = if not, print error message and stop exerting the script. 3. If true (is an integer), continue to exert the script. 
# 功能模块部分：1. 做数据验证时，发现while true不断循环，只能关闭窗口退出，于是乎，加入一个输入quit，退出功能。因为quit是唯一值，所以 user_input = quit = 执行退出，不等于quit时执行输入验证。至此完整数据验证程序写好。