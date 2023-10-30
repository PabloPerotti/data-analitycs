import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*3.14, 0.1)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "b-", label="seno")
plt.plot(x, y2, "r-", label="coseno")
plt.legend()  #le decimos a matplotlib que muestre todos los labels
plt.show()

