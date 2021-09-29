
#定义一个列表，并将该列表元素复制到另外一个列表上

# def clone_runoob(li1):
#     li_copy = li1[:]
#     return li_copy
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = clone_runoob(li1)
# print("原始列表:", li1)
# print("复制后列表:", li2)

#总结：复制列表方法
#1、  代表复制li1[:]
#2、  定义一个列表，然后.extend()
#3、  使用list()方法

# def clone_runoob(li1):
#     # 先定义一个列表
#     li_copy = []
#     li_copy.extend(li1)
#     return li_copy
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = clone_runoob(li1)
# print("原始列表:", li1)
# print("复制后列表:", li2)

def clone_runoob(li1):
    # list()函数是python的内置函数，它可以将任何可迭代数据转换为列表类型，并返回转换后的列表
    li_copy = list(li1)
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)
