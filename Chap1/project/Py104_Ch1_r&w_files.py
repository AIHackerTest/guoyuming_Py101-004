#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, file1, file2 = argv 
# 引入两个文件，文件名字！＝此脚本中变量名字；with 后面可以看到，file1化身成data_file，file2化身to_file；这也好理解，你调用同一个文件，在不同代码作不同处理，变量名字会不同。

with open(file1) as data_file:
    indata = data_file.read() # 打开后读取文件内容
#    print(indata) # need not this if display is not necessary
    data_file.closed
    
# indata serves as the commuting variable, transfer the content 

with open(file2, 'r+') as to_file: # in writing mode, the file content is truncated 
    to_file.write(indata)
#    print(to_file.read())
    to_file.closed
