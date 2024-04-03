def BubbleSort(array):
    n = len(array) - 1
    while n >=1:
        i = 0
        while i < n:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            i = i+1
        n = n - 1
array1 = [9,2,1,3,4,5,6,7,345,5,434,234,234234,34,34,34,42,434,34,34,343,4234,34,4,23423,43,4234,423,423,4234,234,234,4,4,445,3123,5,45,45,4,545,5,45,45,45,4534,545,5,45,45,8]
BubbleSort(array1)
print(array1)
            