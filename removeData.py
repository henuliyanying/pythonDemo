
#python移除字符串中的指定位置字符

test_str = 'Runnoob'

#输出原始字符串
print('原始字符串为：'+test_str)

#移除第三个字符
new_str = ''

for i in range(0,len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print('字符串移除后为:'+new_str)