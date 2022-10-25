import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

np.random.seed(1)
x = np.random.randn(2000)
y = 1.2 * x + np.random.randn(2000) / 6

fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)

ax.set(xlim=(-2, 2), ylim=(-4, 4))

plt.show()


