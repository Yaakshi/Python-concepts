from ast import Str
import numpy as np

a = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]])

print (np.sort(a, axis = None)) #sort array
print (np.sort(a, axis = 1))    #sort row wise
print (np.sort(a, axis = 0, kind = 'mergesort'))


valuetypes = [('name', Str), ('grad_year', int), ('cgpa', float)]
values = [('Avan', 2024, 8.5), ('Tej', 2024, 8.7),
           ('Sach', 2024, 8.9), ('Sand', 2024, 9.0)]
arr = np.array(values, dtype = valuetypes)

print (np.sort(arr, order = 'name'))
print(np.sort(arr,order=['grad_year','cgpa']))

