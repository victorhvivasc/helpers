# -*- coding: utf-8 -*-

class NoOne:

    def __init__(self, ):
        raise ValueError('Esta función solo hace calculos para conjunto de datos, no '
                         'para muestras individuales')


class Longitud:

    def __init__(self, comparar, original):
        raise ValueError(f'Se esperaba un conjunto de datos con longitud = {len(original)}, y '
                         f'se recibio un arreglo de longitud = {len(comparar)}')


class Type:

    def __init__(self, comparar, original):
        raise TypeError(f'El typo de dato de cada grupo a comparar debe ser del mismo tipo, se recibio: '
                        f'{type(original)} y {type(comparar)}')
