import numpy as np
aee_2d=np.array([[1,2,3],[4,5,6]])
print(aee_2d)
print(aee_2d.shape)
print(aee_2d.ndim)
print(aee_2d.size)
print(aee_2d.dtype)

arr=np.array([1,2,3.3])  #convert to int from float
int_arr=arr.astype(int)
print(int_arr)
