# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. El archivo tiene cuatro columnas:

# Equipo
# Puntos
# Goles a favor
# Goles en contra
# Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), y mostrar todas las diferencias usando print.
# Determinar qué equipo es el campeón (1ro) y perdedor (último). ¿Qué columnas del archivo hay que analizar en este caso?
# Determinar qué equipos obtuvieron mas de 20 puntos, y mostrar sus diferencias de goles
# Plus: ordenar los equipos de mayor a menor en puntaje (de forma descendiente)

import pandas as pd
import os 

carpeta_actual = os.path.dirname(__file__) 
archivo = pd.read_excel(carpeta_actual + "//Tabla1.xlsx")
archivo["Diferencia de Gol"] = archivo["Goles a favor"] - archivo["Goles en contra"]
print(archivo)

campeon = archivo[archivo["Puntos"] == archivo["Puntos"].max()].iloc[0]
perdedor = archivo[archivo["Puntos"] == archivo["Puntos"].min()].iloc[0]
print(campeon["Equipo"], "resulto campeon con:", campeon["Puntos"])
print(perdedor["Equipo"], "resulto campeon con:", perdedor["Puntos"])


equipo_mas_de_20 = archivo[archivo["Puntos"] > 20 ]
equipo_ordenado = equipo_mas_de_20.sort_values( by = ["Puntos"], ascending=False)

print(equipo_mas_de_20)
print(equipo_ordenado)

