from tkinter import *
from sympy import *
class MetodoFINTER:
    dominio = [1,3,5]
    imagen = [2,5,6]
    def printear(self):
        print(self.dominio)
        print(self.imagen)

class Lagrange(MetodoFINTER):
    def obtenerL(self,nroDeL):
        auxDominio = self.dominio[:]
        auxImagen = self.imagen[:]
        #(x-3)*(x-5)

        auxDominio.pop(nroDeL)
        auxImagen.pop(nroDeL)

vf, d, a, vi, t = S('vf d a vi t'.split())
algo = Lagrange()
otraCosa = Eq(vf+2,0)
print (solve(otraCosa))
