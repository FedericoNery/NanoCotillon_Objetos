import Producto
from tkinter import Button

class ListaDeProductos:
    def __init__(self, fila, master):
        self.lista = []
        self.fila = fila
        self.master = master
        self.buttonQuitarTodo = Button(self.master, text="Quitar Todo", command=self.quitarTodo, width=15, height=2)
        self.buttonQuitarTodo.grid(row=0, column=1, columnspan=1, padx=5, pady=5, rowspan=2)

    def agregarProducto(self):
        miProducto = Producto.Producto(self.fila, self.master)
        self.lista.append(miProducto)
        self.fila = self.fila + 2

    def eliminarProducto(self,producto):
        indice = self.lista.index(producto)
        self.lista[indice].quitarProducto()
        self.lista.remove(producto)

    def quitarTodo(self):
        try:
            for producto in self.lista[:]:
                self.eliminarProducto(producto)
        except:
            pass