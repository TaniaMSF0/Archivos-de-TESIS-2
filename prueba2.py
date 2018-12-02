import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# archivo = input('archivo de sonido:' )
#archivo = 'D:\UNI\10mo Ciclo\TESIS 2\TESIS FINAL\Data seleccionada\WAV\audio.wav'
muestreo, sonido = waves.read("C:\\WAV\\Raul.wav", 'rb')

# canales: monofónico o estéreo
tamano = np.shape(sonido)
muestras = tamano[0]
m = len(tamano)
canales = 1  # monofónico
if (m>1):  # estéreo
    canales = tamano[1]
# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = sonido[:,canal] 
else:
    uncanal = sonido
    
# rango de observación en segundos
inicia = 1.000
termina = 2.002
# observación en número de muestra
a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = uncanal[a:b]

# Gráfica
plt.plot(parte)
plt.show()

# tiempos en eje x
dt = 1/muestreo
ta = a*dt
tb = (b-1)*dt
tab = np.arange(ta,tb,dt)

plt.plot(tab,parte)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()
plt.plot(tab,parte)
