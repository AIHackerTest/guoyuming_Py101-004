Notes：
Coding involves storing and working with different data, we do so using variables. A variable stores a piece of data, and gives it a specific name. expanding your thoughts....

why use python to do math? Because you can combine math with other data types (e.g. booleans) and commands to create useful programs. Calculators just stick to numbers.

decimal cannot be define directly, rather you should using a division? 

aware of the point in decimal, key one point, even if it looks like a integer. This is where new coding thoughts are contrary to common sense. 

You can't write like upper(variablename), because methods that use dot notation only work with strings. Write, var + .upper(). On the other hand, len() and str() can work on other data types.

> lion = "roar"
len(lion)
lion.upper()

For input and output we have a short name, IO, so we have thigns like IO testing 

Variable = name + value, so only the two components added together or connected can a variable be called meaningful, or correctly processed by the program

# questions 

program language is different from natural langauge, in what ways? >>

python can handle or process these kinds of data: 



What is dynamic language, in perspective of variable


但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：

> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_abs
TypeError: unorderable types: str() >= int()
> abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'

在我们自己定义的函数my_abs('A')中，错误提示：字段和整数无法对比；在python内置函数中，错误提示：字段不能放入abs函数。在定义函数时，附带数据类型检查函数，例如用内置函数isinstance()实现。

从后往前一行行检查代码：让你更容易发现错误，利用人脑的反模式？但这样读似乎没有任何意义，发现不了意义也难读下去。还有一种检查代码方法，把它们大声读出来，包括标点。

Ex3:
输出时候，print函数变量带有一个字符串和一个数字，输出结果带括号。开始预感可能和版本有关，写3的代码，terminal还用2解析。可是思维定势让你不探究问题本源：即如何改变解析版本，而去用问题表象，比如“输出结果带括号”这样的关键字，绕弯搜索问题。用表象关键词其实是偷懒的表现，搜之前应该沿你之前的预感，先思考下可能的答案，在框架中搜索。

int() 把浮点数变成整数，比如20.0-20，6.75-6（注意取整而非四舍五入）

Ex4:
print（“字符串”, 变量, "字符串."）字符串的符号一定要在引号内部，表示那个符号属于字符串的一部分，否则报错。

Ex5:
3.6.2：You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters. 
总结将变量放进字符串中有三种方式, with my_name = 'Zed' defined:

1. Zed Shaw showed us in python3 to use {} to embed variable in the string, with f in the beginning of the "" to tell python3 that the string needs to be formatted. But this method is reported as error in python3.5. > print(f"Let's talk about {my_name}.")

2. Zed Shaw in Python2 use %s to replace the variable in the string. > print("let's talk about %s." % my_name)

3. 廖雪峰in Python3 use print() function to output two variables in one function. > print("Let's talk about", my_name)

升级到3.6.2之后，可以运行Zed Shaw python3代码；升级方法多种，比如最常见的下载安装包，直接在CLI就可以使用。


Ex6:
在study drills中，改变所有变量名字，最好的方式就是全局查找替换；虽然这个练习想要你熟悉变量名字和每行代码，但是还是用最有效不出错的方法。

编程与很多活动不同的地方，他可以获得即时反馈的心流状态，如同游戏中的设计一样。

Ex7:
为什么空格用，end='' 输出？就像注释中问的： watch end = ' ' at the end.  try removing it to see what happens

Ex8:
Define a variable with empty strings, with {} in the string to be assigned value, and print out different types of data. "I'm using something called a "function" to turn the formatter variable into other strings". But things in {} are not called value, but arguments. So simply differ argument from parameters: "While defining method, variables passed in the method are called parameters; while using those methods, values passed to those variables are called arguments." So parameter are used in seting a function or method, while argument are passed as values to those methods. 

Ex11:
end='' at the end of each print line, this tells print function to not end the line with a newline character and go to the next line? how to understand this? what do we mean by newline character? 

With coding experiment like this, I have found out the difference between with and without end=''. If you use it:
> print("What is your gender?", end='')
gender = input()
export: What is your gender? male

The input place doesn't begin with a new line but follow the string, right after the ？mark.

If you don't use it, 
> print("What happen?")
happen = input()
What happen?
Nothing

The input place begin from next line. So that's what we call "not to end the line with a newline character". Take end='' just as a sign to skip auto return hitting.

Ex12:
Summary of input():

1. If the input function is called, the program flow will be stopped until the user has given an input and has ended the input with the return key.  

Ex13:
Hard to explain argv because I don't fully understand it. But a obscure picture had emerged: you pass variable to some already made scripts, like using wheeling to make cars rather than building wheels. 

argv is used before executing the script, like you sign in a website, while input is used when you are logged in and browse the website. 

Ex15:
If you import file as an argv, do not forget to write the file name with its suffix, like "sample.txt".

探索记录：

今天投入多长时间练习编程？
探索了哪些技能点？
分别花费了多少时间、探索到什么程度？
建议详细记录自己完整的折腾历程、相应时间，以便挖掘时间黑洞，改善自己的学习效率。

复盘 & 改进：
今天有哪些收获？
有哪些有用的经验、技巧可以在未来复用？
哪些地方做得不好？打算如何改进？

尽可能记录下来自己的学习探索过程：
怎么设想的？
怎么尝试的？
怎么失败的？
怎么搜索的？

验证自己的想法，是否匹配真实世界，然后校准改变自己的想法。

大妈说：
对问题足够清晰定义，查问题之前，是否排查过代码，形成调试习惯，习惯之上主观意识判定，到哪一步了

编译器报错离自己问题差了十万八千里

技术文档，有固化的结构，应用文。

信心问题：对搜索有信心，他19年从来没碰过网上没有答案的问题；互联网中有一切资源，只是你没有找到。因为技术从外国来，中国复制，之前没有中国用过而外国没有的技术。大妈一般搜索3-4天，搜索几百次才慢慢找到答案。

用谷歌怎么找到关键词？先用中文百度搜，找到类似问题描述，转回英文；更省力的方法，在youtube里面查

追求效率不一定用软件解决，但以效率为出发点，你的路径、速度会不同

相同行为反复进行，不可能出现不同结果；不要重复无效行为。等待问题自己被解决，是以往的思维定势，但不是编程的思维。
