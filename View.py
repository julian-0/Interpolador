from tkinter import ttk
import tkinter as tk
from MetodoController import *

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
        self.combo.current(0)

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
        frame.cargarResultados(self)
        self.controlador.mostrarFrame(VistaPolinomio)


class VistaPolinomio(tk.Frame):

    def __init__(self, padre, controlador):
        tk.Frame.__init__(self, padre)
        Label(self, text="Polinomio interpolante", bg=COLOR_PRINCIPAL, font=FONT_TITULO).pack()
        self.config(bg=COLOR_PRINCIPAL)

        Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL).pack() # Espacio, se me bugueo el grid

        self.lPolinomio = Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lPolinomio.pack()

        # Frame datos
        self.frameDatos = Frame(self, bg=COLOR_PRINCIPAL)
        self.frameDatos.pack()

        self.lMetodo = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lMetodo.grid(row=0, column=0)
        self.lGrado = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lGrado.grid(row=1, column=0)
        self.lEspaciado = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lEspaciado.grid(row=2, column=0)

        Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL).pack() # Espacio, se me bugueo el grid

        # Frame pasos
        self.framePasos = LabelFrame(self, text='Pasos', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.framePasos.pack()

        Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL).pack() # Espacio, se me bugueo el grid

        # Frame calcular en punto
        self.framePunto = LabelFrame(self, text='Especializar en valor', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.framePunto.pack()
        Label(self.framePunto, text="Punto: ", bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=0, column=0)
        self.punto = Entry(self.framePunto)
        self.punto.grid(row=0, column=1)
        self.boton = Button(self.framePunto, text="Calcular", bg="firebrick3", activebackground="darkOrchid4", command= lambda:self.calcularImagen(self.punto.get()))
        self.boton.grid(row=0, column=2)
        self.lImagen = Label(self.framePunto, text="Imagen: ", bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.lImagen.grid(row=1, column=0)
        self.mensajePunto = Label(self.framePunto, text="", bg=COLOR_SECUNDARIO, fg=COLOR_ERROR)
        self.mensajePunto.grid(row=2, column=0, columnspan=3) # Espacio, se me bugueo el grid


        Label(self, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL).pack() # Espacio, se me bugueo el grid

        # Frame botones
        self.frameBotones = Frame(self, bg=COLOR_SECUNDARIO)
        self.frameBotones.pack()

        self.boton = Button(self.frameBotones, text="Alterar valores", bg="firebrick3", activebackground="darkOrchid4",
                            command=lambda: controlador.mostrarFrame(VistaInicial))
        self.boton.grid(row=0, column=0)

        self.boton = Button(self.frameBotones, text="Finalizar", bg="firebrick3", activebackground="darkOrchid4",
                            command=controlador.destroy)
        self.boton.grid(row=0, column=1)

    def cargarResultados(self, padre):
        self.padre = padre
        self.lMetodo['text'] = "Metodo: " + padre.metodoElegido

        self.modelController = MetodoController()
        self.modelController.cargar(padre.dominios, padre.imagenes, padre.metodoElegido)

        self.lPolinomio['text'] = self.modelController.obtenerPolinomio()
        self.lGrado['text'] = "Grado: " + self.modelController.obtenerGrado().__str__()

        self.cargarPasos()

    def cargarPasos(self):
        pasos = self.modelController.obtenerPasos()

        for i, p in enumerate(pasos):
            Label(self.framePasos, text=p, bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=i, column=0)

    def calcularImagen(self, punto):
        self.mensajePunto['text'] = ""

        if self.punto.get().isdigit():
            self.lImagen['text'] = self.modelController.obtenerImagen(punto)
        else:
            self.mensajePunto['text'] = "Ingrese un valor numerico"



if __name__ == '__main__':
    app = AppFinter()
    app.mainloop()