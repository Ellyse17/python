import time
import numpy as np
import matplotlib.pyplot as plt
def linersearch(arr,x):
    i=0
    while i<len(arr):
        if arr[i]==x:
            returni
            i=i+1
            return-1
times=list()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("enter the no of elements"))
    numtimes.append(n)
    for x in  range(n):
        number=np.random.randint(10,99)
        arr.append(number)
    print("list before searching",x+1,"element")
    print(arr)
    linersearch (arr,x)
    end=time.time()