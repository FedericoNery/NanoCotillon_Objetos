from tkinter import *
from tkinter import ttk

class GUIModificarCliente:
    def __init__(self, master):
        self.master = master
        master.title("MODIFICAR CLIENTE")
        master.geometry("565x500+400+50")

        self.labelNombreCliente = Label(self.master, text="Nombre del Cliente")
        self.labelNombreCliente.grid(row=0, column=1)

        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=1, column=1)

        self.l = Listbox(self.master, height=10)
        self.l.grid(row=9, column=1)

        self.spinval = StringVar()
        self.s = Spinbox(self.master, from_=1.0, to=100.0, textvariable=self.spinval)
        self.s.grid(row=10, column=1)

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarCliente(self.root)
        self.root.mainloop()
