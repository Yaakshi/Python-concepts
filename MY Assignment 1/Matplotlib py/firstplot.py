import matplotlib
import matplotlib.pyplot as plt

x=[0,4,6]
y=[9,-5,7]

plt.plot(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('First plot')

print(matplotlib.__version__)

plt.show()