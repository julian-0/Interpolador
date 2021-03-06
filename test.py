import unittest
from Metodos import *

class TestMyModule(unittest.TestCase):
    def test_Lagrange(self):
        metodo = Lagrange()
        metodo.setDominio([5,10,20,30])
        metodo.setImagen([1.519,1.307,1.002,0.796])
        self.assertEqual(metodo.obtenerValorPara(7.5), 1.40710937500000)

    def test_Newton_Coseno52(self):
        metodo = NewtonGregoryProgresivo()
        metodo.setDominio([45,50,55,60])
        metodo.setImagen([0.7071,0.6427,0.57357,0.5000])
        polNewton = metodo.obtenerPolinomioInterpolante()
        polNewton = polNewton.subs(t,(x-45)/5)
        self.assertEqual(round(polNewton.subs(x,52),5),0.6156)

    def test_Newton_Seno52(self):
        metodo = NewtonGregoryProgresivo()
        metodo.setDominio([45,50,55,60])
        metodo.setImagen([0.7071,0.7660,0.8192,0.8660])
        polNewton = metodo.obtenerPolinomioInterpolante()
        polNewton = polNewton.subs(t,(x-45)/5)
        self.assertEqual(round(polNewton.subs(x,52),6),0.788003)

    def test_Newton_Polinomio(self):
        algo = NewtonGregoryRegresivo()
        algo.setDominio([1,3,4,5,7])
        algo.setImagen([1,3,13,37,151])
        e = 1.0+(x-1.0)+3.0*(x-1.0)*(x-3.0)+1.0*(x-1.0)*(x-3.0)*(x-4.0)
        self.assertEqual(algo.obtenerPolinomioInterpolante().as_poly(),e.as_poly())

if __name__ == "__main__":
   unittest.main()
