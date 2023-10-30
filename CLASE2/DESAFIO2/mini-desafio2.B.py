# Mini desafío 2.B - Challenge
# Se pide realizar un gráfico de la cotización de las acciones diarias de las compañias Amazon 
# y Google de los últimos 10 años. Encontrar los puntos donde se cruzan los dos gráficos y 
# marcarlos con un punto. Usar dos tipos de línea distintos.
# Nota:
# Usen la función read_csv. Recuerden que un .csv es prácticamente identico a un .xlsx.
# Los valores a graficar estan la columna Open (usando to_dict("list") podrían resolver el 
# problema).
# Tip: Ya que los gráficos son discretos, para detectar un cruce deberán revisar que la acción 
# que es la más cara hoy sea la que era más barata ayer. Esto es porque sería muy raro que 
# haya un día en el cual ambas acciones tengan exactamente el mismo precio. Para interpretar
# mejor este comentario pueden observar que en la siguiente imagen se producen 2 cruces, pero 
# sólamente en el primero el cruce es exactamente sobre el mismo valor:


#SOLUCION 1
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import matplotlib.dates as mdates
import pandas as pd

carpeta_actual = os.path.dirname(__file__) 
archivo_amazon = pd.read_csv(carpeta_actual + "//AMZN.csv")
archivo_google = pd.read_csv(carpeta_actual + "//GOOGLE.csv")

google = archivo_google.to_dict("list")
amazon = archivo_amazon.to_dict("list")

#print(google['Open'])
#print(amazon['Open'])

plt.figure(figsize=(16, 8))

#Empiezan con el valor del primer dia
gx = [google["Date"][0]]
gy = [google["Open"][0]]
ax = [amazon["Date"][0]]
ay = [amazon["Open"][0]]

crucex = []
crucey = []

for i in range(1, len(google["Date"])): #range empieza desde 1 en vez de 0
    gx.append(google["Date"][i])
    gy.append(google["Open"][i])
    ax.append(amazon["Date"][i])
    ay.append(amazon["Open"][i])

# Condicional de cruce (son iguales o invirtieron su orden)
    if (ay[i] == gy[i]) or (ay[i] > gy[i] and ay[i-1] < gy[i-1]) or (ay[i] < gy[i] and ay[i-1] > gy[i-1]):
        crucex.append(gx[i])
        crucey.append(gy[i])

plt.plot(gx,gy)
plt.plot(ax,ay)
plt.plot(crucex,crucey, 'k.')

# En el eje X elijo mostrar 1 cada 100 fechas
# Roto las fechas 60° y luego elijo la alineación con el borde derecho del texto
plt.xticks(gx[::100], rotation=60, horizontalalignment='right')

plt.show()

#SOLUCION 2

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import os

# carpeta_actual = os.path.dirname(__file__) 
# # Leo los dfs
# google = pd.read_csv(carpeta_actual + "//GOOGLE.csv")
# amazon = pd.read_csv(carpeta_actual + "//AMZN.csv")

# # Me fijo que en la misma fecha, ambos valores den relativamente similar (difrencia < X)
# # Pongo cruces = ambos.copy porque sino arroja un aviso de que puede estar mal cuando estoy poniéndole valores a la copia
# X = 5
# ambos = pd.merge(google, amazon, how="inner", on=["Date"],suffixes=('_google', '_amazon'))
# cruces = ambos.loc[ abs(ambos["Open_google"] - ambos["Open_amazon"]) < X, :].copy(deep=True)

# #PLUS: cambio las fechas, para mostrarlas en formato "dd/mm/aa" y horizontalmente, para lectura más rápida
# for index, row in google.iterrows():
#     google.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]
# for index, row in amazon.iterrows():
#     amazon.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]
# for index, row in cruces.iterrows(): 
#     cruces.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]

# plt.figure(figsize=(16, 8))
# plt.plot(google["Date"],google["Open"])
# plt.plot(amazon["Date"],amazon["Open"])
# plt.plot(cruces["Date"],cruces["Open_google"], 'k.')

# # En el eje X elijo mostrar 1 cada 250 fechas
# # Luego elijo la alineación con el borde derecho del texto
# plt.xticks(google["Date"][::250], horizontalalignment='right')

# plt.show()