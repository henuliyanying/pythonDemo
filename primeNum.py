
# 质数 ： 一个大于1的自然数，除了1和它本身外，不能被其他自然数整除，换句话就是活 该数除了1和它本身以外不再有其他的因数
# 整数b除以非零整数a，商为整数，且余数为零， 我们就说b能被a整除（或说a能整除b

num = int(input('请输入一个数字：'))

if num > 1:
    #range()创建一个整数列表，一般用在for循环中
    #包括左边这个值，但是不包括右区间的值
    for i in range(2,num):
        if(num % i) == 0:
            print(num,'不是质数')
            print(i,'乘于',num//i,'是',num)
            break
    else:
        print(num,'是质数')
else:
    print(num,'不是质数')