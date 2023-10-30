# ★★  Las Algas del Nahuel Huapi (Bug Catcher Continuado)
# Bug Catcher ha encontrado un paper sobre el crecimiento de algas en relación a la intensidad de luz. No entiende los gráficos del paper (porque no estan 
# hechos en Python) pero llega a leer:
# Debajo de una intensidad de  3%  de la del sol ( 𝐼0 ) el crecimiento de las algas disminuye rapidamente
# entre  3%  y  25%  las algas crecen bien.
# Objetivo
# Mostrar rango de profundidad a la cual las algas podrían sobrevivir en el Nahuel Huapi en  𝗏𝖾𝗋𝖽𝖾  y la zona a partir de la cual sufren en  𝗋𝗈𝗃𝗈 .
# Tips:
# %𝐼0 = 𝐼𝑧 / 𝐼0 = 𝑒−𝑘𝑧     ⟶       𝑧 = −ln(%𝐼0) / 𝑘 
# Funcion coloreado debajo la curva: plt.fill_between(zbien, Izbien, color="green", label="Crecimiento bueno")
# Bonus
# ¿Cómo se ve afectada la zona donde sobreviven las algas al modificar el parametro  𝑘 ?

import numpy as np
import matplotlib.pyplot as plt

IzIo=0.1
zfNahuel = 56

# despeje (formula)
kNahuel=-np.log(IzIo)/zfNahuel
kRioArriba = 0.009
zfRioArriba = -np.log(IzIo)/kRioArriba

Izsuperior = 0.25
Izinferior = 0.03
zinferior= -np.log(Izsuperior)/kNahuel
zsuperior = -np.log(Izinferior)/kNahuel

I0= 700

zbien  = np.arange(zinferior,zsuperior,0.2)
zmal =np.arange(zsuperior,zfRioArriba,0.2) 

Izbien = I0*np.e**(-kNahuel*zbien) 
Izmal = I0*np.e**(-kNahuel*zmal)
plt.fill_between(zbien, Izbien, color="green",label="Crecimiento bueno")

plt.fill_between(zmal, Izmal,color="red",label="Crecimiento malo")
plt.legend(loc="upper right")
plt.show()