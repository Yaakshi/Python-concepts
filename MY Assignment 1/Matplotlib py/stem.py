import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"]=[8,4]
plt.rcParams["figure.autolayout"]=True

x=np.linspace(0.1,2*np.pi,30)
y=np.exp(np.sin(x))

markerline,stemline,baseline=plt.stem(x,y,linefmt='pink',markerfmt='*',bottom=1.1)
markerline.set_markerfacecolor('yellow')

plt.show()