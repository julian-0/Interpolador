from tkinter import *
from tkinter import ttk
from Metodos import *

"""
def agregarPunto():
    years.set(ordenada.get())
    print(ordenada.get())

raiz=Tk()
raiz.title("TP matematica superior")
raiz.resizable(1,1)
raiz.config(bg="light green")


miFrame=Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="650",height="350")

miFrame.config(relief="groove",bd=35)

Label(miFrame,text = "Bienvenido!").grid(row=1,column=0)
Label(miFrame,text = "Ingrese los puntos").grid(row=2,column=0)


# Creating a Frame Container
frame = LabelFrame(miFrame, text = 'Ingrese un punto')
frame.grid(row = 3, column = 0, columnspan = 3, pady = 20)

# Name Input

years = StringVar()

Label(frame, text = 'Ordenada: ').grid(row = 4, column = 0)
ordenada = Entry(frame)
#self.name.focus()
ordenada.grid(row = 4, column = 1)

# Price Input
Label(frame, text = 'Imagen: ').grid(row = 5, column = 0)
imagen = Entry(frame)
imagen.grid(row = 5, column = 1)

# Button Add Product
boton = Button(frame, text = "Agregar", command = agregarPunto).grid(row = 6, column = 0)

Label(frame, text = 'Su ordenada: ').grid(row = 7, column = 0)
Label(frame, text = 'Su imagen: ').grid(row = 8, column = 0)

lo = Label(frame,textvariable=years).grid(row = 7, column = 1)
li = Label(frame).grid(row = 8, column = 1)

algo = Lagrange()
algo.printear()
algo.obtenerL(1)

raiz.mainloop()
"""
##############################################3
class AppFinter():

    ordenadas=[]
    imagenes=[]

    def __init__(self):
        raiz=Tk()
        self.raiz=raiz
        raiz.title("TP matematica superior")
        raiz.resizable(1,1)
        raiz.config(bg="light green")


        miFrame=Frame()
        miFrame.pack()
        miFrame.config(bg="red")
        miFrame.config(width="650",height="350")

        miFrame.config(relief="groove",bd=35)

        Label(miFrame,text = "Bienvenido!").grid(row=1,column=0)
        Label(miFrame,text = "Ingrese los puntos").grid(row=2,column=0)


        # Frame Container
        frame = LabelFrame(miFrame, text = 'Ingrese un punto')
        frame.grid(row = 3, column = 0, columnspan = 3, pady = 20)

        # Ordenada Input
        self.years = StringVar()

        Label(frame, text = 'Ordenada: ').grid(row = 4, column = 0)
        self.ordenada = Entry(frame)
        self.ordenada.grid(row = 4, column = 1)

        # Imagen Input
        Label(frame, text = 'Imagen: ').grid(row = 5, column = 0)
        self.imagen = Entry(frame)
        self.imagen.grid(row = 5, column = 1)

        # Boton agregar
        boton = Button(frame, text = "Agregar", command = self.agregarPunto,bg="blue",activebackground="cyan").grid(row = 6, column = 0,columnspan = 3)

        # Tabla
        self.tabla = ttk.Treeview(miFrame,height = 10, columns = 2)
        self.tabla.grid(row = 9, column = 0)
        self.tabla.heading('#0', text = 'Ordenada', anchor = CENTER)
        self.tabla.heading('#1', text = 'Imagen', anchor = CENTER)

    def agregarPunto(self):
        self.ordenadas.append(self.ordenada.get())
        self.imagenes.append(self.imagen.get())
        self.tabla.insert('', 'end', text = self.ordenada.get(), values = self.imagen.get())


if __name__ == '__main__':
    app = AppFinter()
    app.raiz.mainloop()
