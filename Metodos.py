from tkinter import *
from sympy import *
x, y, z, t = symbols('x y z t')

class MetodoFINTER:
    dominio = [5,10,20,30]
    imagen = [1.519,1.307,1.002,0.796]
    def printear(self):
        print(self.dominio)
        print(self.imagen)

    def getDominio(self):
        return self.dominio

class Lagrange(MetodoFINTER):
    def obtenerL(self,nroDeL):
        auxDominio = self.dominio[:]
        auxImagen = self.imagen[:]
        auxDominio.pop(nroDeL)
        #auxImagen.pop(nroDeL)
        e = 1
        f = 1
        for i in range(len(auxDominio)):
            e = e * (x-auxDominio[i])
        for i in range(len(auxDominio)):
            f = f*(self.dominio[nroDeL] - auxDominio[i])
        return e/f

algo = Lagrange()
polinomio = 0
for i in range(len(algo.getDominio() )):
    polinomio = polinomio + algo.imagen[i] * algo.obtenerL(i)

print (polinomio.subs(x, 7.5))
"""
otraCosa = (x + y)*(y - 2.2*z)
otraCosa.as_poly() #Hace la distributiva
print (otraCosa.as_poly())
"""
