#utilizando la libreria math

# import matplotlib.pyplot as plt
# import math

# def f(x):
#   return math.sin( 2 * math.pi * x )

# n = 50  # Cantidad de puntos

# X = [ x/(n-1) for x in range(n) ] 
# Y = [ f(x) for x in X ]

# plt.plot(X, Y)    # plt.plot recibe 2 listas de igual longitud, la primera para el eje X, la segunda para el eje Y
# plt.show()        # Luego de generar el gráfico, lo mostramos

#utilizando la libreria numpy
# El código puede ser simplificado incluso más mediante el uso de Numpy.
# Numpy ofrece nuevos tipos de variables que permiten generar expresiones vectorizadas. De esta 
# forma podremos crear un vector 𝑥 con todas las coordenadas y aplicar la función  𝑠𝑖𝑛  a todo el 
# vector en simultáneo. Lo que va a sucede es que la función se aplica a cada elemento por separado.
# Asimismo, puedo multiplicar un vector por una constante, sumar una constante a cada componente,
# multiplicar dos vectores de forma matricial o escalar, sumar dos vectores, y muchas cosas más.
# Las operaciones que se realizan elemento a elemento son de mucha utilidad, pueden llegar a 
# encontrarlas bajo el nombre element-wise operations.
# Veamos dos alternativas para crear vectores equiespaciados: np.arange(start, stop, step) y 
# np.linspace(start, stop, num):

import numpy as np
# Creamos un arreglo que empieza en 0, llega hasta 1.1 (no inclusivo)
# con incrementos de 0.1 unidades
t1 = np.arange(0, 1.1, 0.1)  
# Creamos un arreglo que empieza en 0, termina en 1 (inclusivo)
# y tiene 11 elementos, es decir, incrementos de 0.1 unidades.
t2 = np.linspace(0, 1, 11)   
print(t1)
print(t2)
# Con np.arange() debemos indicar el salto entre un elemento y otro, mientras que con 
# np.linspace() tenemos que indicar la cantidad total de elementos. Además np.arange() no
# incluye el valor de stop en el vector mientras que np.linspace() sí.


import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 100

X = np.linspace(0, 1, n)
# print('X =\n', X,'\n')

# Se calcula la función sobre cada elemento por separado
Y = np.sin( 2 * np.pi * X )
# print('Y =\n', Y,'\n')

plt.plot(X, Y)
plt.show()