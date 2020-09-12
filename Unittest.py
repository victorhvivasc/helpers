import unittest
from conversiones import escalar, convert_live
from herramientas.unidades import Unidades


class MyTestCase(unittest.TestCase):

    def test_Unidades(self):
        a = Unidades(valor=1, dtype='m')
        self.assertEqual(a.valor, 1, msg='Test unidades valor')
        self.assertEqual(a.dtype, 'm', msg='Test unidades dtype')

    def test_escalar(self):
        m = Unidades(0.3048, 'm')
        pies = escalar(m, 'pies')
        self.assertEqual(pies.dtype, 'pies', msg='test_escalar dtype')
        self.assertEqual(round(pies.valor, 4), 1, msg='test_escalar valor')

    def test_decorador(self):
        @convert_live(u_s='km')
        def sumar(a: Unidades, b: Unidades):
            return a + b
        uno = Unidades(5, dtype='m')
        dos = Unidades(5, dtype='m')
        suma = sumar(uno, dos)
        self.assertEqual(suma.valor, 0.01, msg='Test decorador valor')
        self.assertEqual(suma.dtype, 'km', msg='Test decorador dtype')


if __name__ == '__main__':
    unittest.main()
