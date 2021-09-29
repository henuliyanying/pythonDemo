
#定义一个列表，并计算某个元素在列表中出现的次数

# def countX(lst,x):
#     count = 0
#     for i in lst:
#         if(i == x):
#             count = count +1
#     return count
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# print(countX(lst, x))

def countX(lst,x):
    return lst.count(x)

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

#总结：计算一个元素在一个列表中出现的个数
# 1、采用for循环，判断每个元素是否等于指定元素
# 2、直接使用python的内置函数count()

