from tkinter import *
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
        auxDominio.pop(nroDeL)
        auxImagen.pop(nroDeL)
        print(auxDominio)
        print(auxImagen)


raiz=Tk()
raiz.title("TP matematica superior")
raiz.resizable(1,1)
#raiz.geometry("640x480")
raiz.config(bg="light green")

miFrame=Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="650",height="350")

miFrame.config(relief="groove",bd=35)

algo = Lagrange()
algo.printear()
algo.obtenerL(1)

raiz.mainloop()
