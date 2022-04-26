#BUBBLE SORT
arr=[4,5,66,1,3,5,2,6,5]
n = len(arr)
print('Unsorted List:\n')
print(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print('Sorted Array:\n')
print(arr)


#SELECTION SORT
array=[5,7,3,4,6,44,2,4,4]
size=len(array)
print('Unsorted List:\n')
print(array)
for s in range(size):
        min_idx = s   
        for i in range(s + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[s], array[min_idx]) = (array[min_idx], array[s]) 
print('Sorted List:\n')
print(array)