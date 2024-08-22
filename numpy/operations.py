import numpy as np
a=np.array([1,2,5,3])
print("add 1 to every element:",a+1)
print("subtracting 3 from each element:",a-3)
print("multiplying each element by 10:",a*10)
print("squaring each element",a**2)

a*=2
print("doubled each element of original array:",a)

a=np.array([[1,2,3],[3,4,5],[9,6,0]])

print("traanspose of array:",a.T)