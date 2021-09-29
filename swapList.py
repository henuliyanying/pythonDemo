
# def swapList(newList):
#     newList[0],newList[-1] = newList[-1],newList[0]
#     return newList
#
# newList = [1,2,3]
# print(swapList(newList))

#对调指定两个元素

# def swapPositions(list,pos1,pos2):
#     print('pos2：',pos2)
#     list[pos1],list[pos2] = list[pos2],list[pos1]
#     return list
#
# List = [23,65,19,90]
# pos1,pos2 = 1,3
#
# print(swapPositions(List,pos1-1,pos2-1))

def swapPositions(list, pos1, pos2):
    print('pos1:', pos1)
    first_ele = list.pop(pos1)
    #pos2 - 1  这里还要再减1的原因是：上面删除一个元素之和，寻找值的下标就要再减1
    print('pos2 - 1:',pos2 - 1)
    second_ele = list.pop(pos2 - 1)
    print('second_ele:',second_ele)

    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))