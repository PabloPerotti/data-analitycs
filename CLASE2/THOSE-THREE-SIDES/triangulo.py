# Those three sides
# Escribir una función que dibuje un triángulo equilatero, debe recibir 3 parametros:
# X,Y: coordenadas del centro
# L: Largo de los lados

import numpy as np
import matplotlib.pyplot as plt

# def plotTriangle(x, y, L):
#     height = np.sqrt(3)*L/2
#     apothem = height/3
# #Busco los tres puntos de un triangulo equilatero en base al centro geometrico 
# #https://en.wikipedia.org/wiki/Equilateral_triangle
#     point1 = [x-L/2, y-apothem]
#     point2 = [x+L/2, y-apothem]
#     point3 = [x/2, y+height-apothem]
# # Guardo los puntos en forma x,y, y repito el primer punto para que se cierre el triangulo
#     xCoord = [point1[0], point2[0], point3[0], point1[0]]
#     yCoord = [point1[1], point2[1], point3[1], point1[1]]
#     plt.plot(xCoord, yCoord)
#     plt.show()
#     return

# plotTriangle(0, 0, 100)


def dibujar_triangulo_equilatero(X, Y, L):
    # Coordenadas de los vértices del triángulo
    altura = (np.sqrt(3) / 2) * L
    x = [X - L/2, X + L/2, X, X - L/2]
    y = [Y - altura/2, Y - altura/2, Y + altura/2, Y - altura/2]

    # Dibuja el triángulo
    plt.plot(x, y, 'b-')  # 'b-' para una línea azul sólida
    plt.axis('equal')  # Hace que los ejes tengan la misma escala
    plt.axis('off')  # Desactiva los ejes
    plt.show()

# Ejemplo de uso:
X = 0
Y = 0
Lado = 2.0
dibujar_triangulo_equilatero(X, Y, Lado)