import numpy as np
from herramientas import validate


def distancia_euclidea(x, y=0):
    """Sean x e y dos puntos en el espacio, se calcula la distancia entre los dos puntos
    ejemplo:
    x = np.array([0, 1])
    y = np.array([1, 0])
    teorema_pitagoras(x, y)
    >>> 1.41421356
    """
    x = validate.numpy_or_list(x)
    y = validate.numpy_or_list(y)
    return np.sqrt(sum(np.square(y-x)))


def velocidad_promedio(tiempo, distancia=None, x=None, y=None):
    """Dada una distancia a recorrer y un tiempo determinado se estima la velocidad
    utilizada, la distancia en metros y el tiempo en segundos, puede suministrar dos puntos
    en lugar de la distancia y se determinará la distancia euclidea entre ellas.
    ejemplos:
    velocidad(60, 60)
    >>> 1
    a = [15, 25, 48]
    b = [30, 50, 96]
    velocidad(60, x=a, y=b)
    >>> 0.936
    """
    if not distancia:
        distancia = distancia_euclidea(x, y)
    return distancia/tiempo


def velocidad_cinematica(x0=None, x1=None, t0=0, t1=0, v0=None, v1=None, euclidea=True):
    """Dadas dos posiciones y tiempos conocidos en el movimiento de una particula se estima la velocidad
    en ese tramo.  Si no se suministran los tiempos, se asume que se desea calcular los mismos y la funcion
    cambia a modo calculo de tiempo y no velocidad
    x0: posición inicial dada en metros.
    x1: posición final dada en metros.
    t0: tiempo inicial dado en segundos.
    t1: tiempo final dado en segundos.
    v0: velocidad inicial.
    v1: velocidad final.
    euclidea: Sí False retornara un vector, sí True devuelve el modulo del vector

    nota: si los cuerpos se estan aproximando entre si, se debe asumir 1 de las velocidades negativas
    """
    x0 = validate.numpy_or_list(x0)
    x1 = validate.numpy_or_list(x1)
    if t1 == 0 and t0 == 0:
        v0 = validate.numpy_or_list(v0)
        v1 = validate.numpy_or_list(v1)
        resultado = (x1-x0)/(v1-v0)
    else:
        if euclidea:
            dx = distancia_euclidea(x0, x1)
        else:
            dx = x1 - x0
        resultado = dx/(t1 - t0)
    return resultado


def aceleracion_cinematica(v0, v1, t0, t1, euclidea=False):
    """Dado el cambio de velocidad en una trayectoria y los tiempos medidos de estos cambios
    se calcula la aceleracion
    v0: velocidad inicial
    v1: segunda velocidad
    t0: tiempo inicial
    t1: tiempo final
    euclidea: Sí False retornara un vector, sí True devuelve el modulo del vector
    tiempo en segungos, velocidad en metros/segundos
    x=x0+v0t+12at2
    """
    if euclidea:
        dv = distancia_euclidea(v0, v1)
    else:
        v0 = validate.numpy_or_list(v0)
        v1 = validate.numpy_or_list(v1)
        dv = v1 - v0
    dt = t1 - t0
    return dv/dt


def recorrido_cinematica(v0, a, t1, x0=0, euclidea=True):
    """Dada la aceleración una velocidad y un tiempo determinado se calcula la distancia recorrida"""
    v0 = validate.numpy_or_list(v0)
    a = validate.numpy_or_list(a)
    x0 = validate.numpy_or_list(x0)
    x = x0 + v0*t1 + 0.5*a*np.square(t1)
    if euclidea:
        return np.sqrt(sum(np.square(x)))
    else:
        return x


def fuerza_newton(masa, aceleracion, euclinea=True):
    """Recibe una aceleracion en vector o modulo, una masa interviniente y devuelve
    la fuerza relacionada a la interacción
    masa: expresada en kilogramos
    acelaración: expresada en metros/segundos2
    euclidea: Si False devuelve el vector relacionado a la fuerza, si True devuelve la magnitud de la
    fuerza"""
    if euclinea:
        aceleracion = (np.sqrt(sum(np.square(aceleracion))))
    return masa*aceleracion


def momento(brazo, fuerza, euclidea=True):
    """Dado una distancia vectorial o no (brazo) y una fuerza aplicada al extremo del brazo se
    calcula el momento/torque aplicado sobre el punto final del brazo
    brazo: dado en metros
    fuerza: dada en Kg.m/s2
    euclidea: Si True devuelve el modulo del momento si False devuelve el vector momento
    """
    if isinstance(brazo, float) or isinstance(brazo, int):
        brazo = [brazo]
    if isinstance(fuerza, float) or isinstance(fuerza, int):
        fuerza = [fuerza]
    brazo = validate.numpy_or_list(brazo)
    fuerza = validate.numpy_or_list(fuerza)
    if euclidea:
        brazo = (np.sqrt(sum(np.square(brazo))))
        fuerza = (np.sqrt(sum(np.square(fuerza))))
    return brazo*fuerza


def velocidad_tangencial(velocidad, radio):
    """Dada la velocidad angular w y el radio de acción se calcula la velocidad tangencial
    velocidad: velocidad angular dada en RPM
    radio: dado en metros
    """
    w = 2 * np.pi * velocidad / 60
    return w * radio


def velocidad_angular(velocidad, radio, rpm=False):
    """Dado los vectores velocidad y radio a un punto en una trayectoria se calcula el
    modulo de la velocidad angular
    velocidad: expresada en m/s
    radio: expresado en m
    rpm: Si desea el resultado expresado en rpm cambiar a True
    w expresado en radianes
    """
    velocidad = validate.numpy_or_list(velocidad)
    radio = validate.numpy_or_list(radio)
    if not rpm:
        w = velocidad/radio
    else:
        w = (velocidad/radio)*(30/np.pi)
    return w


def aceleracion_angular_media(w0, w, t0, t):
    w0 = validate.numpy_or_list(w0)
    w = validate.numpy_or_list(w)
    dt = t - t0
    return (w - w0)/dt
