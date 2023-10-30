
import pandas as pd
import random as n 

# df = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/Datos.xlsx")
# d = df.to_dict("list")        
# print(sum(d["Quimica"])/6)    #Calculo el promedio de las notas de quimica
#print(df)                    #  me da el diccionario con todas las listas de la tabla
# d = df.to_dict("records")   #records me hace una lista con varios diccionarios 

# for alumno in d:
#     if alumno["Nombre"] == "Sol":
#         print("Te encontre!!", alumno)

# print()     # me da el informe del legajo 0

# df = pd.read_excel("/users/pabloperotti/desktop/Curso-python/data-science/datos.xlsx", index_col = 0)
# alumno = df.loc[34567]
# print(alumno)

# df = pd.read_excel("/Users/pabloperotti/Desktop/Curso-Python/data-science/Datos.xlsx", index_col="Nombre")
# alumno = df.loc["Sol"]
# print(alumno["Matematica"])



# data = {
#     "Personas" : ["Analía Ferreyra" , "Martin Hugo", "Fernando Lorenzo"],
#     "Edad" : [25, 35, 87],
#     "Random" : [] 
# }
# for i in range(3):
#     data["Random"].append(n.randint(1, 30))
# print(data)

# dataframe = pd.DataFrame(data)
# print(dataframe)

# dataframe.to_excel("personas.xlsx")


# La función idxmax() en Pandas se utiliza para encontrar el índice del primer valor máximo en una Serie o 
# columna de un DataFrame. En otras palabras, idxmax() devuelve el índice (o etiqueta) del elemento que tiene 
# el valor máximo en una Serie de Pandas.

# Supongamos que tienes una Serie de puntajes
puntajes = pd.Series([85, 92, 78, 95, 88])

# Encuentra el índice del puntaje más alto
indice_maximo = puntajes.idxmax()

print("El índice del puntaje más alto es:", indice_maximo)