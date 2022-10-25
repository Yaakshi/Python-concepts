import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

np.random.seed(1)
x = np.linspace(0, 8, 16)
y1 = 5 + 8*x/3 + np.random.uniform(0.0, 0.5, len(x))
y2 = 3 + 4*x/3 + np.random.uniform(0.0, 0.5, len(x))

fig, ax = plt.subplots()

ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


