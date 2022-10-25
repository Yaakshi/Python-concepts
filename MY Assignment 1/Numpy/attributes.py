import numpy as np

arr=np.array([[1,2,3],[9,8,7]])

print(arr)
print("array type: ",type(arr))
print('no of axes: ',arr.ndim)
print("array shape: ",arr.shape)
print('array size: ',arr.size)
print('array datatype: ',arr.dtype)
print()


arr2=np.array([[1, 5, 6],[4, 7, 2],[3, 1, 9]])

print(arr2)
print(arr2.max())
print(arr.max(axis=1))  #row wise max elements
print(arr.min(axis=0))  #col wise min elements
print(arr.sum())    #sum of all array elements
print(arr.cumsum(axis=1))   #cumulative sum of each row

