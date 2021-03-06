from tkinter import ttk
import tkinter as tk
from VerticalScrolledFrame import *
from MetodoController import *

COLOR_PRINCIPAL = "dodger blue"
COLOR_SECUNDARIO = "sky blue"
COLOR_ERROR = "red"
FONT_TITULO = ("Times", 15, "bold")
FONT_PRINCIPAL = ("Arial", 11)
FONT_PRINCIPAL_1 = ("Arial", 12)
FONT_PRINCIPAL_SUB = ("Arial", 12, "underline")
FONT_PRINCIPAL_BOLD = ("Arial", 11, "bold")


class AppFinter(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Finter")
        self.resizable(width=False, height=False)
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
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[vista]
        frame.grid()


class VistaInicial(tk.Frame):
    metodoElegido = ""

    def __init__(self, padre, controller):
        tk.Frame.__init__(self, padre)
        self.controlador = controller
        self.config(bg=COLOR_PRINCIPAL)

        Label(self, text="Bienvenido!", bg=COLOR_PRINCIPAL, font=FONT_TITULO).pack()

        # Frame Container
        frame = LabelFrame(self, text='Ingrese puntos:', font=FONT_PRINCIPAL_1)
        frame.pack()
        frame.config(bg=COLOR_SECUNDARIO, bd=0)

        # Ordenada Input
        Label(frame, text='Dominio: ', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=3, column=0)
        self.dominio = Entry(frame)
        self.dominio.grid(row=3, column=1, pady=5, padx=5)

        # Imagen Input
        Label(frame, text='Imagen: ', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=4, column=0)
        self.imagen = Entry(frame)
        self.imagen.grid(row=4, column=1)

        # Boton agregar
        boton = Button(frame, text="Agregar", command=self.agregarPunto, bg="springGreen2", bd=1,
                       activebackground="springGreen3")
        boton.grid(row=5, column=0, columnspan=2, pady=5)

        # Mensaje resultado
        self.mensaje = Label(frame, text='', fg=COLOR_ERROR, bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.mensaje.grid(row=6, column=0, columnspan=2)

        # Tabla
        self.tabla = ttk.Treeview(self, height=10, columns=2)
        self.tabla.pack()
        self.tabla.heading('#0', text='Dominio', anchor=tk.CENTER)
        self.tabla.heading('#1', text='Imagen', anchor=tk.CENTER)

        # Eliminar punto seleccionado
        botonEliminar = Button(self, text="Eliminar punto", bg="firebrick2", bd=1, activebackground="firebrick3",
                               command=lambda: self.eliminarPunto())
        botonEliminar.pack()

        # Seleccion de metodo
        frameMetodo = LabelFrame(self, text='Seleccione un metodo:', bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        frameMetodo.config(bg=COLOR_SECUNDARIO, bd=0)
        frameMetodo.pack()
        self.combo = ttk.Combobox(frameMetodo, state="readonly", width=24, font=FONT_PRINCIPAL)
        self.combo.pack()
        self.combo["values"] = ["Lagrange", "Newton Gregory progresivo", "Newton Gregory regresivo"]
        self.combo.current(0)

        # Boton calcular
        botonCalcular = Button(self, text="Calcular", bg="springGreen2", bd=1, activebackground="springGreen3",
                               command=lambda: self.calcularPolinomio())
        botonCalcular.pack()

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
        return esDigito(self.dominio.get()) and esDigito(self.imagen.get())

    def agregarPunto(self):
        self.mensaje['text'] = ''
        if self.validar():
            self.tabla.insert('', 'end', text=self.dominio.get(), values=self.imagen.get())
        self.limpiarInputs()

    def getImagenes(self):
        imagenes = []
        for child in self.tabla.get_children():
            imagenes.append(float(self.tabla.item(child)["values"][0]))
        return imagenes

    def getDominios(self):
        dominio = []
        for child in self.tabla.get_children():
            dominio.append(float(self.tabla.item(child)["text"]))
        return dominio

    def limpiarInputs(self):
        self.dominio.delete(0, 'end')
        self.imagen.delete(0, 'end')

    def calcularPolinomio(self):
        if self.hayMasDeUnPunto():
            self.metodoElegido = self.combo.get()
            frame = self.controlador.frames[VistaPolinomio]
            frame.cargarResultados(self)
            self.controlador.mostrarFrame(VistaPolinomio)
        else:
            self.mensaje['text'] = "Debe haber al menos dos puntos"

    def hayMasDeUnPunto(self):
        return len(self.tabla.get_children()) > 1

    def eliminarPunto(self):
        selected_item = self.tabla.selection()[0]
        self.tabla.delete(selected_item)


class VistaPolinomio(tk.Frame):

    def __init__(self, padre, controlador):
        self.polinomioAnterior = None
        self.controlador = controlador

        tk.Frame.__init__(self, padre)
        self.vista = self.configurarVista()


    def configurarVista(self):
        self.scrollPrincipal = VerticalScrolledFrame(parent=self, alto=480)
        self.scrollPrincipal.pack()
        self.scrollPrincipal.config(bg=COLOR_PRINCIPAL)
        self.scrollPrincipal.interior.config(bg=COLOR_PRINCIPAL)

        Label(self.scrollPrincipal.interior, text="Polinomio interpolante", bg=COLOR_PRINCIPAL, pady=5,
              font=FONT_TITULO).pack()
        self.config(bg=COLOR_PRINCIPAL)

        Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL,
              font=FONT_PRINCIPAL).pack()  # Espacio, se me bugueo el grid

        self.lPolinomio = Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL,  wraplength=800)
        self.lPolinomio.pack() #modifique arriba

        # Frame datos
        self.frameDatos = Frame(self.scrollPrincipal.interior, bg=COLOR_PRINCIPAL)
        self.frameDatos.pack()

        self.lMetodo = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lMetodo.grid(row=0, column=0)
        self.lGrado = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lGrado.grid(row=1, column=0)
        self.lEspaciado = Label(self.frameDatos, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lEspaciado.grid(row=2, column=0)

        Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL,
              font=FONT_PRINCIPAL).pack()  # Espacio, se me bugueo el grid

        # Frame pasos
        self.framePasos = LabelFrame(self.scrollPrincipal.interior, text='Pasos:', bg=COLOR_SECUNDARIO,
                                     font=FONT_PRINCIPAL_BOLD)
        self.framePasos.pack()
        self.labelsPasos = []
        self.scroll = VerticalScrolledFrame(parent=self.framePasos, alto=200)
        self.scroll.pack()
        self.scroll.interior.config(bg=COLOR_SECUNDARIO)

        Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL,
              font=FONT_PRINCIPAL, wraplength=800).pack()  # Espacio, se me bugueo el grid

        # Frame calcular en punto
        self.framePunto = LabelFrame(self.scrollPrincipal.interior, text='Especializar en valor', bg=COLOR_SECUNDARIO,
                                     bd=0,
                                     font=FONT_PRINCIPAL_BOLD, padx=5)
        self.framePunto.pack()
        Label(self.framePunto, text="Punto: ", bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL).grid(row=0, column=0)
        self.punto = Entry(self.framePunto)
        self.punto.grid(row=0, column=1, padx=5)
        self.boton = Button(self.framePunto, text="Calcular", bd=1, bg="springGreen2", activebackground="springGreen3",
                            command=lambda: self.calcularImagen(self.punto.get()))
        self.boton.grid(row=0, column=2)
        self.lImagen = Label(self.framePunto, text="Imagen: ", bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL)
        self.lImagen.grid(row=1, column=0)
        self.mensajePunto = Label(self.framePunto, text="", bg=COLOR_SECUNDARIO, fg=COLOR_ERROR)
        self.mensajePunto.grid(row=2, column=0, columnspan=3)  # Espacio, se me bugueo el grid

        Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL,
              font=FONT_PRINCIPAL).pack()  # Espacio, se me bugueo el grid

        # Frame botones
        self.frameBotones = Frame(self.scrollPrincipal.interior, bg=COLOR_PRINCIPAL)
        self.frameBotones.pack()

        self.boton = Button(self.frameBotones, text="Alterar valores", bd=1, bg="firebrick2",
                            activebackground="firebrick3",
                            command=lambda: self.controlador.mostrarFrame(VistaInicial))
        self.boton.grid(row=0, column=0, padx=10)

        self.boton = Button(self.frameBotones, text="Finalizar", bd=1, bg="firebrick2", activebackground="firebrick3",
                            command=self.controlador.destroy)
        self.boton.grid(row=0, column=1)

        self.lCambio = Label(self.scrollPrincipal.interior, text="", bg=COLOR_PRINCIPAL, font=FONT_PRINCIPAL)
        self.lCambio.pack()
        return self.scrollPrincipal

    def cargarResultados(self, padre):
        self.vista.destroy()
        self.vista = self.configurarVista()

        self.padre = padre
        self.lMetodo['text'] = "Metodo: " + padre.metodoElegido

        self.modelController = MetodoController()
        self.modelController.cargar(padre.getDominios(), padre.getImagenes(), padre.metodoElegido)

        self.lPolinomio['text'] = self.modelController.obtenerPolinomio()
        if self.polinomioAnterior is not None:
            if self.cambioPolinomio():
                self.lCambio['text'] = "Cambio: Si"
            else:
                self.lCambio['text'] = "Cambio: No"
        self.polinomioAnterior = self.lPolinomio['text']

        self.lGrado['text'] = "Grado: " + self.modelController.obtenerGrado().__str__()
        self.lEspaciado['text'] = "Equiespaciado: " + self.modelController.esEquiespaciado()

        self.cargarPasos()

    def cambioPolinomio(self):
        return self.lPolinomio['text'] != self.polinomioAnterior

    def limpiarPasos(self):
        for paso in self.labelsPasos:
            paso.destroy()

    def cargarPasos(self):
        self.limpiarPasos()

        pasos = self.modelController.obtenerPasos()
        for i, p in enumerate(pasos):
            paso = Label(self.scroll.interior, text=p, bg=COLOR_SECUNDARIO, font=FONT_PRINCIPAL, wraplength=800)
            paso.pack()
            self.labelsPasos.append(paso)

    def calcularImagen(self, punto):
        self.mensajePunto['text'] = ""

        if esDigito(self.punto.get()):
            self.lImagen['text'] = self.modelController.obtenerImagen(punto)
        else:
            self.mensajePunto['text'] = "Ingrese un valor numerico"


def esDigito(expresion):
    return expresion.replace('.', '', 1).replace('-', '', 1).isdigit()


if __name__ == '__main__':
    app = AppFinter()
    app.mainloop()
