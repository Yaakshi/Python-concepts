import matplotlib.pyplot as plt

x = [1,4,5,7,2,3,5,8,9,0,0]
y = [2,1,4,8,5,6,0,3,9,2,0]

plt.scatter(x, y, label= "points", color= "red",marker= "o", s=30)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My scatter plot!')

plt.legend()

plt.show()

