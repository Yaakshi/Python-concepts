import numpy as np

a=np.array([[1,2,3],[4,5,6]],dtype=float)
b=np.array((9,8,7))
c=np.zeros((3,2))
d=np.full((4,4),5,dtype=complex)
e=np.random.random((2,2))
f=np.arange(0,30,5) #returns evenly spaced values 
                    #within a given interval. step size is specified.

g=np.linspace(0,5,10) #returns evenly spaced values within
                      #a given interval. num no. of elements are returned.
arr=np.array([[1, 2, 3, 4],[5, 2, 4, 2], [1, 2, 0, 1]])
newarr=arr.reshape(2,2,3)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()   #to get a copy of 
                        #array collapsed into one dimension.

print('a: ',a)
print('\nb: ',b)
print('\nc: ',c)
print('\nd: ',d)
print('\ne: ',e)
print('\nf: ',f)
print('\ng: ',g)

print('\narr: ',arr)
print('\nnewarr: ',newarr)

print('\narr2: ',arr2)
print('\nflarr: ',flarr)