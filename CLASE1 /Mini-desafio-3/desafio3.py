# Obtener el promedio general sólo para aquellos alumnos que aprobaron Matemática (con nota >= 6) en el archivo Datos.xlsx.

import pandas as pd
import os

carpeta_actual = os.path.dirname(__file__)
datos = pd.read_excel(carpeta_actual + "//Datos.xlsx")
print(datos)

aprobados = datos[(datos["Matematica"] >= 6)]
promedio = ((aprobados["Quimica"] + aprobados["Fisica"] + aprobados["Matematica"])/3).round(2)

promedio_total = (sum(promedio)/len(promedio))

print(aprobados)
print(promedio)
print(promedio_total)