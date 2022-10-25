import numpy as np

arr = np.array([[-1, 2, 0, 4],[4, -0.5, 6, 0],
                [2.6, 0, 7, 8],[3, -7, 4, 2.0]])

temp1=arr[:2,::2] #Array with first 2 rows and alternate
                    #columns(0 and 2)

cond = arr > 0 # cond is a boolean array
temp2 = arr[cond]

print('temp1: ',temp1)
print('temp2: ',temp2)