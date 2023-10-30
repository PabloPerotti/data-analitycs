# ★★  Demografía en Argentina
# Se pide visualizar la distribución etaria de la población del país. Para ello se cuenta con la información de 2019 en el archivo PopulationArgentina2019.csv,
# en el cual se detalla para cada rango de edades, el número de individuos de sexo femenino y de sexo masculino (estas fueron las únicas dos categorías que 
# fueron contempladas por quién recolectó estos datos). La primer columna 'Age' tiene los valores '0-4', '5-9', '10-14', '15-20', etc. hasta '100+' para 
# cada rango de edades. Las siguientes dos columnas son 'M' y 'F', contienen el número de hombres y de mujeres en la población respectivamente. Se deben 
# mostrar un grafico de barras para hombres y uno para mujeres, mostrando los rangos de edad en el eje horizontal y el porcentaje con respecto a la población
# total en el eje vertical.
# Tip: Usar plt.bar(x, height) para crear gráficos de barra, el resultado debería asemejarse a la siguiente imagen:

import matplotlib.pyplot as plt
import pandas as pd
import os 

carpeta_actual = os.path.dirname(__file__) 
df = pd.read_csv(carpeta_actual + "//PopulationArgentina2019.csv")
print(df)
#SOLUCION 1 
# datos = archivo.to_dict('list')
# Age = datos['Age']
# M = datos['M']
# F = datos['F']

# total = sum(M) + sum(F)
# M_porcentual = [ 100* i/total for i in M ]
# F_porcentual = [ 100* i/total for i in F ]

# plt.figure(figsize=(16, 8))
# plt.subplot(2, 1, 1)
# plt.title('Distribución etaria en mujeres')
# plt.bar(Age, F_porcentual)
# plt.ylabel('Porcentaje')

# plt.subplot(2, 1, 2)
# plt.title('Distribución etaria en hombres')
# plt.bar(Age, M_porcentual)
# plt.ylabel('Porcentaje')
# plt.show()

#SOLUCION 2 = UTILIZANDO UNICAMENTE PROPIEDADES DE PANDAS
total = df.sum()
df.M_porcentual = 100*df['M']/(total.M + total.F)
df.F_porcentual = 100*df['F']/(total.M + total.F)

plt.figure(figsize=(16, 8))
plt.subplot(2, 1, 1)
plt.title('Distribución etaria en mujeres')
plt.bar(df.Age, df.F_porcentual)
plt.ylabel('Porcentaje')

plt.subplot(2, 1, 2)
plt.title('Distribución etaria en hombres')
plt.bar(df.Age, df.M_porcentual)
plt.ylabel('Porcentaje')
plt.show()