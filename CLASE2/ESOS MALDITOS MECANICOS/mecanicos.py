# ★★★  Esos Malditos Mecánicos...
# Intro
# Volodymyr es un profesor de la materia Elementos Finitos I en el ITBA. El método de los elementos finitos consiste en modelar sistemas de sólidos 
# o fluidos mediante una partición del sistema en subsistemas que se resuelven en conjunto según condiciones de borde y condiciones iniciales.
# Problema
# El segundo cuatrimestre del 2018 Volodymyr tomó 3 parciales y ahora quiere obtener estadísticas y además saber cuales alumnos aprobaron y cuales no.
# El archivo NotasFinitos.csv contiene los datos reales de dicha materia sin los nombres de los alumnos.
# Objetivos
# Del archivo "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/NotasFinitos.csv" :
# Obtener promedios para cada parcial.
# Obtener promedio para toda la cursada.
# Obtener promedios de los que aprobaron la materia, para cada parcial.
# Condiciones de Borde
# Condición de aprobación de parcial: Nota>=60.
# Para aprobar la materia se necesita aprobar 2 parciales y sumar entre los tres parciales: sumaNotas>=160.
# Las notas pueden contener los siguientes valores:
# 0-140 : Nota numérica.
# 'Ausente' : Indica ausencia al parcial.
# 'NaN' : El alumno no cumplio condiciones para rendir parcial (celda vacia).
# Tomar los valores Ausente y NaN como 0. Usar la función  isNaN  en el código de arriba.
# Tips:
# ¡Las funciones pueden ser muy útiles para este ejercicio!
# Existe una columna de tres números llamada MAX con el máximo puntaje por parcial (ordenado de primer parcial a tercer parcial). No hace falta usar
# este dato para resolver el ejercicio.
# Convertir la nota de string a int usando la función  int(𝑁𝑜𝑡𝑎) .
# Hint:
# Hay 49 alumnos, 19 aprobaron la materia según el criterio dado.

import pandas as pd
import os

def isNuN(num):
    return num != num

def getNota(estado):
    #Definimos la forma de tomar cada calificación
    if isNuN(estado):
        return 0
    if estado.lower() == 'ausente':
        return 0
    try:
        return int(estado)
    except ValueError:
        return 0
    
def aprobado(parcial1, parcial2, parcial3):
    #Definimos las condiciones de borde para aprobar
    if parcial1 + parcial2 + parcial3 < 160:
        return False
    if parcial1 >= 60 and parcial2 >=60:
        return True
    if parcial1 >= 60 and parcial3 >=60:
        return True
    if parcial2 >= 60 and parcial3 >=60:
        return True
    else:
        return False
        
carpeta_actual = os.path.dirname(__file__)
datos = pd.read_csv(carpeta_actual + "//NotasFinitos.csv")
print(datos)

notas = [datos["1P"], datos["2P"], datos["3P"]]
N = len(notas[0])    # Es la cantidad de alumnos notasNumericas

sum = [0, 0, 0]                   #Aca guardamos la suma de los parciales
sumAprobados = [0, 0, 0]          #Aca guardamos la suma de los parciales de los alumnos aprobados
alumnosAprobados = 0

for i in range(len(notas[0])):    #Por cada alumno
    nota = [0, 0, 0]              
    for j in range(len(nota)):    
        nota[j] = getNota(notas[j][i])      #Obtengo sus notas de cada parcial
        sum[j] += nota[j]               #Y las sumo al total de TODOS los alumnos

    estaAprobado = aprobado(nota[0],nota[1],nota[2])
    if estaAprobado:                  #Si aparte esta aprobado
        alumnosAprobados += 1           #Aumento la cantidad de aprobados
        for j in range(len(sumAprobados)):  
            sumAprobados[j] += nota[j]    #Sumo sus notas al total de los alumnos aprobados
    
prom = []
for i in range(len(sum)):
    prom.append(sum[i]/N)             #Obtengo el promedio de TODOS los alumnos para cada parcial

promAprobados = []                  
for i in range(len(sumAprobados)):  #Por cada parcial
    promAprobados.append(sumAprobados[i] / alumnosAprobados) #Obtengo el promedio solo de los aprobados

print('Cantidad alumnos:',N, '  Cantidad alumnos aprobados:',alumnosAprobados)
print('Promedios para parciales: P1=',prom[0],'P2=',prom[1],'P3=',prom[2])
print('Promedios de los aprobados: P1=',promAprobados[0] ,'P2=',promAprobados[1],'P3=',promAprobados[2] )


