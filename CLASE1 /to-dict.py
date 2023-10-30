import pandas as pd

archivo = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/Datos.xlsx")
data = archivo.to_dict("list")     # "list" significa que vamos a almacenar a cada columna como una lista con su contenido
print(data)
print(data["Nombre"])
print(data["Nombre"][2])

data = archivo.to_dict("records") # "records" significa que vamos a obtener el contenido separado por cada fila
print(data)
print(data[2])
print(data[2]["Nombre"])

# archivo = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/Datos.xlsx", index_col="Apellido")
data = archivo.to_dict("index")
# "index" significa que vamos a obtener el contenido como diccionarios 
# donde la clave es algun campo de cada fila, en este caso la clave de los 
# diccionarios será la clave "Apellido"

# convertimos el tipo de dato de pandas a un dict de python
print(data)
print(data["Martinez"])
print(data["Martinez"]["Legajo"])