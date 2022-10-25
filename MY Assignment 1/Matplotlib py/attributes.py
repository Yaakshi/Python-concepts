from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[4,3,2,1]

plt.plot(x,y, color='orange',linestyle='dashed',linewidth=5,marker='o',markerfacecolor='black',markersize=9)

plt.xlim(1,10)
plt.ylim(1,10)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Customized plot')

plt.show()