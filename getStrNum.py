
#给定一个字符串，然后判断该字符串的长度

# str = 'runoob'
# print(len(str))

def findLen(str):
    counter = 0
    # str[counter:]代表第counter+1后的所有元素
    while str[counter:]:
        print('str[counter:] ',str[counter:],counter)
        counter += 1
    return counter

str = "runoob"
print(findLen(str))
