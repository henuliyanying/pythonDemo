

#复习判断谁是否为闰年的思路：
# 1) 能够被4整除但不能被100整除。
# 2) 能够被400整除。
year = int(input('请输入一个年份:'))
if year % 4 == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            #能够被400整除。
            print("{0}是闰年".format(year))
        else:
            print('{0}不是闰年'.format(year))
    else:
        #能被4整除但不能被100整除
        print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))