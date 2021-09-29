
#python判断字符串是否存在子字符串

def check(string,sub_str):
    if (string.find(sub_str) == -1):
        print('不存在')
    else:
        print(string.find(sub_str))
        print('存在')

string = "www.runoob.com"
sub_str ="runoob"
check(string, sub_str)

# 总结：判断字符串是否存在子字符串
# 1、string.find() 值如果等于-1，代表指定字符串中不存在子字符串
# 2、如果存在，则返回指定字符串第一次出现的下标。