# se quiere conocer más acerca del uso que le dan los usuarios al sistema, por lo cual su tarea será 
# extraer la siguiente información:

# ¿Qué porcentaje de los viajes se completaron en estado NORMAL?
# ¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)
# ¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
# ¿Cuántas estaciones diferentes fueron utilizadas?
# Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que 
# iniciaron de la misma.
# Tip: Recuerden investigar los métodos que tienen los DataFrames para ver si alguno de ellos les ayuda a 
# resolver un problema particular.


import pandas as pd
import numpy as np
import os

carpeta_actual = os.path.dirname(__file__) 
datos = pd.read_csv(carpeta_actual + "//recorridos-realizados-2021-sample.csv")
print(datos)

# Respuesta 1

numero_de_filas = len(datos)
estado_count = datos["Estado cerrado"].value_counts()
porcentaje_normal = (100 * (estado_count["NORMAL"] / numero_de_filas))
print(f"el porcentaje de viajes que se completaron en estado normal es de: {porcentaje_normal:.2f}%")

# Respuesta 2

promedio = round(datos["Duración"].mean())
print(f"el promedio de duracion de los viajes es de : {promedio//60} minutos y {promedio%60} segundos")

# Respuesta 3

horario_de_inicio = datos["Fecha de inicio"]
horario_de_inicio = pd.to_datetime(horario_de_inicio)
hora_de_inicio = horario_de_inicio.dt.hour
hora_pico = hora_de_inicio.value_counts().idxmax()
print(f"Entre las {hora_pico} hs y las {(hora_pico + 1)} hs se realizaron mas viajes")

# Respuesta 4

# Con pd.concat unimos las columnas de estaciones de inicio y fin,
# en caso de que una estación aparece sólo en una de ellas
# Usando len() y .value_counts() encontramos la cantidad total de estaciones
id_inicio =  datos["Nombre de estación de inicio"]
id_fin = datos["Nombre de estación de fin de viaje"]
estaciones_total = pd.concat([id_inicio,id_fin])      
print(f"Fueron utilizadas {len(estaciones_total.value_counts())} estaciones")

# Respuesta 5

# Usando .value_counts().iteritems() podemos recorrer las estaciones ordenadas
# por la cantida de veces que aparece cada una
print('\nCantidad de viajes iniciados en cada estación:\n')
for estacion, cantidad in id_inicio.value_counts().items():
    print('Cantidad:', cantidad, ' Estación:', estacion)
