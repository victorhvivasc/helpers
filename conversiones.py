# -*- coding: utf-8 -*-
from herramientas.unidades import Unidades
from herramientas.valores import *


def convert_live(u_s: str):
    """Decorador que convierte las unidades de una funcion en tiempo de ejecución, siempre que la relación de
    conversión haya sido incluida en el archivo valores.py.
    Cuidado, la conversion se hace sobre todos los argumentos que sean instancia Unidades de la función, no asi sobre
    constantes incluidas en el cuerpo de la misma
    Ejemplo:
    @convert_live(u_s='pies')
    def sumar(a, b):
        return a+b
    uno = Unidades(5, dtype='m')
    dos = Unidades(5, dtype='m')
    sumar(uno, dos)
    :return 32.8084 pies
    """
    def convert_to_mks(f):
        def envoltura(*args):
            aux = []
            for i in args:
                if isinstance(i, Unidades):
                    aux.append(escalar(i, u_s=u_s))
            return f(*aux)
        return envoltura
    return convert_to_mks


def escalar(valor, u_s: str, u_e: str = None) -> Unidades:
    """Funcion para redimensionar segun las escalas preestablecidas en el documento valores.py
    valor: int, float, class Unidades, indiferentemente del valor de entrada la salida sera del type class Unidades
    u_s: Unidad a la cual se desea hacer la conversión de escala.
    u_e: default None, cuando el parametro 'valor' suministrado es del type Unidades se identifica automaticamente el
        tipo de datos de entrada, en caso contrario debe suministrarse

    Ejemplo 1:
    numero = 25
    escala = escalar(numero, u_e='m', u_s='km')
    :return 0.025 km

    Ejemplo 2:
    numero = Unidades(25, dtype='m')
    escala = escalar(numero, u_s='km')
    :return 0.025 km
    """
    if isinstance(valor, Unidades):
        dtypes = str(valor.dtype)+'-'+u_s
        valor.dtype = u_s
        return valor*escalas[dtypes]
    else:
        valor = valor*escalas[u_e+'-'+u_s]
        return Unidades(valor, dtype=u_s)


if __name__ == '__main__':
    numero = Unidades(25, dtype='m')
    escala = escalar(numero, u_s='km')
    print(escala, type(escala))

    @convert_live(u_s='km')
    def sumar(a: Unidades, b: Unidades):
        return a+b
    uno = Unidades(5, dtype='m')
    dos = Unidades(5, dtype='m')
    print(sumar(uno, dos, 3))
