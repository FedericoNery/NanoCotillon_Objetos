from six.moves import tkinter as tk
import AgregarArticulo

class UI(tk.Frame):
    """Docstring."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.numeroColumna = 0
        self.numeroFila = 0
        self.parent.title("NANO COTILLON")
        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=1)
        self.parent.columnconfigure(2, weight=1)
        self.etiqueta = tk.Label(self.parent,text = self.textoVentanaPrincipalEncabezado(),justify = "center").grid(row = 0,column = 1,sticky="nsew")
        self.listaDeBotones = self.generarBotones()

    def textoVentanaPrincipalEncabezado(self):
        return """NANO COTILLON
    Sistema de consulta y registro de los productos
    Creado por : Federico Nery
    """

    def generarBotones(self):
        listaNombres = [
            "1. Agregar Articulo",
            "2. Agregar Cliente",
            "3. Agregar Marca",
            "4. Eliminar Articulo",
            "5. Eliminar Cliente",
            "6. Eliminar Marca",
            "7. Modificar Articulo",
            "8. Modificar Cliente",
            "9. Modificar Marca",
            "10. Crear Factura",
            "11. Imprimir Factura \n por nro de factura",
            "12. Crear Nueva \nBase De Datos",
            "13. Consultar Precio\n del producto",
            "14. Consultar por\n Palabra Clave",
            "15. Consultar por\n Area",
            "16. Consultar por\n Fecha de Actualizacion",
            "17. Consultar Productos \nSin Stock",
            "18. Consultar Total\n Del Dia",
            "19. Imprimir última\n factura",
            "20. Consultar Venta\n Anual",
            "21. Consultar Venta\n Mensual"
        ]
        listaDeFunciones = ["agregarArticulo",
            "agregarCliente",
            "agregarMarca",
            "eliminarArticulo",
            "eliminarCliente",
            "eliminarMarca",
            "modificarArticulo",
            "modificarCliente",
            "modificarMarca",
            "crearFactura",
            "imprimirFacturaPorNroDeFactura",
            "crearNuevaBaseDeDatos",
            "consultarPrecioDelProducto",
            "consultarPorPalabraClave",
            "consultarPorArea",
            "consultarPorFechaDeActualizacion",
            "consultarProductosSinStock",
            "consultarTotalDelDia",
            "imprimirUltimaFactura",
            "consultarVentaAnual",
            "consultarVentaMensual"
        ]
        listaBotones = []
        for nombreDeCadaBoton in listaNombres:
            for nombreDeFuncion in listaDeFunciones:
                if(listaNombres.index(nombreDeCadaBoton) == listaDeFunciones.index(nombreDeFuncion)):
                    listaBotones.append(tk.Button(self.parent,text = nombreDeCadaBoton,justify ="center",command = lambda : nombreDeFuncion, width=20, height=3))

        fila = 1
        columna = 0
        for boton in listaBotones:
            indiceBoton = listaBotones.index(boton)
            if(indiceBoton % 3 == 0):
                fila = fila + 1
                columna = 0
            boton.grid(row = fila, column = columna)
            columna = columna + 1
        return listaBotones

    def agregarArticulo(self):
        AgregarArticulo.ClaseAgregarArticulo.mostrarAgregarArticulo()

ROOT = tk.Tk()
ROOT.geometry("800x600")
ROOT['borderwidth'] = 10
ROOT['relief'] = 'sunken'
APP = UI(parent=ROOT)
APP.mainloop()
ROOT.destroy()

