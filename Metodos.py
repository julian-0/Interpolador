from tkinter import *
from sympy import *
from funcionesNewton import *
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
    def obtenerValorPara(self,K):
        polinomio = self.obtenerPolinomioInterpolante()
        print ("La imagen aproximada en",K," es: ",polinomio.subs(x, K))
        return polinomio.subs(x,K) #Para el test.Se puede sacar

class NewtonGregoryProgresivo(MetodoFINTER):
    def obtenerPolinomioInterpolante(self):
        matrizN = obtenerMatriz(self.imagen,self.dominio)
        polNewton = matrizN[0][0]

        for i in range (1,len(matrizN[0])):
            #print("saco de la matriz: ",matrizN[0][i])
            polNewton += matrizN[0][i]*self.gradoX(i)
        return polNewton


    def gradoX(self,nro):
        pol = 1
        cant = nro-1
        pol = pol * (x-self.dominio[cant])
        while(cant >= 1):
            cant = cant-1
            pol = pol * (x-self.dominio[cant])
        return pol

    def mostrarPasos(self):
        print("-----------Metodo de Newton Progresivo-----------")
        pasos = []
        paso1 = "Paso 1: Calculo de las diferencias finitas:\n"
        pasos.append(paso1)
        #Mostrar cada diferencia(Xi)
        diferencias = obtenerPasosCalculo(self.imagen,self.dominio)
        for i in range(len(diferencias)):
            print(diferencias[i])
            pasos.append(diferencias[i])
        pasos.append("Obteniendose la siguiente matriz: \n")
        matrizN = obtenerMatriz(self.imagen,self.dominio)
        for i in range(len(self.dominio)):
            print(matrizN[i])
            pasos.append(matrizN[i])
        polinomio = self.obtenerPolinomioInterpolante()
#        print("Polinomio de grado ",degree(polinomio)," obtenido: ")
#        print(polinomio.as_poly())
        pasos.append("Paso 2: Reemplazamos en la formula: \n")
        cadena = ""
        for i in range (1,len(matrizN[0])):
            print("a: ",str(matrizN[0][i]))
            cadena += "a"+str(i-1)+"= "+str(matrizN[0][i])
        pasos.append(cadena)
        pasos.append(str(polinomio.as_poly) )
        return pasos

class NewtonGregoryRegresivo(MetodoFINTER):
    def obtenerPolinomioInterpolante(self):
        matrizN = obtenerMatriz(self.imagen,self.dominio)
        polNewton = matrizN[len(self.imagen)-1][0]

        for i in range (1,len(matrizN[0])):
        #   print("saco de la matriz: ",matrizN[len(self.imagen)-1-i][i])
            polNewton += matrizN[len(self.imagen)-1-i][i]*self.gradoX(i)

        return polNewton
    def gradoX(self,nro):
        dominio = self.dominio[::-1]
        pol = 1
        cant = nro-1
        pol = pol * (x-dominio[cant])
        while(cant >= 1):
            cant = cant-1
            pol = pol * (x-dominio[cant])
        return pol

    def mostrarPasos(self):
        print("-----------Metodo de Newton Regresivo-----------")
        pasos = []
        paso1 = "Paso 1: Calculo de las diferencias finitas:\n"
        pasos.append(paso1)
        #Mostrar cada diferencia(Xi)
        diferencias = obtenerPasosCalculo(self.imagen,self.dominio)
        for i in range(len(diferencias)):
        #    print(diferencias[i])
            pasos.append(diferencias[i])
        pasos.append("Obteniendose la siguiente matriz: \n")
        matrizN = obtenerMatriz(self.imagen,self.dominio)
        for i in range(len(self.dominio)):
        #    print(matrizN[i])
            pasos.append(matrizN[i])
        polinomio = self.obtenerPolinomioInterpolante()
#        print("Polinomio de grado ",degree(polinomio)," obtenido: ")
#        print(polinomio.as_poly())
        pasos.append("Paso 2: Reemplazamos en la formula: \n")
        cadena = ""
        for i in range (1,len(matrizN[0])):
        #    print("a: ",matrizN[len(self.imagen)-1-i][i])
            cadena += "a"+str(i-1)+"= "+str(matrizN[len(self.imagen)-1-i][i])
        pasos.append(cadena)
        pasos.append(str(polinomio.as_poly) )
        return pasos



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
    def mostrarPasos(self):
        print("-----------Metodo de Lagrange-----------")
        pasos = []
        paso1 = "Paso 1: Calculo de los L(x) correspondientes:\n"
        #Mostrar cada Li(Xi)
        for i in range(len(self.dominio)):
            foo = "L"+str(i)
            print(foo," = ",self.obtenerL(i))
            paso1 += (foo+" = " + str(self.obtenerL(i))+"\n" )
        print("-------------")
        pasos.append(paso1)
        polinomio = self.obtenerPolinomioInterpolante()
        print("Polinomio de grado ",degree(polinomio)," obtenido: ")
        print(polinomio.as_poly())
        pasos.append("Paso 2: Reemplazamos en la formula: ")
        pasos.append(str(polinomio.as_poly) )
        return pasos



"""
algo = NewtonGregoryProgresivo()
algo.setDominio([0,2,3,5,6])
algo.setImagen([0,8,27,125,216])
algo.mostrarPasos()
print("-----")
#algo = NewtonGregoryRegresivo()
algo.setDominio([0,2,3,5,6])
algo.setImagen([0,8,27,125,216])
esto = algo.mostrarPasos()
for i in range (len(esto)):
    print(esto[i])

e = 1.0+(x-1.0)+3.0*(x-1.0)*(x-3.0)+1.0*(x-1.0)*(x-3.0)*(x-4.0)
e2 = 151.0+57*(x-7)+11*(x-7)*(x-5)+1*(x-7)*(x-5)*(x-4)
"""