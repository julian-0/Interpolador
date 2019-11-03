from Metodos import *


class MetodoController():
    # TODO agregar las otras clases
    clases = {"Lagrange": Lagrange(), "Newton Gregory progresivo": int, "Newton Gregory regresivo": int}

    def obtenerPolinomio(self, dominio, imagenes, metodoPol):
        metodo = self.clases[metodoPol]
        metodo.setDominio(dominio)