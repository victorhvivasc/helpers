# ESTE DOCUMENTO PUEDE SERVIR DE AYUDA COMO HELPER EN APLICACIONES ESTADISTICAS
# LOS RESULTADOS SERAN RAPIDOS Y CONFIABLES, AUNQUE EL USUARIO ES EL UNICO RESPONSABLE
# DE LOS RESULTADOS OBTENIDOS DEL USO DE LA MISMA ASI COMO TAMBIEN ES ACREEDOR DE LOS BENEFICIOS
# QUE PUEDA OBTENER.
#
# Python 3.7
# numpy == 1.19

import numpy as np
import raises


def sse(comparar, original):
    """Calcula la suma de los errores al cuadrado"""
    if type(comparar) == type(original):
        if len(comparar) == len(original):
            if len(comparar) >= 2:
                if type(comparar) == list:
                    y_true = np.array(original)
                    y_pred = np.array(comparar)
                    return np.square(y_pred - y_true)
                else:
                    return np.square(comparar - original)
            else:
                raises.NoOne()
        else:
            raises.Longitud(comparar, original)
    else:
        raises.Type(comparar, original)


def mse(comparar, original) -> float:
    """Puede recibir un array, una lista, retorna el error cuadratico medio
    mse = (y_pred-y_true)**2
    ejemplo:
    a = [1, 2]
    b = [5, 3]
    print(mse(a, b))
    >8.5
    """
    return sse(comparar, original).mean()


def rmse(comparar, original) -> float:
    """Calcula la raiz del error cuadratico medio, se apoya de la funcion
    Puede recibir un array, una lista, retorna el error cuadratico medio
    mse = (y_pred-y_true)**2
    ejemplo:
    a = [1, 2]
    b = [5, 3]
    print(rmse(a, b))
    >2.9154759
    """
    return np.sqrt(mse(comparar, original))


def accuracy(comparar, original) -> float:
    """Evalua 2 grupos de datos y devuelve un valor que representa la proporcion de igualdad entre ambos
    conjuntos de datos, es una medida de la precision de una predicción
    recibe listas o array y retorna un flotante
    ejemplo:
    a = [1, 2]
    b = [5, 3]
    >
    """
    if type(comparar) == type(original):
        if len(comparar) == len(original):
            if len(comparar) >= 2:
                if type(comparar) == list:
                    y_true = np.array(original)
                    y_pred = np.array(comparar)
                    return sum(y_true == y_pred)/len(y_true)
                else:
                    return sum(original == comparar)/len(original)
            else:
                raises.NoOne()
        else:
            raises.Longitud(comparar, original)
    else:
        raises.Type(comparar, original)


def mae(comparar, original) -> float:
    """Calcula el error absoluto medio a partir de 2 conjuntos de datos que pueden ser listas o array"""
    if type(comparar) == type(original):
        if len(comparar) == len(original):
            if len(comparar) >= 2:
                if type(comparar) == list:
                    y_true = np.array(original)
                    y_pred = np.array(comparar)
                    return np.abs((y_pred - y_true)).mean()
                else:
                    return np.abs((comparar - original)).mean()
            else:
                raises.NoOne()
        else:
            raises.Longitud(comparar, original)
    else:
        raises.Type(comparar, original)
