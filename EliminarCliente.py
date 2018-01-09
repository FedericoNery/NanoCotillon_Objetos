from tkinter import *
from tkinter import messagebox

class GUIEliminarCliente:
    def __init__(self, master):
        self.master = master
        master.title("ELIMINAR CLIENTE")
        master.geometry("565x500+400+50")

        self.labelNombreCliente = Label(self.master, text="Nombre del Cliente")
        self.labelNombreCliente.grid(row=0, column=0)

        self.stringClienteABuscar = StringVar()
        self.entryClienteABuscar = Entry(self.master, textvariable=self.stringClienteABuscar)
        self.entryClienteABuscar.grid(row=1, column=0)

        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=0, column=1)

    def buscarClientePorPalabra(self):
        pass

    def eliminarCliente(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIEliminarCliente(self.root)
        self.root.mainloop()
        messagebox.showinfo(parent=self.master, message='INGRESE EL NOMBRE O PARTE \n DE UN CLIENTE PARA ELIMINAR', icon="info", title="ATENCION", type="ok")

"""
root = Tk()
my_gui = GUIEliminarCliente(root)
root.mainloop()
"""
