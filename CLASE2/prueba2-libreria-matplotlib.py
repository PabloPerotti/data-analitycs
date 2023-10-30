import matplotlib.pyplot as plt

# Cantidad de puntos
n = 11

# x/(n-1) genera valores entre 0 y 1
# ya que x va desde 0 hasta (n-1)
X = [ x/(n-1) for x in range(n) ]
print(X)

# Para cada valor en X calculo la función elegida
Y = [ x**2 for x in X ]
print(Y)

plt.plot(X, Y)    # plt.plot recibe 2 listas de igual longitud, la primera para el eje X, la segunda para el eje Y
plt.show()        # Luego de generar el gráfico, lo mostramos