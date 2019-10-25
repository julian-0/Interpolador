from tkinter import *

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

raiz.mainloop()

