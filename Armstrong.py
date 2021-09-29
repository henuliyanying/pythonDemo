
#阿姆斯特朗数：
# 如果一个n位正整数等于其各位数字的n次方之和，则称该数为阿姆斯特朗数。
#例如1^3 + 5^3 + 3^3 = 153。
#1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

# 获取用户输入的数字
num = int(input("请输入一个数字: "))

# 初始化变量 sum
sum = 0
# 指数
#将参数转化成字符串类型，并计算长度
n = len(str(num))

#检测
temp = num
while temp > 0:
    #取余数
    digit = temp % 10
    sum += digit ** n
    temp //= 10

#输出结果
if num == sum:
    print(num,'是阿姆斯特朗')
else:
    print(num,'不是阿姆斯特朗')

# 总结：得到一个数字各个位上的数字
# 1、先对10取余
# 2、再除以10 取整
# 3、可以得到每一位的数字