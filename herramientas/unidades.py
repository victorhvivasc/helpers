# -*- coding: utf-8 -*-
# clase para designar el valor y unidades de trabajo
from herramientas.equivalencia import con_m


class Unidades:
    """Clase con la utilidad de asignar dimensionalidad a los valores operados
    incluye sobrecarga de los operadores de suma, resta, multiplicacion y division
    para coordinar el manejo de las unidades
    """

    def __init__(self, valor, dtype='m3/s'):
        """Inicialización del objeto"""
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
        print(mensaje_deleter)

    def __add__(self, other, *args) -> object:
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades(self.valor + other.valor, dtype=other.dtype)
            else:
                raise TypeError(f'No se puede sumar {self.dtype} con {other.dtype}, por favor elija datos con la misma'
                                f'dimensionalidad')
        else:
            raise TypeError(error_diensiones_1)

    def __sub__(self, other) -> object:
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades((self.valor - other.valor), dtype=other.dtype)
            else:
                raise TypeError(f'No se puede sumar {self.dtype} con {other.dtype}, por favor elija datos con la misma'
                                f'dimensionalidad')
        else:
            raise TypeError(error_diensiones_1)

    def __mul__(self, other, simp=False) -> object:
        if isinstance(other, Unidades):
            return self.simplificar(Unidades(self.valor * other.valor, dtype=f"({self.dtype}).({other.dtype})"), con_m)
        else:
            return Unidades(self.valor * other, dtype=f"{self.dtype}")

    def __truediv__(self, other) -> object:
        if isinstance(other, Unidades):
            if self.dtype == other.dtype:
                return Unidades(self.valor/other.valor, dtype='adimensional')
            else:
                return Unidades(self.valor/other.valor, dtype=f'({self.dtype})/({other.dtype})  ')
        else:
            return Unidades(self.valor/other, dtype=self.dtype)

    @staticmethod
    def simplificar(obj, dict):
        if obj.dtype in dict:
            dtype = dict[obj.dtype]
        else:
            dtype = obj.dtype
        return Unidades(obj.valor, dtype=dtype)

    def __str__(self, ) -> str:
        return str(self.valor) + ' ' + self._dtype


error_diensiones_1 = "Para garantizar la dimensionalidad de los datos no se permite sumar datos adimensionales"
mensaje_deleter = 'El dtype no puede ser eliminado para mejorar la coherencia de la información'

if __name__ == '__main__':
    u1 = Unidades(25, dtype='k6')
    u2 = Unidades(5, dtype='k5')
    a = u2 * u1
    print(a)
