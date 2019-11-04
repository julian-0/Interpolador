from Metodos import *
from sympy import *

x = symbols('x')

class MetodoController():
    # TODO agregar las otras clases
    clases = {"Lagrange": Lagrange(), "Newton Gregory progresivo": NewtonGregoryProgresivo(), "Newton Gregory regresivo": int}

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

    def obtenerPasos(self):
        return self.metodo.mostrarPasos()

    def obtenerImagen(self, punto):
        return self.metodo.obtenerValorPara(punto)
