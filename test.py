import unittest
from Metodos import *

class TestMyModule(unittest.TestCase):
    def test_1(self):
        metodo = Lagrange()
        metodo.setDominio([5,10,20,30])
        metodo.setImagen([1.519,1.307,1.002,0.796])
        self.assertEqual(metodo.obtenerValorPara(7.5), 1.40710937500000)

if __name__ == "__main__":
   unittest.main()
