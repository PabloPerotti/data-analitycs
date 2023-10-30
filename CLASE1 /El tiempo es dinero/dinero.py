# ★★  El tiempo es dinero
# Temas:

# Analisís de información estructurada
# Librerías
# La administración del dinero es una tarea que requiere una altísima fiabilidad. En esta ocasión tu objetivo será programar un script que 
# actualize la cantidad de dinero de una serie de usuarios a partir de la información de las transferencias que fueron realizadas. Más concretamente 
# recibiras una base de datos con la cantidad de dinero de una serie de usuarios, un base de datos con una serie de transferencias que los usuarios se 
# realizan entre si, y deberás generar con eso una nueva base de datos con el dinero actualizado de cada usuario.

# Importar el archivo Finanzas.xlsx que contiene la cantidad de dinero de los usuarios y las transferencias en dos hojas de archivo.
# Exportar un archivo usuarios_actualizados.xlsx que contiene las cantidades de dinero actualizadas.


import pandas as pd
import os

carpeta_actual = os.path.dirname(__file__)

usuarios_datos = pd.read_excel(carpeta_actual + "//Finanzas.xlsx", "Usuarios", index_col="Usuario")
usuarios = usuarios_datos.to_dict("index")
print(usuarios_datos)

transferencias_usuarios = pd.read_excel(carpeta_actual +"//Finanzas.xlsx", "Transferencias")
transferencias = transferencias_usuarios.to_dict("records")
print(transferencias_usuarios)

for transferencia in transferencias:
    emisor = transferencia["Emisor"]
    receptor = transferencia["Receptor"]
    monto = transferencia["Monto"]

    usuarios[emisor]["Presupuesto"] -= monto
    usuarios[receptor]["Presupuesto"] += monto

usuarios_actualizados = pd.DataFrame.from_dict(usuarios, orient="index")  
print("Usuarios luego de realizar las transferencias:")
print(usuarios_actualizados)

usuarios_actualizados.to_excel("usuarios_actualizados.xlsx")