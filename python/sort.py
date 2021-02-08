arr = [2,5,3,6,1,2,3,5,7]
arr2 = [1,2,3,4,1,2,5,1,2,3,1,6,8,2,1]

def insertSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while temp < array[j] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = temp
        
insertSort(arr)
print(arr)
insertSort(arr2)
print(arr2)


print(arr[0:4])

print(arr[4:])

arr3 = [2,1,4,2,3,5,1]
# 2 1 4 -> 2 / 1 4 
            # -> 1 / 4
# 2 3 5 1

def mergeSort(array,array2):
    if len(array) > 1:
        index = len(array) // 2
        mergeSort(array[:index])
        mergeSort(array[index:])
