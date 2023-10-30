# Caja y Bigote
# Vamos a crear un histograma y un Box-and-Whisker plot.
# Este tipo de gráfico es comunmente utilizado para mostrar la distribución de una muestra poblacional de 
# forma muy visual.

# Procesar Notas de tres parciales (convertirlas a números). Se debería obtener tres listas con notas del 0-140,
# una para cada uno de los tres parciales. ¡Tengan cuidado que pandas devuelve las notas en formato string!
# Función para ver si un valor es NaN:

# Graficar Histograma
# El histograma debería tener 5 barras por cada parcial.

# Intervalos:
# Notas entre 0-30.
# Notas entre 31-60.
# Notas entre 61-90.
# Notas entre 91-120.
# Notas entre 121-140.
# Esto se puede lograr otorgandole un valor a la propiedad bins del histograma.
# plt.hist([parcial1,parcial2,parcial3], bins=intervalos_superiores ,label=nombreDeDatasets)
# Graficar Box-and-Whisker plot
# Graficar el box-and-whisker plo
# plt.boxplot([notasParcial1, notasParcial2, notasParcial3])
# Datos y Tips
# Las notas pueden contener los siguientes valores:
# 0-140 : Nota numérica.
# 'Ausente' : Indica ausencia al parcial.
# 'NaN' : El alumno no cumplió condiciones para rendir parcial (celda vacía).
# Descartar los valores no-numéricos (Ausente y NaN).
# Usar  int()  para convertir valores numericos de string a int.

def isNaN(num):
    return num != num

import pandas as pd
import matplotlib.pyplot as plt
import requests

url = "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/NotasFinitos.csv"
archivo_csv = "NotasFinitos.csv"

resp = requests.get(url)
with open(archivo_csv, "wb") as file:
    file.write(resp.content)

datos = pd.read_csv(archivo_csv)
print(datos)

notas1 = datos.loc[~isNaN(datos['1P']) & (datos['1P'] != 'Ausente'), '1P']
notas2 = datos.loc[~isNaN(datos['2P']) & (datos['2P'] != 'Ausente'), '2P']
notas3 = datos.loc[~isNaN(datos['3P']) & (datos['3P'] != 'Ausente'), '3P']


intervalos_superiores=[30,60,90,120,140]
nombreDeDatasets=['Parcial 1','Parcial 2','Parcial 3']
plt.hist(["parcial1","parcial2","parcial3"], bins=intervalos_superiores ,label=nombreDeDatasets)
plt.legend(loc="upper right")
plt.show()

_=plt.boxplot(["parcial1","parcial2","parcial3"]) 