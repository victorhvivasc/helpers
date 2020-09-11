# from herramientas import validate
from herramientas.unidades import Unidades
from herramientas.valores import *


def convert_to_mks(f):
    """Decorador de metodo para la clase Unidades, aplicado directamente sobre una operación hace la conversion
    en tiempo real """
    def envoltura(*args, **kwargs):
        correcto = True
        for i in args:
            if isinstance(i, Unidades):
                i.valor = i.valor * equivalencia[i.dtype][0]
                i.dtype = equivalencia[i.dtype][1]
            else:
                correcto = False
        if not correcto:
            raise TypeError('Metodo solo util para la clase Unidades')
        return f(*args, *kwargs)
    return envoltura


def mks_ingles(valor: (float, int), u_e: str) -> Unidades:
    """Recibe un numero flotante o entero, una unidad de entrada, se hace la conversion a la unidad correspondiente
    de salida, de sistema internacional a ingles y viceversa, NO SIRVE PARA CAMBIO DE ESCALAS EJEMPLO DE m A cm
    a = longitud(25, 'm')
    :return 82.021 pie
    """
    valor = valor * equivalencia[u_e][0]
    return Unidades(valor, dtype=equivalencia[u_e][1])


def escalar(valor: (float, int), u_e: str, u_s: str) -> Unidades:
    """Para cambiar escala entre dimensiones de la misma unidad"""
    valor = valor*escalas[u_e+'-'+u_s]
    return Unidades(valor, dtype=u_s)


print(escalar(25, 'm2', 'pies2'))
