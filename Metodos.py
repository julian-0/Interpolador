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
    def setDominio(self,listaPuntos):
        self.dominio = listaPuntos
    def getImagen(self):
        return self.imagen
    def setImagen(self,listaPuntos):
        self.imagen = listaPuntos
    def obtenerPolinomioInterpolante(self):
        pass
    def mostrarPasos(self):
        pass


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

    def obtenerPolinomioInterpolante(self):
        polinomio = 0
        for i in range(len(self.dominio)):
            polinomio = polinomio + self.imagen[i] * self.obtenerL(i)
        return polinomio
    def mostrarPasos(self):#Por ahora printea pero podria devolver un String
        print("-----------Metodo de Lagrange-----------")
        #Mostrar cada Li(Xi)
        for i in range(len(self.dominio)):
            foo = "L"+str(i)
            print(foo," = ",self.obtenerL(0))
        print("-------------")
        polinomio = self.obtenerPolinomioInterpolante()
        print("Polinomio de grado ",degree(polinomio)," obtenido: ")
        print(polinomio.as_poly())

algo = Lagrange()
poli = algo.obtenerPolinomioInterpolante()
print("El polinomio obtenido es: ", poli)
print ("La imagen aproximada en 7.5 es: ",poli.subs(x, 7.5))
algo.mostrarPasos();

"""
otraCosa = (x + y)*(y - 2.2*z)
otraCosa.as_poly() #Hace la distributiva
print (otraCosa.as_poly())
"""
