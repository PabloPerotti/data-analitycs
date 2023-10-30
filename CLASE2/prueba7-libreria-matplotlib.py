import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 2*3.14, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)   # 2 filas, 1 columna, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(2, 1, 2)   # 2 filas, 1 columna, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('Ejemplo 1:\n')
plt.show()


# Una vez que usamos plt.show() el gráfico se muestra y podemos crear uno nuevo:


plt.subplot(1, 2, 1)   # 1 fila, 2 columnas, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(1, 2, 2)   # 1 fila, 2 columnas, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('\nEjemplo 2:\n')
plt.show()