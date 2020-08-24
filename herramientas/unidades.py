# -*- coding: utf-8 -*-
# clase para designar el valor y unidades de trabajo

class Unidades:

    def __init__(self, valor, dtype='m3/s'):
        self.valor = valor
        self._dtype = dtype

    @property
    def dtype(self, ):
        return self._dtype

    @dtype.setter
    def dtype(self, valor):
        self._dtype = valor

    @dtype.deleter
    def dtype(self, ):
        print('el dtype no puede ser eliminado para mejorar la coherencia de la información')

    def __add__(self, other):
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades((self.valor + other.valor), dtype=other.dtype)
            else:
                raise TypeError(f'No se puede sumar {self.dtype} con {other.dtype}, por favor elija datos con la misma'
                                f'dimensionalidad')
        else:
            raise TypeError(error_diensiones_1)

    def __sub__(self, other):
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades((self.valor - other.valor), dtype=other.dtype)
            else:
                raise TypeError(f'No se puede sumar {self.dtype} con {other.dtype}, por favor elija datos con la misma'
                                f'dimensionalidad')
        else:
            raise TypeError(error_diensiones_1)

    def __mul__(self, other):
        if isinstance(other, Unidades):
            return Unidades(self.valor * other.valor, dtype=f"({self.dtype}).({other.dtype})")
        else:
            return Unidades(self.valor * other, dtype=f"{self.dtype}")

    def __truediv__(self, other):
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades(self.valor/other.valor, dtype='adimensional')
            else:
                return Unidades(self.valor/other.valor, dtype=f'({self.dtype})/({other.dtype})  ')
        else:
            return Unidades(self.valor/other, dtype=self.dtype)

    def __str__(self, ):
        return str(self.valor) + ' ' + self._dtype


error_diensiones_1 = "Para garantizar la dimensionalidad de los datos no se permite sumar datos adimensionales"
