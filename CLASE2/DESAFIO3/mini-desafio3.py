# Mini desafío 3
# PARTE 1
# Visualizar usando un piechart la cuota de mercado de diferentes compañías que ofrecen un 
# producto (por ejemplo: marcas de celulares). Buscar en internet los valores actuales para el 
# producto que eligieron.
# PARTE 2
# Averiguar el color favorito de caramelos Sugus de diferentes amigos o conocidos y visualizar
# la información con un gráfico piechart, mostrando los colores de cada sección que 
# corresponden al color de caramelo.

# PARTE 1

import matplotlib.pyplot as plt

labels = ('Apple', 'Samsung', 'Huawei', 'Xiaomi', 'vivo', 'Oppo', 'Lenovo', 'Otros')
sizes = [72.3, 70.4, 56.2, 32.9, 31.5, 31.4, 11.7, 94.7] #Millones de unidades: 2019 Q4
colors = ['silver', 'royalblue', 'orangered', 'orange', 'cornflowerblue', 'green', 'red', 'grey']

fig = plt.figure(figsize=(6, 6))

plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle = 90)

# Dibujar un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.50,fc='white')
fig.gca().add_artist(centre_circle)

plt.show()

# PARTE 2

labels = ('Frutilla', 'Menta', 'Anana', 'Limón', 'Manzana', 'Naranja')
sizes = [10, 6, 2, 9, 4, 1]
colors = ['red', 'green', 'blue', 'yellow', 'lime', 'orange']

fig = plt.figure(figsize=(6, 6))

plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle=0)

# Dibujar un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

plt.show()