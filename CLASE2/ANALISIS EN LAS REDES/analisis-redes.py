# ★  Análisis en las redes
# Se pide graficar en función del tiempo la cantidad de vistas, minutos vistos, likes, y subscriptores ganados de un canal de Youtube. Además, se debe indicar
# cuándo se produjo el mayor incremento de un día hacia otro para cada variable mencionada.
# Los datos reales se encuentran en un archivo JSON obtenido mediante la API de YouTube para el Canal de YouTube de IEEE-ITBA.
# Para convertir la información en el archivo a estructuras de datos conocidas se puede emplear el siguiente código, de forma que no es necesario conocer
# el formato JSON, sólamente trabajar con datos de Python:
# import json
# json_file = open('youtube_data.json')
# data = json.load(json_file)
# Tips:
# Para mostrar las fechas sin que se superpongan, se puede usar fig, ax = plt.subplots(1) antes de comenzar a graficar, para luego usar fig.autofmt_xdate().
# Otra alternativa es rotar el texto con plt.xticks(rotation=90)
# ¡Pueden buscar en internet todo lo que necesiten! Si les hace falta realizar cierta tarea que no fue explicada en esta clase pueden encontrar muchas 
# respuestas investigando.

import json
import os
import matplotlib.pyplot as plt


carpeta_actual = os.path.dirname(__file__) 
json_file = open(carpeta_actual + '//youtube_data.json', encoding="utf-8")
data = json.load(json_file)


day = []
emw = []
views = []
likes = []
subs = []

# Organizo la información
for day_info in data['rows']:
    day.append(day_info[0])
    emw.append(day_info[1])
    views.append(day_info[2])
    likes.append(day_info[3])
    subs.append(day_info[4])

# Determino el cambio diario
emw_change = [emw[i] - emw[i-1] for i in range(1, len(emw))]
views_change = [views[i] - views[i-1] for i in range(1, len(views))]
likes_change = [likes[i] - likes[i-1] for i in range(1, len(likes))]
subs_change = [subs[i] - subs[i-1] for i in range(1, len(subs))]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(12, 10))

ax1.plot(day, emw)
i = emw_change.index( max(emw_change) ) + 1  # Máximo cambio
ax1.plot(day[i], emw[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(emw[i],day[i]))
ax1.set_title('Estimated Minutes Watched')
ax1.grid()
ax1.legend()

ax2.plot(day, views)
i = views_change.index( max(views_change) ) + 1
ax2.plot(day[i], views[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(views[i],day[i]))
ax2.set_title('Views')
ax2.grid()
ax2.legend()

ax3.plot(day, likes)
i = likes_change.index( max(likes_change) ) + 1
ax3.plot(day[i], likes[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(likes[i],day[i]))
ax3.set_title('Likes')
ax3.grid()
ax3.legend()

ax4.plot(day, subs)
i = subs_change.index( max(subs_change) ) + 1
ax4.plot(day[i], subs[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(subs[i],day[i]))
ax4.set_title('Subscribers Gained')
ax4.grid()
ax4.legend()

fig.autofmt_xdate()
plt.show()



