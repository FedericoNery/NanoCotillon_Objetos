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
        self.entryPrecio.delete(0,len(str(self.doublePrecio)))

        self.intStock = IntVar()
        self.entryStock = ttk.Entry(self.master, textvariable=self.intStock)
        self.entryStock.delete(0,len(str(self.intStock)))

        self.listboxMarcas = Listbox(self.master, listvariable=self.baseDeDatos.listaDeMarcas, height=5)

        self.stringArea = StringVar()
        self.spinboxArea = Spinbox(self.master, values=self.baseDeDatos.listaDeAreas, textvariable=self.stringArea)

        self.buttonBuscarArticulo = Button(self.master, text="Buscar Articulo \n a Modificar", command=self.buscarCodigoDeBarras, width=20, height=3)
        self.buttonBuscarArticulo.grid(row=0, column=2, rowspan=3, padx=10)

        self.buttonModificarArticulo = Button(self.master, text="Modificar Articulo", command=self.modificarArticulo, width=20, height=3)


    def buscarCodigoDeBarras(self):
        self.obtenerDatosDelArticulo(self.intCodigo.get())

    def obtenerDatosDelArticulo(self,codigoDeBarrasIngresado):
        try:
            self.baseDeDatos.setComandoSql('SELECT * FROM ARTICULOS WHERE CODIGO_DE_BARRA={}'.format(codigoDeBarrasIngresado))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.setElemento()
            articulo = self.baseDeDatos.elemento
            self.setearElementosConSusValoresEncontrados(articulo)
            self.mostrarElementosRestantes()
        except:
            messagebox.showinfo(parent=self.master, message='NO SE ENCONTRO EL ARTICULO', icon="error", title="ATENCION!", type="ok")

    def mostrarElementosRestantes(self):
        self.buttonModificarArticulo.grid(row=0, column=3, rowspan=3, padx=10)
        self.spinboxArea.grid(row=4, column=3)
        self.listboxMarcas.grid(row=6, column=2, rowspan=5)
        self.listboxMarcas.insert(0, *self.baseDeDatos.listaDeMarcas)
        self.entryStock.grid(row=6, column=1, padx=5, pady=5)
        self.entryPrecio.grid(row=4, column=1, padx=5, pady=5)
        self.entryNombre.grid(row=4, column=2, padx=5, pady=5)
        self.labelArea.grid(row=3, column=3)
        self.labelStock.grid(row=5, column=1)
        self.labelMarca.grid(row=5, column=2)
        self.labelDescripcion.grid(row=3, column=2)
        self.labelPrecio.grid(row=3, column=1)

    def setearElementosConSusValoresEncontrados(self,articulo):
        self.miArticulo.setArticulo(articulo[0],articulo[1],articulo[2],articulo[3],articulo[4],articulo[5],articulo[6],articulo[7])
        self.entryPrecio.insert(0,self.miArticulo.precio)
        self.entryNombre.insert(0,self.miArticulo.nombreArticulo)
        self.entryStock.insert(0,self.miArticulo.stock)

    def modificarArticulo(self):
        try:
            comandoSQL = 'UPDATE ARTICULOS SET NOMBRE_ARTICULO = "{}", PRECIO = {}'.format(self.entryNombre.get(),str(self.entryPrecio.get()))
            idMarca = self.listboxMarcas.curselection()
            idMarca = idMarca[0] + 1
            idArea = self.baseDeDatos.listaDeAreas.index(self.stringArea.get()) + 1
            comandoSQL = comandoSQL + ',ARTICULO_MARCA = {},ARTICULO_AREA = {},'.format(idMarca,idArea)
            comandoSQL = comandoSQL + 'STOCK = {} WHERE CODIGO_DE_BARRA = {} ;'.format(str(self.entryStock.get()),str(self.entryCodigo.get()))
            self.baseDeDatos.setComandoSql(comandoSQL)
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
            self.master.destroy()
        except:
            messagebox.showinfo(parent=self.master, message='VERIFIQUE SI SELECCIONO \n TODOS LOS DATOS ', icon="error", title="ATENCION!", type="ok")

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarArticulo(self.root)
        self.root.mainloop()
"""
root = Tk()
my_gui = GUIModificarArticulo(root)
root.mainloop()
"""