from tkinter import Tk, Label, Button
import AgregarArticulo

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("NANO COTILLON")

        self.label = Label(self.master, text=self.textoVentanaPrincipalEncabezado())
        self.label.grid(row = 0, column = 1)

        self.agregarArticulo_button = Button(self.master, text="1. Agregar Articulo", command = self.agregarArticulo, width = 20, height = 3)
        self.agregarArticulo_button.grid(row = 1, column = 0)

        self.agregarArticulo_button = Button(self.master, text="2. Agregar Cliente", command=self.agregarCliente, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=1)

        self.agregarArticulo_button = Button(self.master, text="3. Agregar Marca", command=self.agregarMarca, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=2)

        self.agregarArticulo_button = Button(self.master, text="4. Eliminar Articulo", command=self.eliminarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=2, column=0)

        self.agregarArticulo_button = Button(self.master, text="5. Eliminar Cliente", command=self.eliminarCliente, width=20, height=3)
        self.agregarArticulo_button.grid(row=2, column=1)

        self.agregarArticulo_button = Button(self.master, text="6. Eliminar Marca", command=self.eliminarMarca, width=20, height=3)
        self.agregarArticulo_button.grid(row=2, column=2)

        self.agregarArticulo_button = Button(self.master, text="7. Modificar Articulo", command=self.modificarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=3, column=0)

        self.agregarArticulo_button = Button(self.master, text="8. Modificar Cliente", command=self.modificarCliente, width=20, height=3)
        self.agregarArticulo_button.grid(row=3, column=1)

        self.agregarArticulo_button = Button(self.master, text="9. Modificar Marca", command=self.modificarMarca, width=20, height=3)
        self.agregarArticulo_button.grid(row=3, column=2)

        self.agregarArticulo_button = Button(self.master, text="10. Crear Factura", command=self.crearFactura, width=20, height=3)
        self.agregarArticulo_button.grid(row=4, column=0)

        self.agregarArticulo_button = Button(self.master, text="11. Imprimir Factura \n por nro de factura", command=self.imprimirPorNumDeFact, width=20, height=3)
        self.agregarArticulo_button.grid(row=4, column=1)

        self.agregarArticulo_button = Button(self.master, text="12. Crear Nueva \nBase De Datos", command=self.crearBaseDeDatos, width=20, height=3)
        self.agregarArticulo_button.grid(row=7, column=2)

        self.agregarArticulo_button = Button(self.master, text="13. Consultar Precio\n del producto", command=self.consultarPrecio, width=20, height=3)
        self.agregarArticulo_button.grid(row=5, column=0)

        self.agregarArticulo_button = Button(self.master, text="14. Consultar por\n Palabra Clave", command=self.consultarPorPalabra, width=20, height=3)
        self.agregarArticulo_button.grid(row=5, column=1)

        self.agregarArticulo_button = Button(self.master, text="15. Consultar por\n Area", command=self.consultarPorArea, width=20, height=3)
        self.agregarArticulo_button.grid(row=5, column=2)

        self.agregarArticulo_button = Button(self.master, text="16. Consultar por\n Fecha de Actualizacion", command=self.consultarPorFechaDeAct, width=20, height=3)
        self.agregarArticulo_button.grid(row=6, column=0)

        self.agregarArticulo_button = Button(self.master, text= "17. Consultar Productos \nSin Stock", command=self.consultarProductosSinStock, width=20, height=3)
        self.agregarArticulo_button.grid(row=6, column=1)

        self.agregarArticulo_button = Button(self.master, text="18. Consultar Total\n Del Dia", command=self.consultarTotalDelDia, width=20, height=3)
        self.agregarArticulo_button.grid(row=6, column=2)

        self.agregarArticulo_button = Button(self.master, text="19. Imprimir última\n factura", command=self.imprimirUltimaFactura, width=20, height=3)
        self.agregarArticulo_button.grid(row=4, column=2)

        self.agregarArticulo_button = Button(self.master, text= "20. Consultar Venta\n Anual", command=self.consultarVentaAnual, width=20, height=3)
        self.agregarArticulo_button.grid(row=7, column=0)

        self.agregarArticulo_button = Button(self.master, text="21. Consultar Venta\n Mensual", command=self.consultarVentaMensual, width=20, height=3)
        self.agregarArticulo_button.grid(row=7, column=1)


    def agregarArticulo(self):
       AgregarArticulo.GUIAgregarArticulo.crearVentana(self)

    def agregarCliente(self):
        pass

    def agregarMarca(self):
        pass

    def eliminarArticulo(self):
        pass

    def eliminarCliente(self):
        pass

    def eliminarMarca(self):
        pass

    def modificarArticulo(self):
        pass

    def modificarCliente(self):
        pass

    def modificarMarca(self):
        pass

    def crearFactura(self):
        pass

    def imprimirPorNumDeFact(self):
        pass

    def crearBaseDeDatos(self):
        pass

    def consultarPrecio(self):
        pass

    def consultarPorPalabra(self):
        pass

    def consultarPorArea(self):
        pass

    def consultarPorFechaDeAct(self):
        pass

    def consultarProductosSinStock(self):
        pass

    def consultarTotalDelDia(self):
        pass

    def imprimirUltimaFactura(self):
        pass

    def consultarVentaAnual(self):
        pass

    def consultarVentaMensual(self):
        pass

    def textoVentanaPrincipalEncabezado(self):
        return """NANO COTILLON
    Sistema de consulta y registro de los productos
    Creado por : Federico Nery
    """

root = Tk()
root.geometry("565x500+400+50")
my_gui = MyFirstGUI(root)
root.mainloop()