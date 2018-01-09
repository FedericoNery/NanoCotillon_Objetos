from tkinter import *
from tkinter import ttk

class GUIEliminarMarca:
    def __init__(self, master):
        self.master = master
        master.title("ELIMINAR MARCA")
        master.geometry("565x500+400+50")


    def eliminarMarca(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIEliminarMarca(self.root)
        self.root.mainloop()

"""
root = Tk()
my_gui = GUIEliminarCliente(root)
root.mainloop()
"""
