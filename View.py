from tkinter import ttk
import tkinter as tk
from Metodos import *

COLOR_PRINCIPAL = "dodger blue"
COLOR_SECUNDARIO = "sky blue"
COLOR_ERROR = "red"
FONT_TITULO = ("Verdana", 13)
FONT_PRINCIPAL = ("Arial", 11)


class AppFinter(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Finter")
        self.resizable(1, 1)
        self.config(bg="light green")

        container = Frame()
        container.pack(side="top", fill="both", expand=True)
        container.config(bg=COLOR_PRINCIPAL)
        container.config(width="650", height="350")
        container.config(relief="groove", bd=35)

        self.frames = {}

        for Vista in (VistaInicial, VistaPolinomio):
            frame = Vista(container, self)
            self.frames[Vista] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrarFrame(VistaInicial)

    def mostrarFrame(self, vista):
        frame = self.frames[vista]
        frame.tkraise()


class VistaInicial(tk.Frame):
    ordenadas = []
    imagenes = []

    def __init__(self, padre, controller):
        tk.Frame.__init__(self, padre)
        self.controlador = controller
        self.config(bg=COLOR_PRINCIPAL)

        Label(self, text="Bienvenido!", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=1, column=0)

        # Frame Container
        frame = LabelFrame(self, text='Ingrese puntos', font=FONT_PRINCIPAL)
        frame.grid(row=3, column=0)
        frame.config(bg=COLOR_SECUNDARIO)

        # Ordenada Input
        Label(frame, text='Ordenada: ', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=4, column=0)
        self.ordenada = Entry(frame)
        self.ordenada.grid(row=4, column=1)

        # Imagen Input
        Label(frame, text='Imagen: ', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=5, column=0)
        self.imagen = Entry(frame)
        self.imagen.grid(row=5, column=1)

        # Boton agregar
        boton = Button(frame, text="Agregar", command=self.agregarPunto, bg="turquoise", activebackground="cyan")
        boton.grid(row=6, column=0, columnspan=2)

        # Mensaje resultado
        self.mensaje = Label(frame, text='', fg=COLOR_ERROR, bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.mensaje.grid(row=8, column=0, columnspan=2)

        # Tabla
        self.tabla = ttk.Treeview(self, height=10, columns=2)
        self.tabla.grid(row=9, column=0)
        self.tabla.heading('#0', text='Ordenada', anchor=tk.CENTER)
        self.tabla.heading('#1', text='Imagen', anchor=tk.CENTER)

        # Seleccion de metodo
        frameMetodo = LabelFrame(self, text='Seleccione un metodo', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        frameMetodo.grid(row=10, column=0, pady=5)
        self.combo = ttk.Combobox(frameMetodo, state="readonly", width=24, font=FONT_PRINCIPAL)
        self.combo.pack()
        self.combo["values"] = ["Lagrange", "Newton Gregory progresivo", "Newton Gregory regresivo"]
        self.combo.set("Lagrange")

        # Boton calcular
        botonCalcular = Button(self, text="Calcular", bg="firebrick3", activebackground="darkOrchid4",
                               command=lambda: self.calcularPolinomio())
        botonCalcular.grid(row=11, column=0)

    def validar(self):
        if not self.completos():
            self.mensaje['text'] = 'Los campos deben estar completos'
            return False
        if not self.numericos():
            self.mensaje['text'] = 'Los valores deben ser numéricos'
            return False
        return True

    def completos(self):
        return len(self.ordenada.get()) != 0 and len(self.imagen.get()) != 0

    def numericos(self):
        return self.ordenada.get().replace('.', '', 1).isdigit() and self.imagen.get().replace('.', '', 1).isdigit()

    def agregarPunto(self):
        self.mensaje['text'] = ''
        if self.validar():
            self.ordenadas.append(float(self.ordenada.get()))
            self.imagenes.append(float(self.imagen.get()))
            self.tabla.insert('', 'end', text=self.ordenada.get(), values=self.imagen.get())
        self.limpiarInputs()

    def limpiarInputs(self):
        self.ordenada.delete(0, 'end')
        self.imagen.delete(0, 'end')

    def calcularPolinomio(self):
        frame = self.controlador.frames[VistaPolinomio]
        frame.cargarPolinomio(self)
        self.controlador.mostrarFrame(VistaPolinomio)


class VistaPolinomio(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self, padre)
        Label(self, text="Vista polinomio", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=1, column=0)

        boton = Button(self, text="Volver", bg="firebrick3", activebackground="darkOrchid4",
                       command=lambda: controlador.mostrarFrame(VistaInicial))
        boton.grid(row=2, column=0)

    def cargarPolinomio(self, padre):
        self.padre = padre

        Label(self, text="Ordenadas", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=3, column=0)
        i = 0
        for o in padre.ordenadas:
            Label(self, text=o, bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=4 + i, column=0)
            i = i + 1

        Label(self, text="Ordenadas", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=3, column=1)
        j = 0
        for img in padre.imagenes:
            Label(self, text=img, bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=4 + j, column=1)
            j = j + 1


if __name__ == '__main__':
    app = AppFinter()
    app.mainloop()
