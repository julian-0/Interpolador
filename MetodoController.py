from Metodos import *
from sympy import *

x = symbols('x')

class MetodoController():
    # TODO agregar las otras clases
    clases = {"Lagrange": Lagrange(), "Newton Gregory progresivo": int, "Newton Gregory regresivo": int}

    def cargar(self, dominio, imagenes, metodoPol):
        self.metodo = self.clases[metodoPol]
        self.metodo.setDominio(dominio)
        self.metodo.setImagen(imagenes)
        self.polinomio = self.metodo.obtenerPolinomioInterpolante()
        self.grado = degree(self.polinomio)
        # self.pasos = calcularPasos()

    def obtenerPolinomio(self):
        return self.polinomio

    def obtenerGrado(self):
        return self.grado

    # TODO sacar esto
    def obtenerPasos(self):
        return ["L0(X) = (X-2)(X-5)  L0(X0) = 4", "L1(X) = (X-1)(X-5)  L1(X1) = -3", "L2(X) = (X-1)(X-2)  L2(X2) = 12"]
