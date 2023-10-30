# Mini desafío 1
# Gráficar en el intervalo de [-1, 1] la función valor absoluto. Elegir una cantidad 
# apropiada de puntos de acuerdo a su criterio.

# Tip: Usar la funcion np.absolute de numpy.

import numpy as np
import matplotlib.pyplot as plt

n = 101

X = np.linspace(-1, 1, n)
Y = np.absolute(X)

plt.plot(X, Y)
plt.show()