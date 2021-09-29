#注释：
#i=10
#李艳莹的第一个注释
#print(i) #给狗蛋儿来一个注释
#代表单行注释
#print("Hello,Python!")

'''
狗蛋的第二个注释：用英文三个单引号  简称：三引号
'''
import math

"""
狗蛋的第三个注释：用英文的三个双引号
"""

# if True:
#     print("True")
# else:
#     print("False")
#  #print(dkdk) 报错 # 缩进不一致，会导致运行错误
#
# #Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠\来实现多行语句，
# #在[]{}()中的多行语句，不需要使用反斜杠\
#
# #python中数字有四种类型： 整数、布尔型、浮点数和复数
#
# #"""可以指定一个多行字符串
# #paragraph = """这是一个段落,
# str = '123456789'
#
# print(str)  #输出字符串
# print(str[0:-1])  #输出第一个到倒数第二个的所有字符
# print(str[0])  #输出字符串第一个字符
# print(str[2:5])   #输出从第三个开始到第五个的字符
# print(str[2:])   #输出从第三个开始后的所有字符
# print(str[1:5:2])  #截取字符串语法  变量[头下标：尾下标：步长]
# # 输出从第二个开始到第五个且每隔一个的字符（不长为2）
# print(str * 2)  # *星号 代表重复  即是：输出字符串两次
# print(str + '你好') # 连接字符串
# print('__________________________')
# print('hello\nrunoob') #使用反斜杠（\）+n转义特殊字符
# print(r'hello\nrunnob')
#
# x="a"
# y="b"
# print(x)  #换行输出
# print(y)
#
# #不换行输出
# print(x,end="")
# print(y,end="")
#
# import sys
# print('_______________Python import mode_________________')
# print('命令行参数为：')
# for i in sys.argv:
#     print(i)
# print('\n python路径为',sys.path)

#python变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建

#Python中有6个标准的数据类型
# 不可变数据（3个）：Number(数字) String(字符串)  Tuple(元组)
# 可变数据（3个）：List(列表)、Dictionary(字典)、Set(集合)

# a,b,c,d = 20,5.5,True,4+3j  #python可以同时为多个赋值
# print(type(a),type(b),type(c),type(d))
#type(变量) 可以用来查询变量所指向的对象类型

# a = 111
# print(isinstance(a,int))
#isinstance()可以用来判断 变量是否是指定类型
#区别：type()不会认为子类是一种父类类型；
#isinstance()会认为子类是一种父类类型

#Python3中，bool是int的子类。True和False可以和数字相加True==1.False==0是会返回True

# del #语句删除单个或多个对象
# var1 = 1
# print(var1)
# del var1

#除法 / 得到一个浮点数
# print(2/4)
# #除法 // 得到一个整数
# print(2//4)
#
# #取余 1
# print(17%3)
#
# #python还支持复数，复数由实数部分和虚数部分构成，可以用a+bj表示
#
# #python中的字符串用单引号‘或者双引号“括起来，同时使用反斜杠\转义特殊字符
#
# #乘方
# print(2**5)

# print('Ru\noob')  #\n代表换行
# print(r'Ru\noob')  #不想让反斜杠发生转义，可以再字符串前面添加一个r


#python字符串
#python字符串不能改变
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义
#字符串可以用+运算符连接在一起，用*运算符表示重复
#python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始

#List（列表）
#列表中元素类型可以不相同，支持数字、字符串

# list = ['abcd','786',2.23,'runnoob',70.2]
# tinylist = [123,'runnob']

# print(list)  #输出完整列表
# print(list[0]) #输出列表第一个元素
# print(list[1:3])
# print(list[2:]) #输出从第三个元素开始的所有元素
# print(tinylist * 2) #输出两边列表
# print(list + tinylist)

# def reverseWords(input):
#     inputWords = input.split("")
#     #翻转字符串
#     inputWords = inputWords[-1::1]
#     #重新组合字符串
#     output = ' '.join(inputWords)
#     return output
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)


#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号（）里
#tuple元素不可改变，但可以包含可变的对象，比如list列表
#构造包含0个或者1个元素的元组比较特殊，
#和字符串一样，元组的元素不能修改
# tup1 = ()  #空元组
# tup2 =(20,) #一个元素，需要在元素后添加逗号


#Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#
# 基本功能是进行成员关系测试和删除重复元素。
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Baidu'}
# print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')

# print(a)
# print(a - b)     # a 和 b 的差集  a中有，而b中没有的
# print(a | b)     # a 和 b 的并集
# print(a & b)     # a 和 b 的交集
# print(a ^ b)     # a 和 b 中不同时存在的元素

#Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

#字典是python中另一个非常有用的内置数据类型
#列表是有序的对象集合，字典是无序的对象集合。两者的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
#字典是一种映射类型，字典用{}标识，它是一个无序的键值的结合。键必须使用不可变类型，在同一个字典中，键必须是唯一的

# dict={}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# print(dict)
#
# tinydict = {'name':'runnoob','code':1,'site':'www.runnoob.com'}
# print(tinydict)
# print(dict['one']) #输出键为’one‘的值
# print(dict[2])
# print(tinydict.keys())
# print(dict.keys())
# print(tinydict.values())
#字典是一种映射类型，它的元素是键值对
#字典的关键字必须为不可变类型，且不能重复

#总结：
# List 列表 内容写在[]中间
#  tuple 元组 内容写在（）里
# set 集合  内容写在{}里
# dictionary 字典 内容写在 {}

# a =100
# print(float(a)) #将x转化为一个浮点数
# print(complex(1,2)) #创建一个复数
# print(str(a))  # str()将对象x转化为字符串
# print(repr(a))

# list1 =['Google','Taobao']
# tuple1 = tuple(list1)  #将序列x转换成一个元组（元素值不能修改）
# print(tuple1)

#list()方法用于将元组或字符串转换为列表
# aTuple = (123,'Google','Runnoob','Taobao')
# list1 = list(aTuple)
# print(list1)
#
# str = "Hello World"
# list2 = list(str)  #list()可以将字符串转化为一个列表
# print("列表元素：",list2)

# x = set('runnoob')
# y = set('google')
# print(x) #{'r', 'b', 'u', 'n', 'o'} 创建一个无序不重复元素集合  重复的被删除

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5]
#
# if (a in list):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if (b not in list):
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
#
# # 修改变量 a 的值
# a = 2
# if (a in list):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")


# a = 20
# b = 20
#
# if (a is b):
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
#
# if (id(a) == id(b)):
#     print("2 - a 和 b 有相同的标识")
# else:
#     print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
# b = 30
# if (a is b):
#     print("3 - a 和 b 有相同的标识")
# else:
#     print("3 - a 和 b 没有相同的标识")
#
# if (a is not b):
#     #判断两个标识符是不是引用自不同对象，如果引用的不是同一个对象则返回结果为True
#     print("4 - a 和 b 没有相同的标识")
# else:
#     print("4 - a 和 b 有相同的标识")

#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等

# //用于向下取接近除数的整数

#python运算符  优先级顺序为NOT、AND、OR

# a = [1,4,5,8,9]
# print(id(a))
#
# a[:] = [0,9,10] #对a[:]赋新的值
# print(id(a))
# print(a)  #对a[:]赋值后查看a的地址，发现地址不变，原因是并没有分配新的内存地址，而是直接在原内存地址上修改
#
# a= [1,4]
# print(id(a))  #.对a赋值后查看a的地址，发现地址变了，原因是a为一个新的对象，所以分配了新的内存地址。

#python支持三种不同的数值类型
#整型、浮点型、复数

#数据类型转化：只需要将数据类型作为函数名即可
#int(x) 将x转换为一个整数
#float(x)将x转换到一个浮点数

# //得到的并不一定是整数类型的数，它与分母分子的数据类型有关系

#abs()返回数字的绝对值
# print ("abs(-40) : ", abs(-40))
# print ("abs(100.10) : ", abs(100.10))

# import math
# #ceil()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
# #ceil()函数返回一个大于或等于x的最小整数
# print ("math.ceil(-45.17) : ", math.ceil(-45.17))
# print ("math.ceil(100.12) : ", math.ceil(100.12))
# print ("math.ceil(100.72) : ", math.ceil(100.72))
# print ("math.ceil(math.pi) : ", math.ceil(math.pi))

import random

# print(random.choice(range(100)))  #从 range(100) 返回一个随机数
# print(random.choice([1,2,3,5,9]))  #从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素
# print(random.choice('Runoob'))  #从字符串中 'Runoob' 返回一个随机字符
# 从 1-100 中选取一个奇数
#randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
# print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# # 从 0-99 选取一个随机数
# print ("randrange(100) : ", random.randrange(100))

# var1 = 'Hello World'
# var2 = "Runnoob"
# print(var1+" "+var2)
# print(var1[2:5]) #python访问字符串，可以使用方括号[]来截取字符串

# print("random():",random.random()) #randow()返回随机生成的一个实数，它在[0,1)范围内
#
# random.seed()
# print ("使用默认种子生成随机数：", random.random())
# print ("使用默认种子生成随机数：", random.random())
#
# random.seed(10)
# print ("使用整数 10 种子生成随机数：", random.random())
# random.seed(10)
# print ("使用整数 10 种子生成随机数：", random.random())

#我们调用 random.random() 生成随机数时，每一次生成的数都是随机的
#但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。
#意思是：使用random.seed()之后，可以保证每次生成的随机数不变。

#shuffle()洗牌的意思。该方法是将序列的所有元素随机排序
# list = [20, 16, 10, 5];
# random.shuffle(list)
# print("随机排序列表 : ", list)
# random.shuffle(list)
# print("随机排序列表 : ", list)

#随机生成下一个实数，它在[x,y]范围内
# print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
# print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))

#!!!!!!注意：str[:6] 代表第6个字符之前的元素
# str[:3] 代表第3个字符之前的元素
# var1 = 'Hello World!'
# print(var1[:])
# # print("已更新字符串 : ", var1[:6] + 'Runoob!')
# var2 = "ABCDEFG"
# print(var2[:])

# \ 行尾 代表续行符
# print("line1 \
# line2 \
# line3")
# # \\ 反斜杠符号
# print("\\")
#
# print('\'')
#
# print("\"")

# print("\a")
# print("Hello \b World!")
# print("Hello\rWorld!")
# print('google runoob taobao\r123456')
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
# str = "[runoob]"

# print ("str.center(40, '*') : ", str.center(40, '*'))
# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
#
# print(str)
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
# print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
# print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
# Str='Runoob example....wow!!!'
# suffix='!!'
# print (Str.endswith(suffix))
# print (Str.endswith(suffix,20))
# suffix='run'
# print (Str.endswith(suffix))
# print (Str.endswith(suffix, 0, 19))

# str = "runoob\t12345\tabc"
# print('原始字符串:', str)
# print('使用 2 个空格替换 \\t 符号:', str.expandtabs(2))
# # 3 个空格
# print('使用 3 个空格:', str.expandtabs(3))
# str1 = "Runoob example....wow!!!"
# str2 = "exam";
# # str.find() 与 str.index()都是检测字符串中是否包含子字符串。
# #区别在与 srr.index()方法，没有找到子字符串时，会报异常
# print(str1.find(str2))
# print(str1.find(str2, 5))  #代表从下标5开始查找
# print(str1.find(str2, 10))
# str = "runoob"  # 字符串没有空格
# print(str.isalnum())
# # str.isalnum() 检测字符串中是否由字母和数字组成
# str = "www.runoob.com"
# print(str.isalnum())
# print(str.isalpha())  #检测字符串所有字符是否只由字母或者文字组成
# str = '2345f'
# print(str.isdigit())
# str.isdigit() 检测字符串是否只由数字组成
# str = 'abv'
# print(str.islower())
# str.islower()  lower()就代表小写
# str = "Runoob example....wow!!!"
#
# print (str.ljust(50, '*'))
# list = [1, 2, 3]
# for x in list:
#     print(x, end=" ")
# + 号用于组合列表
# test = [4,5,6]
# print(list+test)
# nest = (list,test) #将两个列表组合嵌套放在一个新的列表里
# # print(nest)
# # print(nest[1])
# print(len(test))
# print(min(list))
# list.append(3)
# print(list)
# print(list.count(3)) #统计某个元素在列表中出现的次数
# list.extend(test)  #用于在一个列表的末尾一次性追加另一个序列的多个值
# list.insert(2,8) #将指定对象插入列表
# list.remove(3) # 删除列表中某一个值的第一个匹配项
# list.reverse() # 用于将列表元素反向
# print(list)
# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
#
#
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# random.sort(key=takeSecond)
#
# # 输出类别
# print('排序列表：', random)
# list1 = list[:] #复制列表
# list2 = list.copy(); #复制列表
# print(list2)
# tup2 = (1, 2, 3, 4, 5 )
# tup3 = "a", "b", "c", "d"
# print(type(tup2))
#
# tup1 = ("50",)  #当元组中只包含一个元素时，需要在元素后面添加逗号, 否则括号会被当作运算符使用
# print(type(tup1))
# tup4 = tup1 + tup2 +tup3  #和列表一样，可以通过+将元组连接起来 组成新的元组
# print(tup4)
#元组的元素值是不允许删除的，但是我们可以使用del语句来删除整个元组
# for x in (1, 2, 3): print (x,)

#字典是另一种可变容器模型，且可存储任意类型对象
#值可以取任何数据类型，但键必须是不可变的，如字符串、数字
#键必须不可变，所以可以用数字，字符串或者元组充当，但是不可以用列表
# dict1 = { 'abc': 456 }
# dict2 = { 'abc': 123, 98.6: 37 }
# print(dict2)
# print(dict2['abc'])
# del dict2[98.6]
# print(dict2)
# del dict1

#
# dict = {'Name': 'Zara', 'Age': 7}
#
# print ("字典长度 : %d" %len(dict))
# dict.clear()
# print ("字典删除后长度 : %d" %  len(dict))
# seq = ('name', 'age', 'sex')
#
# dict = dict.fromkeys(seq) #dict.fromkeys()可以将元组转换成字典
# print(type(seq))
# print("新的字典为 : %s" % str(dict))
# dict = {'Name': 'Runoob', 'Age': 7}
# if 'Age' in dict:
#     print("键Age存在")
# else:
#     print("键Age不存在")

#
# dict = {'Name': 'Runoob', 'Age': 7}
# for i,j in dict.items():
#     print(i, ":\t", j)
#
# d={1:"a",2:"b",3:"c"}
# result=[]
# for k,v in d.items():
#     result.append(k)
#     result.append(v)
#
# print(result)

# dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
# keys = dishes.keys();
# # for i in keys:
# #     print(i)
#
# print(list(keys))

# dict.setdefault(key,default=None)  #如果key在字典中，返回对应的值，如果不在，则插入key,并设置默认值default.
# dict = {'Name': 'Runoob', 'Age': 7}
# dict2 = {'Sex': 'female'}
#
# dict.update(dict2) #将一个字典参数更新到dict中，
# print("更新字典 dict : ", dict)

# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.pop('name') #删除指定键值，并返回被删除的值。
# print(pop_obj)

# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.popitem()  #删除最后一个键值对，并且返回出来
# print(pop_obj)
# print(site)

#set集合是一个无序的不重复元素序列，可以使用{}或者set()函数创建集合，注意：创建一个空集合必须是set()，因为{}被用来创建一个空字典
#创建空集合
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('apple' in basket) #用in 快速判断元素是否在集合内
#
# a = set('abracadabra') #会把重复的元素去掉
# b = set('alacazam')
# print(a - b)   #集合a中包含而集合b中不包含的元素
# print(a|b) #集合a或b中包含的所有元素
# print(a & b)  ## 集合a和b中都包含了的元素
# print(a^b) #不同时包含于a和b的元素


# 注意：用set()创建集合时，是两个括号，里面是单个元素。
# thisset = set(("Google", "Runoob", "Taobao"))
# # dict = {'Google','Runoob','Taobao'}
# # print(thisset)
# print(dict)
# thisset.add("Facebook")
# thisset.update({1,3})  #利用update() 添加字典
# thisset.update([1,4],[5,6])  #利用update()添加 列表
# # thisset.discard(1)
# # thisset.remove(3)
# thisset.pop()  #s.pop()方法随机删除集合中的一个元素
# print(thisset)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# z = x.difference(y) # 在x集合中  但是不再y集合内
# print(z)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)  #和上边的different的区别是 前者返回元素到一个新集合。  但是后边这个 是直接在原来集合中移除元素，没有返回值
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
# z = x.intersection(y)  # 返回一个新集合，该集合的元素既包含在集合x又包含在集合y中
# print(z)


#python编程第一步
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b

# i = 256*256
# print('i的值为：',i)
#
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b


# python 中用elif代替了else if,所以if语句的关键字为 ： if - elif -else
# 每个条件后面要使用冒号：
#在python中 没有switch - case语句

# a = 1
# while a < 7:
#     if(a % 2 == 0):
#         print(a,'is even')
#     else:
#         print(a,'is odd')
#     a+=1

# age = int(input("请输入你家狗狗的年龄："))
# str1 = str(input("请输入你家狗狗的年龄："))
# print("")
# if age <= 0:
#     print("你是在逗我吧！")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 2:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age-2)*5
#     print("对应人类年龄:",human)
#
# input("点击enter键退出")
# input("lyy好好学习呀")

# print(5 == 6)


# number = 7
# guess = -1
# print("数字猜谜游戏！")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了……")
#     elif guess > number:
#         print("猜的数字大了……")

# num = int(input("请输入一个数字："))
# if num%2 == 0:
#     if num%3==0:
#         print("你输入的数字可以整除 2 和 3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")


#while 循环注意要有冒号和缩进。另外在python中没有do while循环

# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter +=1
# print("1到%d之和为：%d" %(n,sum))


# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")

# list = [1,2,3,4]
# it = iter(list)  #创建迭代器对象
# # print(next(it))
# # print(next(it))
# # print(next(it))
# for x in it:
#     print(x,end=",") #输出迭代器的下一个元素

# import sys
#
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#在python中，类型属于对象，变量是没有类型的
# a=[1,2,3]
# print(type(a))
# b = "Runoob"
# print(type(b))

# a = 1
# print(id(a))
#
# a = 19
# print(id(a))

# 可写函数说明
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 函数参数的使用不需要使用指定顺序
# # 调用printinfo函数
# printinfo(age=50, name="runoob")


# 可写函数说明
# 加了*号的参数会以元组tuple的形式导入，存放所有未命名的变量参数
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)

# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)  # 第一个参数作为arg1  其余后面的参数作为元组元素进入  vartuple参数


# 可写函数说明
#参数加了两个**的参数会以字典的形式导入
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

# print(math.pi)

# from math import  pi
# print(pi)

#python 中的列表是可以变的，列表可以修改，而字符串和元组不能

# __name__属性：
#一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')

# 每个模块都有一个__name__属性，当其值‘__main__’时，表明该模块自身在运行，否则是被引入
# 说明： __name__ 与__main__底下是双下划线
#dir()函数，内置的函数dir()可以找到模块内定义的所有名称。以一个字符串列表的形式返回。
#如果没有给定参数，那么dir()函数会罗列出当前定义的所有名称：


#range(1,11)创建一个整数列表，一般用在for循环中
#这句话的意思是 从1-10。不包含11
#str.rjust(width[, fillchar])  返回一个原字符串右对齐，并使用空格填充至长度windth的新字符串
#rjust()方法可以将字符串靠右，并在左边填充空格
# for x in range(1,11):
#     print(repr(x).rjust(2,'^'),repr(x*x).rjust(3,'@'),end=' ')
#     print(repr(x*x*x).rjust(4,'*'))


#这里面：{0:2d} 表示第一个参数x的格式。0 代表x,:2d 表示两个宽度的10进制数显示。
#{1:3d} 表示第一个参数x*x的格式。1 代表x*x,:3d 表示三个宽度的10进制数显示。
#{2:4d} 表示第一个参数x*x*x的格式。2代表x*x*x,:4d 表示四个宽度的10进制数显示。

# for x in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

#format格式化函数
#"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

import math
# print('常量 PI 的值近似为： {}。'.format(math.pi))
# print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, number))

#input函数用来输入控制台信息
# str = input("请输入：");
# print ("你输入的内容是: ", str)

# f = open("/tmp/foo.txt", "w")

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# #实例化类
# t = Test()
# t.prt()

#类方法必须包含参数self，self代表的是类的实例，代表当前对象的地址。self.calss则指向类。
# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = 0
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
# # 实例化类
# p = people('runoob', 10, 30)
# p.speak()

#类的继承： class DerivedClassName(BaseClassName)
# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# #多继承
# # class DerivedClassName(Base1,Base2,Base3):
#
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫%s,我是一个演说家，我演讲的主题是%s"%(self.name,self.topic))
#          "字符串"  %   变量
#
# #多重继承
# class sample(speaker,student):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
#
#
# test = sample("Tim",25,80,4,"Python")
# #方法名相同，默认调用的是在括号中排前地父类的方法
# test.speak()

#super()函数是用于调用父类（超类）的一个方法

#__private_attrs：两个下划线开头，声明该属性为私有
#在类的内部，使用def关键字来定义一个方法，类方法必须包含参数self，且为第一个参数，self代表的是类的实例。
#self的名字不是规定死的，也可以使用this
#__private_method：两个下划线开头，声明该方法为私有方法

#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了


#下面这个例子：要么声明为全局变量；要么就通过参数传递

a = 10
def test():
    #声明为全局变量
    global a
    a = a + 1
    print(a)
test()


a = 10
#直接进行参数传递
def test(a):
    a = a + 1
    print(a)
test(a)












