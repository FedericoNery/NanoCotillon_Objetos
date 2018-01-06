from tkinter import *
import Articulo

class Producto:
    def __init__(self, filaProducto, master):
        self.miArticulo = Articulo.Articulo()
        self.miFilaDelProducto = filaProducto
        self.labelCodigoProducto = Label(master, text="Codigo")
        self.labelCodigoProducto.grid(row=filaProducto, column=0)

        self.intCodigoProducto = IntVar()
        self.entryCodigoProducto = Entry(master, textvariable=self.intCodigoProducto)
        self.entryCodigoProducto.grid(row=filaProducto, column = 1)

        self.labelStockDeseado = Label(master, text="Cantidad")
        self.labelStockDeseado.grid(row=filaProducto, column=2)

        self.intStockDeseado = IntVar()
        self.entryStockDeseado = Entry(master, textvariable=self.intStockDeseado)
        self.entryStockDeseado.grid(row=filaProducto, column=3)

        self.buttonQuitarProducto = Button(master, text="Quitar", command=self.quitarProducto, width=10, height=1)
        self.buttonQuitarProducto .grid(row=filaProducto, column=4, rowspan=1)

    def quitarProducto(self):
        self.labelCodigoProducto.grid_forget()
        self.entryCodigoProducto.grid_forget()
        self.labelStockDeseado.grid_forget()
        self.entryStockDeseado.grid_forget()
        self.buttonQuitarProducto.grid_forget()
