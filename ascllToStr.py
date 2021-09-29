# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

print(c + " 的ASCII 码为", ord(c))
print(a, " 对应的字符为", chr(a))

# 总结
# 1、python中有ASCLL和字符串相互转换的函数
# 2、ord() 将字符串转换为ASCLL码
# 3、chr()  将ASCLL码转换为字符串