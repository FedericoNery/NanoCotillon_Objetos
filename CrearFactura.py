from tkinter import *
from tkinter import ttk
import Articulo
import BaseDeDatos

class GUICrearFactura:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()
        self.master = master
        master.title("CREAR FACTURA")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de barra")
        self.labelCodigo.grid(row=0, column=0)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=0, column=1, padx=5, pady=5)

        self.buttonFacturarProducto = Button(self.master, text="Facturar Producto", command=self.facturarProducto, width=15, height=2)
        self.buttonFacturarProducto.grid(row=0, column=2, columnspan=1, padx=5, pady=5, rowspan=2)

        self.facturacion = Text(self.master, width=40, height=10)
        self.facturacion.grid(row=5, column=0, columnspan=3)

        self.buttonFinalizarCompra = Button(self.master, text="Finalizar Compra", command=self.finalizarCompra, width=15, height=2)
        self.buttonFinalizarCompra.grid(row=2, column=2, columnspan=1, padx=5, pady=5, rowspan=2)

        self.buttonQuitarTodo = Button(self.master, text="Quitar Todo", command=self.quitarTodo, width=15, height=2)
        self.buttonQuitarTodo.grid(row=4, column=2, columnspan=1, padx=5, pady=5, rowspan=2)

    def facturarProducto(self):
        pass

    def finalizarCompra(self):
        pass

    def quitarTodo(self):
        pass

    def crearFacturaVersion2():
        articulosFacturados = []
        contador = 0
        idDeUltimaFactura = extraerIDDeLaUltimaFactura()
        nombreDelCliente = ingreso_de_datos.ingresoNombre("Cliente")
        existeCliente = verificarSiExisteCliente(nombreDelCliente)
        if (not existeCliente):
            print("No existe el cliente, debe agregarlo")
            agregarRegistros.agregarCliente()

        validacionSeguirFacturando = True
        while (validacionSeguirFacturando):
            codigoDeBarras = ingreso_de_datos.ingresoCodigoDeBarras()
            existeArticulo = verificarQueExistaElArticulo(codigoDeBarras)
            if (not existeArticulo):
                agregarRegistros.agregarArticulo()

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
                funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
                articuloConsultado = funciones_SQLite.extraerElemento(cursorBaseDeDatos)
                codigoDeBarrasDelArticulo = articuloConsultado[0]
                precioDelArticulo = articuloConsultado[3]

                comandoSQL = 'INSERT INTO ART_FACT(ID_ART,ID_FACT,CANTIDAD,PRECIO) VALUES({},{},{},{});'.format(codigoDeBarrasDelArticulo, str(idDeUltimaFactura),
                                                                                                                stockDeseadoDelArticulo,
                                                                                                                str(precioDelArticulo))
                funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)

                comandoSQL = 'INSERT INTO FACTURAS (ID_CLIENTE) VALUES ((SELECT ID_CLIENTE FROM CLIENTES WHERE NOMBRE = "{}"));'.format(
                    nombreDelCliente)
                funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
                funciones_SQLite.guardarBaseDeDatos(baseDeDatos)

                comandoSQL = 'UPDATE ARTICULOS SET STOCK = (SELECT STOCK FROM ARTICULOS WHERE CODIGO_DE_BARRA = {})-{} WHERE CODIGO_DE_BARRA = {}'.format(
                    codigoDeBarras, stockDeseadoDelArticulo, codigoDeBarras)
                funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
                funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
                contador = contador + 1

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUICrearFactura(self.root)
        self.root.mainloop()


root = Tk()
my_gui = GUICrearFactura(root)
root.mainloop()