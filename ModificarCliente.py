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

        self.radioButtonPorNombre = Radiobutton(master, text="Por Nombre", value=1, function=self.selectorBuscarPorNombre)
        self.radioButoonPorLista = Radiobutton(master, text="Por Lista", value=2, function=self.selectorBuscarPorLista)
        self.radioButtonPorNombre.grid(row=4, column=0)
        self.radioButoonPorLista.grid(row=5, column=0)

    def selectorBuscarPorNombre(self):
        pass

    def selectorBuscarPorLista(self):
        pass

    def buscarClientesPorNombre(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarCliente(self.root)
        self.root.mainloop()
