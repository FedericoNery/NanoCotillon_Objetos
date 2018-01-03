from tkinter import *
from tkinter import ttk

class GUIEliminarMarca:
    def __init__(self, master):
        self.master = master
        master.title("ELIMINAR MARCA")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Nombre de Marca")
        self.labelCodigo.grid(row=0, column=1)
        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=1, column=1)

        self.stringCodigo = StringVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.stringCodigo)
        self.entryCodigo.grid(row=6, column=1)

        self.l = Listbox(self.master, height=10)
        self.l.grid(row=9, column=1)

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIEliminarMarca(self.root)
        self.root.mainloop()


