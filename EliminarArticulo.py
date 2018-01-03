from tkinter import *
from tkinter import ttk

class GUIEliminarArticulo:
    def __init__(self, master):
        self.master = master
        master.title("ELIMINAR ARTICULO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de Barra")
        self.labelCodigo.grid(row=0, column=1)

        self.stringCodigo = StringVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.stringCodigo)
        self.entryCodigo.grid(row=6, column=1)

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIEliminarArticulo(self.root)
        self.root.mainloop()


