import numpy as np

A=np.arange(15,24).reshape(3,3)
B=np.arange(20,29).reshape(3,3)
print(A)
print(B)
result=A.dot(B)
print("Result:",result)
