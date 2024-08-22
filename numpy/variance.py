import numpy as np

arr = [20, 2, 7, 1, 34]  
  
print("arr:",arr)  
print("var of arr:",np.var(arr))

print("var of arr:",np.var(arr,dtype=np.float32))  
print("var of arr:",np.var(arr,dtype=np.float64))

arr2 = [[2, 2, 2, 2, 2],  
    [15, 6, 27, 8, 2],  
    [23, 2, 54, 1, 2, ],  
    [11, 44, 34, 7, 2]]
# can only be done for >1D
print("var of arr,axis=0:",np.var(arr2,axis=0))  
print("var of arr,axis=1:",np.var(arr2,axis=1)) 