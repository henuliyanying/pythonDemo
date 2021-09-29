
#求数组元素之和
def _sun(arr,n):
    #使用内置的sum函数计算
    return(sum(arr))

#调用函数
arr = []
#数组元素
arr = [12,3,4,15]

#计算数组元素的长度
n = len(arr)

ans = _sun(arr,n)
print('数组元素之和为',ans)

#总结
# 1、Python的数组分三种类型：
# (1) list 普通的链表，初始化后可以通过特定方法动态增加元素。
# 定义方式：arr = [元素]
#
# (2) Tuple 固定的数组，一旦定义后，其元素个数是不能再改变的。
# 定义方式：arr = (元素)
#
# (2) Dictionary 词典类型， 即是Hash数组。
# 定义方式：arr = {元素k:v}