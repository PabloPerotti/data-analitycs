# ★  Copy
# Temas:
# Uso de librerías
# Manejo de archivos
# Armar una función que copie un archivo .xlsx, y lo guarde como "Copia 1 - 𝑛𝑜𝑚𝑏𝑟𝑒", de ya existir debe 
# guardarlo como Copia 2 -, Copia 3 - , ...
# Usar la libreria os para chequear si existe el archivo. Tips:
# os.path.exists(𝑛𝑜𝑚𝑏𝑟𝑒) devolverá True si ya existe
# Se puede importar con: import os

import os
import shutil

def func(nombre):
    repeticion = 1

    while os.path.exists("Copia " + str(repeticion) + " "+ nombre):
        repeticion += 1
        
    shutil.copyfile(nombre, "Copia " + str(repeticion) + " "+ nombre)
    
        
func('Tabla1.xlsx')


