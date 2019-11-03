from tkinter import ttk
import tkinter as tk
from Metodos import *

COLOR_PRINCIPAL = "dodger blue"
COLOR_SECUNDARIO = "sky blue"
COLOR_ERROR = "red"
FONT_TITULO = ("Verdana", 15)
FONT_PRINCIPAL = ("Arial", 11)


class AppFinter(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Finter")
        self.resizable(1, 1)
        self.config(bg="light green")

        self.container = Frame()
        self.container.pack(side="top", fill="both", expand=True)
        self.container.config(bg=COLOR_PRINCIPAL)
        self.container.config(width="650", height="350")
        self.container.config(relief="groove", bd=35)

        self.frames = {}

        for Vista in (VistaInicial, VistaPolinomio):
            frame = Vista(self.container, self)
            self.frames[Vista] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrarFrame(VistaInicial)

    def mostrarFrame(self, vista):
        frame = self.frames[vista]
        frame.tkraise()


class VistaInicial(tk.Frame):
    dominios = []
    imagenes = []
    metodoElegido = ""

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
        Label(frame, text='Dominio: ', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=4, column=0)
        self.dominio = Entry(frame)
        self.dominio.grid(row=4, column=1)

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
        self.tabla.heading('#0', text='Dominio', anchor=tk.CENTER)
        self.tabla.heading('#1', text='Imagen', anchor=tk.CENTER)

        # Seleccion de metodo
        frameMetodo = LabelFrame(self, text='Seleccione un metodo', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        frameMetodo.grid(row=10, column=0, pady=5)
        self.combo = ttk.Combobox(frameMetodo, state="readonly", width=24, font=FONT_PRINCIPAL)
        self.combo.pack()
        self.combo["values"] = ["Lagrange", "Newton Gregory progresivo", "Newton Gregory regresivo"]
        self.combo.current(1)

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
        return len(self.dominio.get()) != 0 and len(self.imagen.get()) != 0

    def numericos(self):
        return self.dominio.get().replace('.', '', 1).isdigit() and self.imagen.get().replace('.', '', 1).isdigit()

    def agregarPunto(self):
        self.mensaje['text'] = ''
        if self.validar():
            self.dominios.append(float(self.dominio.get()))
            self.imagenes.append(float(self.imagen.get()))
            self.tabla.insert('', 'end', text=self.dominio.get(), values=self.imagen.get())
        self.limpiarInputs()

    def limpiarInputs(self):
        self.dominio.delete(0, 'end')
        self.imagen.delete(0, 'end')

    def calcularPolinomio(self):
        self.metodoElegido = self.combo.get()
        frame = self.controlador.frames[VistaPolinomio]
        frame.cargarPolinomio(self)
        self.controlador.mostrarFrame(VistaPolinomio)


class VistaPolinomio(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self, padre)
        Label(self, text="Polinomio interpolante", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=1, column=0)

        self.boton = Button(self, text="Volver", bg="firebrick3", activebackground="darkOrchid4",
                            command=lambda: controlador.mostrarFrame(VistaInicial))
        self.boton.grid(row=2, column=0)

        self.lMetodo = Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_TITULO)
        self.lMetodo.grid(row=3, column=0)

        Label(self, text="Dominios", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=4, column=0)
        Label(self, text="Imagenes", bg=COLOR_PRINCIPAL, font=FONT_TITULO).grid(row=4, column=1)

    def cargarPolinomio(self, padre):
        self.padre = padre
        self.lMetodo['text'] = "Metodo: " + padre.metodoElegido
        """"
        if padre.metodoElegido == "Lagrange":
            self.cargarVistaLagrange()
        else:
            self.cargarVistaNewtonGregory()
        """


if __name__ == '__main__':
    app = AppFinter()
    app.mainloop()
