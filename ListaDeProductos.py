import Producto

class ListaDeProductos:
    def __init__(self, fila, master):
        self.lista = []
        self.fila = fila
        self.master = master

    def agregarProducto(self):
        miProducto = Producto.Producto(self.fila, self.master)
        self.lista.append(miProducto)
        self.fila = self.fila + 2

    def eliminarProducto(self,producto):
        indice = self.lista.index(producto)
        self.lista[indice].quitarProducto()
        self.lista.remove(producto)