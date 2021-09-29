
#定义一个列表，并计算列表元素之和

# total = 0
#
# list1 =  [11, 5, 17, 18, 23]
#
# for ele in range(0,len(list1)):
#     total = total + list1[ele]
#
# print('列表元素之和为：',total)

# total = 0
# ele = 0
#
list1 = [11, 5, 17, 18, 23]
#
# while(ele < len(list1)):
#     total = total + list1[ele]
#     ele +=1
# print('列表元素之和为：',total)

def sumOfList(list,size):
    if(size == 0):
        return 0
    else:
        return list[size-1]+sumOfList(list,size-1)

total = sumOfList(list1,len(list1))
print('列表元素之和为：',total)

#总结 ：求列表中元素的和
#1、for循环列表，累积求和
#2、while循环，找到
#3、使用递归进行累积相加