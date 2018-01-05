from tkinter import *
from tkinter import ttk
import Articulo
import BaseDeDatos
from tkinter import messagebox

class GUIConsultarPrecioDelProducto:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()
        self.master = master
        master.title("PRECIO DEL PRODUCTO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de barra")
        self.labelCodigo.grid(row=0, column=0)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=0, column=1, padx=5, pady=5)

        self.buttonBuscarPrecio = Button(self.master, text="Buscar precio \n del producto", command=self.buscarPrecioDeUnArticulo, width=20, height=3)
        self.buttonBuscarPrecio.grid(row=0, column=2, rowspan=3, padx=10)

        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=5, column=0,columnspan=3)

        self.resultadosObtenidos = Text(self.master, width=40, height=10)
        self.resultadosObtenidos.grid(row=6, column=0, columnspan=3)

    def buscarPrecioDeUnArticulo(self):
        try:
            codigoDeBarrasDelArticuloBuscado = self.intCodigo.get()
            self.baseDeDatos.setComandoSql(
                'SELECT ARTICULOS.CODIGO_DE_BARRA, ARTICULOS.NOMBRE_ARTICULO, ARTICULOS.PRECIO,ARTICULOS.STOCK, MARCAS.NOMBRE_MARCA FROM (ARTICULOS) INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE CODIGO_DE_BARRA ={};'.format(
                    codigoDeBarrasDelArticuloBuscado))
            self.baseDeDatos.ejecutarComandoSQL()
            articuloBuscado = self.baseDeDatos.setElemento()

            encabezado = ["Codigo de Producto", "Nombre/Descripcion", "Precio Por Unidad", "Cantidad ", "Marca"]
            print('|{:<20} '.format(encabezado[0]) + '|{:<30} '.format(encabezado[1]) + '|{:<20} '.format(
                encabezado[2]) + '|{:<9} '.format(encabezado[3]) + '|{:<20}|'.format(encabezado[4]))
            print('|{:<20} '.format(articuloBuscado[0]) + '|{:<30} '.format(articuloBuscado[1]) + '|{:<20} '.format(articuloBuscado[2]) + '|{:<9} '.format(
                articuloBuscado[3]) + '|{:<20}|'.format(articuloBuscado[4]))

        except:
            messagebox.showinfo(parent=self.master, message='NO SE ENCONTRO ARTICULO', icon="error", title="ERROR!", type="ok")

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIConsultarPrecioDelProducto(self.root)
        self.root.mainloop()

root = Tk()
my_gui = GUIConsultarPrecioDelProducto(root)
root.mainloop()