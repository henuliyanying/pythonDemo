
# def Reverse(lst):
#     lst.reverse()
#     return lst
#
# lst = [10,11,12,13,14,15]
# print(Reverse(lst))

#总结
#1、list翻转 用reverse()方法
#2、

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#总结：
#1、lst[::-1] 代表start为1，end为list.size  默认为1。步长为-1时，返回倒序原序列
#2、翻转有两种写法。reverse()和list[::-1]