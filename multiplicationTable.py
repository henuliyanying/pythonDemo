
# 九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end='')
    #执行完一个数之后，要换行
    print()
