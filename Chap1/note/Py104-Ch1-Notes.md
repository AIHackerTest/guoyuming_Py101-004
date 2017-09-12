Ch1 Building Weather Consulting MVP
## 零碎不知道为什么的记录

## MVP 元思维
- 确定 MVP: 任务需要实现哪些功能？最核心的功能是什么？
- 确定开发计划：初步的实现思路是什么？如何一步步完成开发？
- 实现 MVP: 如何将核心功能转化为具体步骤？有哪些知识点可以用上？

### read a file:
you need to create a file as in buffering area in python, not the file stored in your disk. Just like Zed said, open. method is like creating a CD driver, while the file is the CD in it. 

尝试几番，遇到初级坑：当你文件命名test file.txt 时，import 两个argv，命令行输入脚本名和文件名，会提示too many values to unpack，我明明只有两个文件啊。文件名改成test_file，正常跑动。看来事先要掌握python命名规范啊。

文件读取输出已经很溜，卡片提示本章只涉及文件读写，还需要写入信息到文件。想到MVP功能之一是打印查询历史，这个可能要用一个文件来存放，之前做这个任务也是这么做的。那么来写一写。

先创建一个空txt文件。如何将数据从另一个文件中写入？参考Zed教程，用以下代码实现文件读写：
> importing 

### Dict 
- Python 中为什么有不同数据类型？
- 相比其他数据类型，Dict 类型有什么特点？
- 如何将用逗号分隔的两列字符串转换为字典？

### 复盘
卡住的地方有两处，
第一次在将txt文档转换成dict类型数据，文档每找到直接方法，google一下有案例。案例有坑，因为没有一个案例的数据类型、需求和你一样，所以用print大法一步步尝试。比如
> key, value = line.strip().split(',')

开始案例并没有strip().，打印出来的dict每一组都带/n，很恼人。虽然可以用，但是觉得好丑，心情一直过不去。因为之前做过这个任务，拿出来看以前代码，才加上strip，去掉空格、回车。

字典创建好，第二次卡在查询城市。以前用的好端端的if...in 语句忘了，这次看文档中说looping a dict, 写出了 for ... in 语句，结果每次不管输入什么词，都出来整个dict。而且在打印结果时候，用print(d[key])这样嵌套语句，开始没有写对，一直报错，后来证明可行。

最后储存并输出历史记录，已经忘了之前怎么做，想过用txt储存，想想要调用新的txt文件就想偷懒，那用list储存吧。之后代码几乎是自主心智一气呵成，模糊思路如下：

1. 先建一个list，这是Ch0学到的，函数操作前先把素材／数据准备好。list结构不熟悉，但list里面可以放str吧
2. str怎么储存？要放在变量里吧，那创建一个“历史条目”的变量，str如何与动态的城市、天气结合，用f ＋ {}的特性，这是3.6.2更新的。每个条目每搜索一次，就加入list里面，用append."历史条目"方法喽。
3. 查询结果，顺便把“历史条目”print出来。


### 下一步行动
1. Jupyter Notebook 撰写分享笔记
2. 解决Ch0遗留问题，改进猜数字程序
3. 学会调用函数，用函数封装写过的代码模块
4. 理解line.strip(), line.split(), 和dict.keys(), dict.items().

### Ch1 任务改进的点
1. 查询历史输出整个list，不是友好的展现方式，尝试用tuple，list，形式化出更简洁的历史记录。
2. 用户错误输入的限制和调试，比如输入英文和数字时，作何提示
3. 用函数封装



