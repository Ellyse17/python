def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] <arr[min_index]:
               min_index = j
        arr[i],arr[min_index] =arr[min_index],arr[i]
        return arr
arr =[1,22,2,2,33,3,4,5,5,45,6,66,6,456,46,6,]
sorted_arr = selection_sort(arr)
print("Sorted array is:",sorted_arr)