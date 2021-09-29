
# test_list = [1,6,3,5,4]
#
# print('查看4是否在列表中（使用循环）')
#
# # for i in test_list:
# #     if i == 4:
# #         print('存在')
#
# if (4 in test_list):
#     print('存在')

# 判断元素是否在列表中共有两个方法
# 1、 x in list: 使用in 关键字
# 2、使用循环


# 初始化列表
test_list_set = [1, 6, 3, 5, 3, 4]
test_list_bisect = [1, 6, 3, 5, 3, 4]

print("查看 4 是否在列表中 ( 使用 set() + in) : ")

#set()方法的特点：无序性、确定性、不重复性
test_list_set = set(test_list_set)
print(test_list_set)
if 4 in test_list_set:
    print("存在")

print("查看 4 是否在列表中 ( 使用 count()) : ")
#count()统计字符串中，指定字符出现的次数
if test_list_bisect.count(4) > 0:
    print("存在")

test_list_bisect.clear()
print('清空列表：',test_list_bisect)