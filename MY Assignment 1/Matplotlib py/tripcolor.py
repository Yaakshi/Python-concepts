import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

np.random.seed(1)
x = np.random.uniform(-2, 2, 180)
y = np.random.uniform(-2, 2, 180)
z = (1 - x/3 + x**8 + y**5) * np.exp(-x**4 - y**4)

fig, ax = plt.subplots()

ax.plot(x, y, 'o', markersize=2, color='grey')
ax.tripcolor(x, y, z)

ax.set(xlim=(-3, 3), ylim=(-3, 3))

plt.show()

