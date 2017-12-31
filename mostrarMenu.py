from tkinter import Tk, Label, Button
import claseDePrueba
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text=self.textoVentanaPrincipalEncabezado())
        self.label.grid(row = 0, column = 1)

        self.agregarArticulo_button = Button(master, text="1. Agregar Articulo", command = self.agregarArticulo, width = 20, height = 3)
        self.agregarArticulo_button.grid(row = 1, column = 0)

        self.agregarArticulo_button = Button(master, text="2. Agregar Cliente", command=self.agregarCliente, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="3. Agregar Marca", command=self.agregarMarca, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="4. Eliminar Articulo", command=self.eliminarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="5. Eliminar Cliente", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="6. Eliminar Marca", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="7. Modificar Articulo", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="8. Modificar Cliente", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="9. Modificar Marca", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="10. Crear Factura", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="11. Imprimir Factura \n por nro de factura", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="12. Crear Nueva \nBase De Datos", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="13. Consultar Precio\n del producto", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="14. Consultar por\n Palabra Clave", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="15. Consultar por\n Area", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="16. Consultar por\n Fecha de Actualizacion", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text= "17. Consultar Productos \nSin Stock", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="18. Consultar Total\n Del Dia", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="19. Imprimir última\n factura", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text= "20. Consultar Venta\n Anual", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)

        self.agregarArticulo_button = Button(master, text="21. Consultar Venta\n Mensual", command=self.agregarArticulo, width=20, height=3)
        self.agregarArticulo_button.grid(row=1, column=0)


    def agregarArticulo(self):
       claseDePrueba.GUIAgregarArticulo.crearVentana(self)

    def textoVentanaPrincipalEncabezado(self):
        return """NANO COTILLON
    Sistema de consulta y registro de los productos
    Creado por : Federico Nery
    """







root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()