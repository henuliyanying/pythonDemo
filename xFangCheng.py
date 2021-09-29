
#以下为 通过用户输入数字，并计算二次方程

# 二次方程 ax**2 + bx +c =0
# a b c为用户提供，为实数， a 不为0

# cmath(成为复杂数学模块)
import cmath

a = float(input('输入a: '))
b = float(input('输入b: '))
c = float(input('输入c: '))

#计算
d = (b**2) - (4*a*c)

#两个解：
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为{0} 和 {1}'.format(sol1,sol2))

# 总结：
# 1、input()接收的用户输入的参数是 字符串；
# 2、平方根计算时：最好用cmath.sqrt()包下的方法，适用于 负数、复数、正数
# 3、str.format()方法，''.format()  变量可以使用序号进行标注出来
