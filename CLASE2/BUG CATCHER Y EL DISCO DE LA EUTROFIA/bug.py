# ★★  Bug Catcher y el disco de la Eutrofia
# Atención: Este problema asume algunos conocimientos básicos de analisis matemático.
# Pasaron 10 años desde que se concretó un acuerdo para la construcción de una fabrica de queso al lado del Lago Nahuel Huapi, a dos kilometros de la 
# ciudad natal de Bug Catcher. Bug Catcher dice que en ese tiempo el agua del lago ha visto un deterioro en su calidad y esta peticionando ante la ciudad
# la imposición de regulaciones más estrictas sobre los efluentes del sector industruial.
# Pero primero tiene que demostrar este deterioro... Y así, Bug Catcher ha venido a tí para pedirte ayuda, graficando los resultados de un estudio de agua.

# El estudio
# Se efectua un estudio de turbiedad de agua del tipo Secchi . El estudio consiste en hundir un disco blanco en el cuerpo de agua a estudiar y medir la
# profundidad  𝑧f  a la cual el disco desaparece. Para el estudio se tiene que tener en cuenta la intensidad de la luz sobre el cuerpo de agua  𝐼0 .
# El problema
# Bug Catcher quiere un gráfico que muestre la turbiedad del lago Nahuel Huapi y compararlo a la de otro lago cercano río arriba.
# Objetivo
# Graficar la intensidad de luz  𝐼𝑧  en el eje vertical a una profundidad  𝑧 ( 𝑧 en el eje horizontal) para el Nahuel Huapi y el otro lago.
# Datos
# Rige la ley de Beer-Lambert:
# 𝐼𝑧 / 𝐼0=𝑒−𝑘𝑧 
# donde:
# - 𝐼𝑧  es la intensidad de luz a una profundidad  𝑧 
# - 𝐼0  es la intensidad de luz sobre la superficie del agua, para un día soleado  𝐼0≈700 W/m2 
# - 𝑘  es el factor de atenuación del agua. Indica turbiedad.
# Sabemos que el disco Secchi de Bug Catcher desaparece bajo 56cm de agua del Nahuel Huapi. Para todos los cálculos suponga que la relación  𝐼𝑧f / 𝐼0  vale  10% 
# (para la profundidad a la cual desaparece el disco).
# El factor de atenuación del lago río arriba fue medido la semana pasada y vale  𝑘ra=0,009 cm−1 .

# Tips:
# Hay que despejar  𝑘  y calcularla para el lago Nahuel Huapi antes de graficar.
# La función log de la libreria math es el logaritmo natural.
# Prueben graficar ambas curvas hasta la profundidad  𝑧f  del lago río arriba.
# Tener una bolígrafo y un cuaderno abierto ayuda.

import numpy as np
import matplotlib.pyplot as plt
IzIo=0.1
zfNahuel = 56

# despeje (formula)
kNahuel=-np.log(IzIo)/zfNahuel
kRioArriba = 0.009

#despeje (formula)
zfRioArriba = -np.log(IzIo)/kRioArriba

print('Nahuel Huapi k=',kNahuel)
print('Rio Arriba k=',kRioArriba)

# valores de z a gráficar
z = np.arange(0,zfRioArriba,1)

I0= 700

# valores a gráficar
IzNahuel = I0*np.e**(-kNahuel*z)
IzRioArriba = I0*np.e**(-kRioArriba*z)

plt.figure(figsize=(15,9))
plt.plot(z, IzNahuel, "blue",label="Nahuel Huapi")
plt.plot(z, IzRioArriba, "cyan",label="Río arriba")
plt.ylabel("Intensidad Iz [W/m^2]")
plt.xlabel("Profundidad z [cm]")

plt.legend()                                #Habilitamos los labels
plt.title("Abajo con la fabrica")
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth=0.2, color='black')
#Le asignamos el estilo a la grilla mayor
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.show()