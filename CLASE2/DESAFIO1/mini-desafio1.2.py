import numpy as np
import matplotlib.pyplot as plt

n = 100

X = np.linspace(-5, 5, n)
gaussiana = np.exp(-X**2/2)

plt.plot(X, gaussiana)
plt.show()
