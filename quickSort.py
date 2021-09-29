
#快速排序：
# 使用分治法策略来把一个序列分为大小两个子序列，然后递归地排序两个子序列
# 步骤为：
# 1、挑选基准值：从数列中挑出一个元素，称为‘基准’
# 2、分割：重新排序数列，所有比基准值小的放在基准前面，比基准大的放在基准后面
# 3、递归排序子序列

def partition(arr,low,high):
    i = (low-1)
    #代表最后一个元素
    pivot = arr[high]
    print('pivot:',pivot)

    for j in range(low,high):
        print('arr[j]:',arr[j])
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

#快速排序，递归
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("排序后的数组:")
for i in range(n):
    print ("%d" %arr[i]),