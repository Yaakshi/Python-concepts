from re import X    #That re. X flag stands for verbose. This flag allows more flexibility
                    #and better formatting when writing more complex regex patterns between the parentheses 
                    #of the match() , search() , or other regex methods. You can specify this flag using two ways.
import numpy as np

a = np.array([1, 2, 3, 4])

print(a+1)
print(a-3)
print(a*5)
print(a**3)
print(a)
print()

b = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print(b)
print()
print(b.T)  #transpose of 'b'

x = np.array([[1, 2],
            [3, 4]])
y = np.array([[4, 3],
            [2, 1]])
print()
print(x+y)
print(x*y)  #element wise multiplication
print(x.dot(y)) #matrix multiplication

