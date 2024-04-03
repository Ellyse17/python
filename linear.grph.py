import time
import numpy as np
import matplotlib.pyplot as plt

def linear_search(a,x):
    for i in range(0,len(a)):
        if a[i]==x:
            print("Search is successful at posible",i)
            return
    print("Search is successful")
#main program
    
elements=np.array([i*1000 for i in range(1,40)])
plt.xlabel("List Length")
plt.ylabel("Time Complexity")                                                                                                      
times=list()
for i in range(1,40):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    linear_search(a,1)
    end=time.time()
    times.append(end-start)
    print("Time taken for linear search in",i*1000,"elements is",end-start,"s")
plt.plot(elements,times,label="linear search")
plt.grid()
plt.legend()
plt.show()
