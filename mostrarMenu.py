from six.moves import tkinter as tk


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
        self.etiqueta = tk.Label(self.parent,text = self.textoVentanaPrincipalEncabezado())
        self.etiqueta.grid(row = 0,column = 0)
        self.listaDeBotones = self.generarBotones()

    def textoVentanaPrincipalEncabezado(self):
        return """NANO COTILLON
    Sistema de consulta y registro de los productos
    Creado por : Federico Nery
    Colaboracion de : Lucas Kammann
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
            "11. Imprimir Factura por nro de factura",
            "12. Crear Nueva Base De Datos(solo para el técnico)",
            "13. Consultar Precio del producto",
            "14. Consultar por Palabra Clave",
            "15. Consultar por Area",
            "16. Consultar por Fecha de Actualizacion",
            "17. Consultar Productos Sin Stock",
            "18. Consultar Total Del Dia",
            "19. Imprimir última factura",
            "20. Consultar Venta Anual",
            "21. Consultar Venta Mensual"
        ]
        listaBotones = []
        for i in listaNombres:
            listaBotones.append(tk.Button(self.parent,text = i))

        fila = 1
        columna = 0
        for j in listaBotones:
            indiceBoton = listaBotones.index(j)
            if(indiceBoton % 3 == 0):
                fila = fila + 1
                columna = 0
            j.grid(row = fila, column = columna)
            columna = columna + 1
        return listaBotones


ROOT = tk.Tk()
ROOT.geometry("800x600")
APP = UI(parent=ROOT)
APP.mainloop()
ROOT.destroy()

