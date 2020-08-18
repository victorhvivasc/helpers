import numpy as np
from herramientas import raises


def validar_datos(comparar, original):
    if type(comparar) == type(original):
        if len(comparar) == len(original):
            if len(comparar) >= 2:
                if isinstance(comparar, list):
                    ok = True
                    original = np.array(original)
                    comparar = np.array(comparar)
                    return original, comparar, ok
                else:
                    ok = True
                    return original, comparar, ok
            else:
                raises.NoOne()
        else:
            raises.Longitud(comparar, original)
    else:
        raises.Type(comparar, original)


def numpy_or_list(x):
    if isinstance(x, float) or isinstance(x, int):
        x = [x]
    if type(x) == list:
        return np.array(x)
    else:
        return x
