import numpy as np

arr=np.random.randn(4)      #randn=> of specified shape with
print(arr)                  #values between 0 and 1
print()

arr=np.random.randint(1,9,size=(3,3))  #randint
print(arr)
print()

arr=np.random.randn(2,3,5)
print(arr)
print()

arr=np.random.randn(4,3,2,1)
print(arr)

