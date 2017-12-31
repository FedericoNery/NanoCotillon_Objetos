from tkinter import *
from tkinter import ttk

class GUIAgregarMarca:
    def __init__(self, master):
        self.master = master
        master.title("AGREGAR MARCA")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Nombre de Marca")
        self.labelCodigo.grid(row=0, column=1)
        self.labelDescripcion = Label(self.master, text="Descripción")
        self.labelDescripcion.grid(row=1, column=1)
        self.labelPrecio = Label(self.master, text="Precio")
        self.labelPrecio.grid(row=2, column=1)
        self.labelStock = Label(self.master, text="Stock")
        self.labelStock.grid(row=3, column=1)
        self.labelMarca = Label(self.master, text="Marca")
        self.labelMarca.grid(row=4, column=1)
        self.labelArea = Label(self.master, text="Area")
        self.labelArea.grid(row=5, column=1)

        self.stringCodigo = StringVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.stringCodigo)
        self.entryCodigo.grid(row=6, column=1)

        self.stringNombre = StringVar()
        self.entryNombre = ttk.Entry(self.master, textvariable=self.stringNombre)
        self.entryNombre.grid(row=7, column=1)

        self.stringPrecio = StringVar()
        self.entryPrecio = ttk.Entry(self.master, textvariable=self.stringPrecio)
        self.entryPrecio.grid(row=8, column=1)

        self.stringStock = StringVar()
        self.entryStock = ttk.Entry(self.master, textvariable=self.stringStock)
        self.entryStock.grid(row=8, column=1)

        self.l = Listbox(self.master, height=10)
        self.l.grid(row=9, column=1)

        self.spinval = StringVar()
        self.s = Spinbox(self.master, from_=1.0, to=100.0, textvariable=self.spinval)
        self.s.grid(row=10, column=1)

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarMarca(self.root)
        self.root.mainloop()


