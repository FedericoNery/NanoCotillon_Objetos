from tkinter import *
from tkinter import ttk
import Articulo
import BaseDeDatos
import Producto
import ListaDeProductos
import AgregarCliente
import AgregarArticulo

class GUICrearFactura:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.master = master
        master.title("CREAR FACTURA")
        master.geometry("600x500+400+50")

        self.labelNombreCliente = Label(self.master, text="Cliente")
        self.labelNombreCliente.grid(row=3, column=0)

        self.stringNombreCliente = StringVar()
        self.entryNombreCliente = ttk.Entry(self.master, textvariable=self.stringNombreCliente)
        self.entryNombreCliente.grid(row=3, column=1, padx=5, pady=5)

        self.buttonFacturarProducto = Button(self.master, text="Facturar Producto", command=self.facturarProducto, width=15, height=2)
        self.buttonFacturarProducto.grid(row=0, column=0, columnspan=1, padx=5, pady=5, rowspan=2)

        self.buttonFinalizarCompra = Button(self.master, text="Finalizar Compra", command=self.finalizarCompra, width=15, height=2)
        self.buttonFinalizarCompra.grid(row=0, column=2, columnspan=1, padx=5, pady=5, rowspan=2)

        self.buttonQuitarTodo = Button(self.master, text="Quitar Todo", command=self.quitarTodo, width=15, height=2)
        self.buttonQuitarTodo.grid(row=0, column=1, columnspan=1, padx=5, pady=5, rowspan=2)

        self.articulosFacturados = []
        self.filaProducto = 5
        self.columnaProducto = 0
        self.productosAgregados = ListaDeProductos.ListaDeProductos(self.filaProducto, self.master)

    def facturarProducto(self):
        self.productosAgregados.agregarProducto()

    def finalizarCompra(self):
        pass

    def quitarTodo(self):
        pass

    def extraerIDDeLaUltimaFactura(self):
        self.baseDeDatos.setComandoSql('SELECT MAX(ID_FACTURA) FROM FACTURAS;')
        self.baseDeDatos.ejecutarComandoSQL()
        self.baseDeDatos.setElemento()
        idDeUltimaFactura = self.baseDeDatos.elemento
        if (idDeUltimaFactura[0] == None):
            idDeUltimaFactura = 1
        else:
            idDeUltimaFactura = idDeUltimaFactura[0] + 1
        return idDeUltimaFactura

    def verificarQueExistaElArticulo(self,codigoDeBarra):
        self.baseDeDatos.setComandoSql('SELECT * FROM ARTICULOS WHERE CODIGO_DE_BARRA = {}'.format(codigoDeBarra))
        self.baseDeDatos.ejecutarComandoSQL()
        self.baseDeDatos.setElemento()
        articuloBuscado = self.baseDeDatos.elemento
        if (articuloBuscado == None):
            return False
        else:
            return True

    def verificarStockDisponible(self,codigoDeBarra, stockDeseado):
        self.baseDeDatos.setComandoSql('SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {};'.format(codigoDeBarra))
        self.baseDeDatos.ejecutarComandoSQL()
        self.baseDeDatos.setElemento()
        stockDisponible = self.baseDeDatos.elemento[0]
        if (stockDisponible < stockDeseado):
            print("Solo quedan disponibles {} unidades".format(stockDisponible))
            return False
        else:
            return True

    def verificarSiExisteCliente(self,nombreCliente):
        self.baseDeDatos.setComandoSql("SELECT * FROM CLIENTES;")
        self.baseDeDatos.ejecutarComandoSQL()
        self.baseDeDatos.setTabla()
        for cliente in self.baseDeDatos.tabla:
            if (cliente[1] == nombreCliente):
                return True
        return False

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUICrearFactura(self.root)
        self.root.mainloop()
"""
    def crearFactura(self):
        contador = 0
        self.idDeUltimaFactura = self.extraerIDDeLaUltimaFactura()
        self.nombreDelCliente = self.stringNombreCliente.get()
        existeCliente = self.verificarSiExisteCliente(self.nombreDelCliente)
        if (not existeCliente):
            print("No existe el cliente, debe agregarlo")
            AgregarCliente.GUIAgregarCliente.crearVentana()

        validacionSeguirFacturando = True
        while (validacionSeguirFacturando):
            codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
            existeArticulo = verificarQueExistaElArticulo(codigoDeBarras)
            if (not existeArticulo):
                AgregarArticulo.GUIAgregarArticulo.crearVentana()
            print("Ingrese stock deseado")
            stockDeseadoDelArticulo = ingreso_de_datos.ingresoCantidadDeStock()
            stockDeseadoDelArticulo = int(stockDeseadoDelArticulo)
            sePoseeElStockDeseado = verificarStockDisponible(codigoDeBarras, stockDeseadoDelArticulo)

            if (sePoseeElStockDeseado):
                articulosFacturados.append((codigoDeBarras, stockDeseadoDelArticulo))
                validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()
            else:
                validacionSeguirFacturando = deseaSeguirIngresandoArticulosALaFactura()

        if (len(articulosFacturados) == 0):
            print("No se realizo factura alguna")
        else:
            while (contador < (len(articulosFacturados))):
                comandoSQL = 'SELECT ARTICULOS.CODIGO_DE_BARRA,ARTICULOS.NOMBRE_ARTICULO,MARCAS.ID_MARCA, ARTICULOS.PRECIO FROM ARTICULOS,MARCAS WHERE ARTICULOS.CODIGO_DE_BARRA = {}'.format(
                    codigoDeBarras)
                self.baseDeDatos.ejecutarComandoSQL()
                articuloConsultado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
                codigoDeBarrasDelArticulo = articuloConsultado[0]
                precioDelArticulo = articuloConsultado[3]

                comandoSQL = 'INSERT INTO ART_FACT(ID_ART,ID_FACT,CANTIDAD,PRECIO) VALUES({},{},{},{});'.format(codigoDeBarrasDelArticulo, str(idDeUltimaFactura),
                                                                                                                stockDeseadoDelArticulo,
                                                                                                                str(precioDelArticulo))
                self.baseDeDatos.ejecutarComandoSQL()

                comandoSQL = 'INSERT INTO FACTURAS (ID_CLIENTE) VALUES ((SELECT ID_CLIENTE FROM CLIENTES WHERE NOMBRE = "{}"));'.format(nombreDelCliente)
                self.baseDeDatos.ejecutarComandoSQL()


                comandoSQL = 'UPDATE ARTICULOS SET STOCK = (SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {})-{} WHERE CODIGO_DE_BARRA = {}'.format(
                    codigoDeBarras, stockDeseadoDelArticulo, codigoDeBarras)
                self.baseDeDatos.ejecutarComandoSQL()
                self.baseDeDatos.guardarBaseDeDatos()
                contador = contador + 1
"""

root = Tk()
my_gui = GUICrearFactura(root)
root.mainloop()