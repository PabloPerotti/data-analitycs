import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 2*3.14, 0.25)

plt.plot(x, np.sin(x), "m*")
plt.plot(x, np.cos(x), "r--")

plt.show()