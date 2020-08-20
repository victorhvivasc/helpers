import mecanica_fisica
import numpy as np
import Graficas3D


"""Ejemplo

Un ciclista comienza su paseo matutino y al cabo de 10 segundos su velocidad es de 7.2 km/h. 
En ese instante ve aproximarse un perro y comienza a frenar durante 6 segundos 
hasta que la bicicleta se detiene. 

Calcular:

a) La aceleración hasta que comienza a frenar. 
b) La aceleración con la que frena la bicicleta.
c) El espacio total recorrido.
"""

v0 = 0.
v1 = 7.2*1000/3600
t0 = 0.
t1 = 10.

aceleracion = mecanica_fisica.aceleracion_cinematica(v0, v1, t0, t1, euclidea=False)
print("aceleracion = ", aceleracion)
desacelera = mecanica_fisica.aceleracion_cinematica(v1, 0., 0., 6., euclidea=False)
print('desacelera = ', desacelera)
recorrido1 = mecanica_fisica.recorrido_cinematica(v0, aceleracion, 10., euclidea=False)
print("recorrido inicial = ", recorrido1)
recorrido2 = mecanica_fisica.recorrido_cinematica(v1, desacelera, 6., euclidea=False)
print("Recorrido final = ", recorrido2)
print("Recorrido total = ", recorrido1 + recorrido2)

escala = np.linspace(0, np.pi/2, 100)
senos = np.array([np.sin(x*np.pi) for x in escala])
cosenos = np.array([[np.cos(x*np.pi)] for x in escala])
Graficas3D.plot_scatter(escala, senos, cosenos, nombre='Seno')
