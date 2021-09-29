
#输出指定范围的素数

minNum = int(input("请输入区间的最小值："))
maxNum = int(input('请输入区间的最大值：'))

#双重循环
for num in range(minNum,maxNum+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)

