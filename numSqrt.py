
#对用户输入的数字，计算它的平方根

# num = float(input("请输入一个数字："))
# num_sqrt = num ** 0.5
# #每一个变量前面加上百分号。0.3f 代表小数点后有三位数
# print('%0.3f的平方根为%0.3f'%(num,num_sqrt))


#下面是求复数或者负数的平方根
import cmath
num = int(input("请输入一个数字："))
num_sqrt = cmath.sqrt(num)
# {1:0.3f}  1 代表：格式化输出第一个字符； 0.3f代表：保留小数点3位数字
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))