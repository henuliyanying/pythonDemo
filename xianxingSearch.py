
#线性查找指按一定的顺序检查数组中的每一个元素，直到找到所要寻找的特定值为止

def search(arr,n,x):
    for i in range(0,n):
        if (arr[i] == x):
            return i;
    return -1

arr = ['A','B','C','D','E']
x = 'D'
n = len(arr)

result = search(arr,n,x)
if(result == -1):
    print('元素不在数组中')
else:
    print('元素在数组中的索引为',result);