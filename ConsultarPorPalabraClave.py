from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Articulo
import BaseDeDatos

class GUIConsultarPorPalabraClave:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()

        self.master = master
        master.title("PRODUCTOS POR PALABRA CLAVE")
        master.geometry("450x400+450+100")

        self.labelPalabraClave = Label(self.master, text="Palabra clave \n para buscar producto")
        self.labelPalabraClave.grid(row=0, column=0,padx=5,pady=5)

        self.labelResultado = Label(self.master, text="Resultado de Busqueda")
        self.labelResultado.grid(row=3,column = 0,columnspan=3)

        self.stringPalabra = StringVar()
        self.entryPalabra = ttk.Entry(self.master, textvariable=self.stringPalabra)
        self.entryPalabra.grid(row=0, column=1,padx=5,pady=5)

        self.buttonBuscarPorPalabra = Button(self.master, text="Buscar Por \n Palabra Clave", command=self.buscarPorPalabraClave, width=15, height=2)
        self.buttonBuscarPorPalabra.grid(row=0, column=2,columnspan=1,padx=5,pady=5, rowspan=2)

        self.resultadosObtenidos = Text(self.master, width=40, height=10)
        self.resultadosObtenidos.grid(row=5,column=0,columnspan=3)

    def buscarPorPalabraClave(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIConsultarPorPalabraClave(self.root)
        self.root.mainloop()


root = Tk()
my_gui = GUIConsultarPorPalabraClave(root)
root.mainloop()