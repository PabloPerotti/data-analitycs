import matplotlib.pyplot as plt

#SOLUCION 1
#explode: Le indicamos si alguna de las porciones debe estar alejada del centro
# sizes = [255, 130, 245, 210, 300]
# e = (0.2, 0, 0, 0, 0) # Cuánto separar cada porción

# plt.pie(sizes, explode=e)
# plt.show()


#SOLUCION 2
# labels: Le indicamos el nombre de cada porción.
# l = ('Python', 'C++', 'Ruby', 'Java')
# sizes = [255, 130, 245, 210]
# e = (0.1, 0, 0, 0)  # explode 1st slice

# plt.pie(sizes, explode=e, labels=l)
# plt.show()


#SOLUCION 3
# colors: Le podemos asignar una paleta de color.
# l = ('Python', 'C++', 'Ruby', 'Java')
# sizes = [255, 130, 245, 210]
# c = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# e = (0.1, 0, 0, 0)  # explode 1st slice

# plt.pie(sizes, explode=e, colors=c, labels=l)
# plt.show()


#SOLUCION 4
# startangle: Le indicamos el ángulo de rotación.
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [2150, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# explode = (0.1, 0, 0, 0)  # explode 1st slice

# plt.pie(sizes, explode=explode, labels=labels, colors=colors,  startangle=0)
# plt.show()


#SOLUCION 5
# autopct: Le indicamos que muestre los porcentajes. Este parámetro sigue una sintáxis estándar, para que 
# muestre 1 decimal se usa: "%1.1f%%". De esta forma le indicamos que vamos a mostrar un numero float con 
# 1 decimal y el %% indica que queremos el simbolo %. Se utiliza un doble % porque el primero es usado 
# como símbolo de escape.

labels = ('Python', 'C++', 'Ruby', 'Java')
sizes = [255, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%5.01f%%',  startangle=140)
#en autopct ponemos como deseamos que se escriban los porcentajes
plt.show()
