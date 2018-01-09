from tkinter import *
from tkinter import ttk
import Articulo
import BaseDeDatos
from tkinter import messagebox

class GUIModificarArticulo:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()

        self.master = master
        master.title("MODIFICAR ARTICULO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de Barra")
        self.labelCodigo.grid(row=0, column=1)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=1, column=1, padx=5, pady=5)

        self.labelDescripcion = Label(self.master, text="Descripción")
        self.labelPrecio = Label(self.master, text="Precio")
        self.labelStock = Label(self.master, text="Stock")
        self.labelMarca = Label(self.master, text="Marca")
        self.labelArea = Label(self.master, text="Area")

        self.stringNombre = StringVar()
        self.entryNombre = ttk.Entry(self.master, textvariable=self.stringNombre)

        self.doublePrecio = DoubleVar()
        self.entryPrecio = ttk.Entry(self.master, textvariable=self.doublePrecio)

        self.intStock = IntVar()
        self.entryStock = ttk.Entry(self.master, textvariable=self.intStock)

        self.listboxMarcas = Listbox(self.master, listvariable=self.baseDeDatos.listaDeMarcas, height=5)

        self.stringArea = StringVar()
        self.spinboxArea = Spinbox(self.master, values=self.baseDeDatos.listaDeAreas, textvariable=self.stringArea)

        self.buttonBuscarArticulo = Button(self.master, text="Buscar Articulo \n a Modificar", command=self.buscarCodigoDeBarras, width=20, height=3)
        self.buttonBuscarArticulo.grid(row=0, column=2, rowspan=3, padx=10)

        self.buttonModificarArticulo = Button(self.master, text="Modificar Articulo", command=self.modificarArticulo, width=20, height=3)


    def buscarCodigoDeBarras(self):
        pass

    def obtenerDatosDelArticulo(self,codigoDeBarrasIngresado):
        try:
            self.baseDeDatos.setComandoSql('SELECT * FROM ARTICULOS WHERE CODIGO_DE_BARRA={}'.format(codigoDeBarrasIngresado))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.setElemento()
            articulo = self.baseDeDatos.elemento
            self.mostrarElementosRestantes()
        except:
            messagebox.showinfo(parent=self.master, message='NO SE ENCONTRO EL ARTICULO', icon="error", title="ATENCION!", type="ok")

    def mostrarElementosRestantes(self):
        self.buttonModificarArticulo.grid(row=5, column=3, rowspan=3, padx=10)
        self.spinboxArea.grid(row=1, column=3)
        self.listboxMarcas.grid(row=3, column=2, rowspan=5)
        self.listboxMarcas.insert(0, *self.baseDeDatos.listaDeMarcas)
        self.entryStock.grid(row=5, column=1, padx=5, pady=5)
        self.entryPrecio.grid(row=3, column=1, padx=5, pady=5)
        self.entryNombre.grid(row=1, column=2, padx=5, pady=5)
        self.labelArea.grid(row=0, column=3)
        self.labelStock.grid(row=4, column=1)
        self.labelMarca.grid(row=2, column=2)
        self.labelDescripcion.grid(row=0, column=2)
        self.labelPrecio.grid(row=2, column=1)

    def setearElementosConSusValoresEncontrados(self):
        pass

    def modificarArticulo(self):
        pass

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarArticulo(self.root)
        self.root.mainloop()


root = Tk()
my_gui = GUIModificarArticulo(root)
root.mainloop()