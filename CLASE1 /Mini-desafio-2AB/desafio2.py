# Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.
# Tip: Podemos usar la función sum( 𝑖𝑡𝑒𝑟𝑎𝑏𝑙𝑒 ) para obtener la suma de todos los campos. Un ejemplo de como funciona

# Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el 
# índice de un alumno. Luego debe devolver con return el promedio de sus notas en las diferentes materias.


import pandas as pd
import os

carpeta_actual = os.path.dirname(__file__)
datos = pd.read_excel(carpeta_actual + "//Datos.xlsx")
print(datos)

promedio = datos["Quimica"].sum() / len(datos["Quimica"])
print("El promedio de Quimica de todos los alumnos es", promedio.round(2))

def prome(df, index):
    alumno = df.loc[index]
    f = alumno["Fisica"]
    q = alumno["Quimica"]
    m = alumno["Matematica"]
    return (f + q + m) / 3

datos = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/Datos.xlsx")

print("El promedio del index 0 es  " , prome(datos, 0).round(2))
print("El promedio del index 1 es  " , prome(datos, 1).round(2))