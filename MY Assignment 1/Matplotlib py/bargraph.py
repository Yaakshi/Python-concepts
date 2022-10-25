import matplotlib.pyplot as plt

x=[1,2,3]
y=[9,8,7]

names=['1','2','3']

plt.bar(x,y,tick_label=names,width=0.3,color=['black','pink'])

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Bar graph')

plt.show()