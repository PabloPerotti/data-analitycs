# ★★  Venta de pasajes
# Python Airlines es la nueva low-cost en el mercado. Parece que todo el mundo quiere volar en esta aerolínea, pero la cantidad de asientos es limitada y la
# aerolínea no puede comprar nuevos aviones fácilmente. El departamento de ventas tuvo una gran idea (o al menos eso es lo que compañía piensa). Observaron que
# algunos de viajeros no se presentan para abordar el vuelo, así que van a vender más pasajes que la cantidad de asientos disponibles y confiar en que 
# suficientes pasajeros no se presenten en el aeropuerto como para no tener que impedir el ingreso de pasajeros al avión.
# Las características de los vuelos son los siguientes:
# La aerolínea tiene como ganancia neta $400 por pasaje vendido, independientemente de que se presente el pasajero.
# Si la cantidad de pasajeros que se presentan es mayor a la cantidad de asientos, la aerolínea debe gastar $600 por pasajero extra para poder ofrecer un 
# hotel y una compensación.
# Cada pasajero tiene una probabilidad del 95% de presentarse en el aeropuerto para tomar el vuelo.
# Cada avión tiene capacidad para 222 pasajeros.
# Simular 1000 vuelos en los cuales se vendieron exactamente 250 pasajes. Calcular la ganancia neta promedio que se obtiene vendiendo esta cantidad de
# pasajes (la venta de pasajes siempre produce la misma ganancia, y se debe restar la pérdida por compensación que depende de la cantidad de pasajeros que 
# se presenten).
# Repetir el cálculo de la ganancia promedio para distinta cantidad de pasajes vendidos, entre un rango de 222 y 250. Graficar la ganancia promedio en 
# función de la cantidad de pasajes vendidos y mostrar el punto de máxima ganancia.
# Tip:
# Se puede usar np.random.rand() < 0.95 para determinar si cierto pasajero se presenta o no.
# Usando mi_lista.index( max(mi_lista) ) se obtiene primero el valor máximo de una lista, y luego se busca el índice en el cual aparece ese valor. De 
# esta forma obtenemos el índice de la lista en el cual se encuentra el valor máximo.

import matplotlib.pyplot as plt
import numpy as np

vendidos = []
ganancias = []

MAX_CAPACIDAD = 222
PASAJES_VENDIDOS = 250
Q_SIMULACIONES = 1000
GANANCIA_NETA_PASAJE = 400
COMPENSACION = 600
PROBABILIDAD_DE_PRESENTE = 0.95

# v es la cantidad de pasajes vendidos
for v in range(MAX_CAPACIDAD, PASAJES_VENDIDOS + 1):
    promedio = 0

    # i es el indice de cada simulacion
    for i in range(Q_SIMULACIONES):
        presentes = 0
        for p in range(v):
            if np.random.rand() < PROBABILIDAD_DE_PRESENTE:  # Determino si la persona p esta presente
                presentes += 1
        if presentes <= MAX_CAPACIDAD:
            promedio += v*GANANCIA_NETA_PASAJE    # Venta del pasaje
        else:
            promedio += v*GANANCIA_NETA_PASAJE - (presentes-MAX_CAPACIDAD)*COMPENSACION   # Venta menos compensación
    promedio /= Q_SIMULACIONES
    ganancias.append(promedio)
    vendidos.append(v)

# Imprimo el valor máximo
imax = ganancias.index(max(ganancias))
print("Al vender", vendidos[imax], "pasajes, se espera ganar: $", ganancias[imax])

plt.figure(figsize=(12, 6))
plt.plot(vendidos, ganancias)
plt.plot(vendidos[imax], ganancias[imax], 'ro')   # Muestro el valor máximo
plt.grid()
plt.show()