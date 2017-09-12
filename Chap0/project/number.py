#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 开始我用的是random.randint(a, b)这条命令从官方代码里看到，以为找到了救主，报错提示说random没有被定义，后来查到stackoverflow告诉你如下写法。原来你不懂官方文档的格式。据此推测，应该 . 前面是package，从库中import；后面是funtion，但也有人写成random.randint()，说明import是必须的，写法可能只写randint会不严谨

from random import randint

No1 = randint(0,9) 
print(No1)

def input_number(x):
    while True:
        try:
            user_input = int(input(x)) 
        except ValueError:
            print("你输入的不是整数，请重新输入哦")
            continue
        else:
            return user_input
            break
            
 
#print(type(input_number)) # 用以判断user_input变量的数据类型
        
choice_left = 10 # 定义开始机会次数

while choice_left > 0: # 这是你之前没有想到的，想要用户不断输入，把input放在while里面
    number_guessed = input_number("请输入你猜的10以内整数：")  
    number_guessed = int(number_guessed) 

# 如果没有下面这句，会报错： '<' not supported between instances of 'str' and 'int'，也就是这行把用户输入转化成整数;because "the input() function always returns a string of teuser_inputt the player typed"

    
           
    choice_left = choice_left - 1 # 每输入一次，机会少一，传给while判断条件是否还满足；“the choice left variable should be one less than what it already is, the outcome of the operation is stored as the new value of guessesTaken”
    
        
    if number_guessed < No1: 
        print(f"小了，你还有 {choice_left} 次机会。")
        

    if number_guessed > No1:
        print(f"大了，你还有 {choice_left} 次机会。") 
    
    if number_guessed == No1: # 在不断猜测循环过程中猜对
        print("棒！猜对了") 
        break # 就算while条件还满足，也会提前结束循环，break会将命令结束在break处，之后命令不会执行了，所以位置放好
        

#if user_input == No1: # 一次就猜对的情况
#    print("厉害，一次就猜对！")



"""
### 复盘：
用时1h40min。第一次卡在判断用户输入等于随机数字语句，用＝会报错，偶然想到＝是定义，用＝＝才代表相等。第二次卡在代码block已经写出，组合顺序不对，如何让用户不断输入数字，我总想如何def定义input，然后不断调用input观赏完类似游戏代码，发现破局点在把input放在while下面，把迭代公式放在while下面。

python是好懂的语言，从上到下按顺序执行。比如while下面命令不断被执行，比如这个例子input、迭代公式、print都不断在跑；直到while后的条件满足不了。if不执行任何命令，只做条件判断。

思考重点：判断以什么为标准循环－所剩机会；循环时不同条件下执行什么命令；

步骤：最先定义好变量，那么想这个程序需要哪些变量，数据类型是什么、排查机制，再对变量执行操作
     
提升点：用函数封装block、一次就猜对的break、机会都用完game over的break、数据检查
   
"""
