# -*- coding: utf-8 -*-
# herramientas para resolucion de problemas de mecánica de fluidos
from herramientas.unidades import Unidades
import mecanica_fisica


def caudal_volume(volumen=None, tiempo=None, type_volumen='m3', type_tiempo='s'):
    """Calculo de caudal en funcion del volumen desplazado y el tiempo medido
    volumen: volumen que se encuentra en circulacion, se tiene predefinido en m³(metros cubicos).
    type_volumen: unidades en que se sumistra el dato volumen.
    tiempo: periodo de tiempo en el que circula el volumen dada, predefinido en s(segundos).
    type_tiempo: Unidades en que se suministra el dato del tiempo.
    vector: si es True convierte el dato suministrado en un numpy array para seguir operando
    ejemplo:
    v = 5
    t = 2
    q = caudal(volumen=v, tiempo=t)
    print(q)
    >>>2.5 'm3/s'
    """
    if isinstance(tiempo, (float, int)):
        if isinstance(volumen, (float, int)):
            volumen = Unidades(volumen, dtype=type_volumen)
        else:
            volumen = mecanica_fisica.distancia_euclidea(volumen)
            volumen = Unidades(volumen, dtype=type_volumen)
        tiempo = Unidades(tiempo, dtype=type_tiempo)
        #q = Unidades(volumen.valor/tiempo.valor, dtype=f"{volumen.dtype}/{tiempo.dtype}")
        return volumen/tiempo
    else:
        raise ValueError('No considero el tiempo como un vector.')


def caudal_area(area=None, velocidad=None, type_area='m2', type_velocidad='m/s2'):
    """Cálculo del caudal en función de la velocidad y el area transversal
    area: default m2 referidos al area de la seccin por la cual circula fluido.
    velocidad: default m/s2 referido a la velocidad medida a la cual se desplaza el fluido
    """
    if isinstance(area, (float, int)) and isinstance(velocidad, (float, int)):
        area = Unidades(area, dtype=type_area)
        velocidad = Unidades(velocidad, type_velocidad)
        return area*velocidad


def presion(fuerza=None, area=None, type_area='m2', type_fuerza='N'):
    """Calculo de la presion ejercida sobre una superficie"""
    if isinstance(fuerza, (float, int)) and isinstance(area, (float, int)):
        fuerza = Unidades(fuerza, dtype=type_fuerza)
        area = Unidades(area, dtype=type_area)
        return fuerza/area


