# Extraer la siguiente información:
# ¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
# ¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas? Rta: 2466.31
# ¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814
# ★★  Obtener la media y la varianza de la propiedad 'median_house_value'. Rta: 207300.91 - 13451442293.57
# Tip: ¡Pueden investigar funciones de numpy para conseguir la media y la varianza! numpy.var

import pandas as pd
import numpy as np

datos = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/California-Housing/california_housing_train.xlsx")
# print(datos)

#respuesta 1
median_house_mayor_80000 = datos[(datos["median_house_value"] > 80000) & (datos["longitude"] >= -120) & (datos["longitude"] <= -118)]
cantidad_houses = len(median_house_mayor_80000)
print(median_house_mayor_80000)
print(cantidad_houses)

#respuesta 2
prom = (median_house_mayor_80000["total_rooms"]).mean()
print(prom)

#respuesta 3
mas_cara = (median_house_mayor_80000["median_house_value"]).max()
# print(mas_cara)
cantidad_mas_cara = datos[(datos["median_house_value"] == mas_cara)]
print(len(cantidad_mas_cara))

#respuesta 4
media = np.mean(datos["median_house_value"])
print(media.round(2))

varianza = np.var(datos["median_house_value"])
print(varianza.round(2))