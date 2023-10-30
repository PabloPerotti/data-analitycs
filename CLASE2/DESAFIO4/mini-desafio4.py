# Mini desafío 4

# Leer el archivo notas.xlsx que tiene en el campo Notas los puntajes de alumnos en un examen 
# (van de 0 a 10) y armar un histograma con los datos, guardarlo en un archivo Notas.png

import matplotlib.pyplot as plt
import pandas as pd
import os

carpeta_actual = os.path.dirname(__file__) 
archivo = pd.read_excel(carpeta_actual + "//notas.xlsx") 

data = archivo.to_dict("list")

# Con plt.figure elegimos el tamaño del gráfico
plt.figure(figsize=(12, 5))

# Debemos elegir bins del 0 al 11 para que los intervalos de bins correspondan
# a los intervalos semi-abiertos:
# [0, 1) [1, 2) [2, 3) ... [10, 11)
# con align elegimos centrar los bins en el 'borde izquierdo' del intervalo
# Con rwidth controlamos el espesor de las barras
# Con zorder elegimos el orden en que se dibujan los elementos gráficos
plt.hist(data["notas"], range(12), align = 'left', rwidth=0.75, zorder=2)

# xticks de 1 en 1, yticks de 10 en 10
plt.xticks(range(0, 11))
plt.yticks(range(0, 130, 10))

# Grilla horizontal, linea punteada, detras del histograma
plt.grid(axis='y', linestyle='--', zorder=1)

plt.savefig('Notas.png')
plt.show()