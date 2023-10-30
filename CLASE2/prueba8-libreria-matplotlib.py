# Veamos algunas cosas más que pueden realizarse:

# Con plt.figure( figsize = (w, h) ) podemos elegir el tamaño de la figura.
# Con plt.subplots(nrows, ncols) podemos crear un conjunto de subplots para ser usados más adelante.
# Con plt.xlabel('xlabel') y plt.ylabel('ylabel') podemos ponerle nombre a los ejes.
# Con plt.axis([xmin, xmax, ymin, ymax]) podemos elegir los límites de los ejes.
# Con plt.title('title') podemos mostrar un título sobre el gráfico.
# Con plt.grid() pueden activar una grilla cuadriculada.
# Se pueden configurar muchísimos más parámetros, por lo cual les mostrarmos únicamente los que se suelen
# usar más regularmente. Si necesitan funcionalidades más específicas, puedan encontrarlas en la documentación 
# de matplotlib.pyplot.



import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0, 2*3.14, 0.3)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12, 4))  # Configuramos el tamaño del gráfico (en pulgadas)

plt.subplot(1, 2, 1)
plt.title("Gráfico azul")
plt.plot(x, y1, 'bo')        # Graficamos la función y1
plt.xlabel('Tiempo')
plt.ylabel('Corriente')

plt.subplot(1, 2, 2)
plt.title("Gráfico rojo")
plt.plot(x, y2, 'r-.')       # Graficamos la función y2
plt.xlabel('Tiempo')
plt.axis([0, 3, -1, 1])      # Elegimos los límites de los ejes
plt.grid(True)               # Activamos la grilla

plt.show()