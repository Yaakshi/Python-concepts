from cProfile import label
import matplotlib
import matplotlib.pyplot as plt

x1=[3,5,4]
y1=[0,9,1]

x2=[-9,3,-7]
y2=[-3,-4,0]

plt.plot(x1,y1,label='line1')
plt.plot(x2,y2,label='line2')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Two lines graph')

plt.legend()
plt.show()