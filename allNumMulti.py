
#定义一个列表，并计算列表元素之乘积

def multiplyList(mylist):
    #注意：当求累计乘积时，初始值要设为1，而不是0
    result = 1
    for x in mylist:
        result = result * x
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
