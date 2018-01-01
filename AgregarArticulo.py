from tkinter import Tk, Label, Button
from tkinter import ttk
from tkinter import *
import BaseDeDatos
import Articulo

class GUIAgregarArticulo:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.baseDeDatos.conectarConBaseDeDatos()

        self.miArticulo = Articulo.Articulo()

        self.master = master
        master.title("AGREGAR ARTICULO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de Barra")
        self.labelCodigo.grid(row=0, column=1)
        self.labelDescripcion = Label(self.master, text="Descripción")
        self.labelDescripcion.grid(row=1, column=1)
        self.labelPrecio = Label(self.master, text="Precio")
        self.labelPrecio.grid(row=2, column=1)
        self.labelStock = Label(self.master, text="Stock")
        self.labelStock.grid(row=3, column=1)
        self.labelMarca = Label(self.master, text="Marca")
        self.labelMarca.grid(row=4, column=1)
        self.labelArea = Label(self.master, text="Area")
        self.labelArea.grid(row=5, column=1)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=6, column=1)

        self.stringNombre = StringVar()
        self.entryNombre = ttk.Entry(self.master, textvariable=self.stringNombre)
        self.entryNombre.grid(row=7, column=1)

        self.doublePrecio = DoubleVar()
        self.entryPrecio = ttk.Entry(self.master, textvariable=self.doublePrecio)
        self.entryPrecio.grid(row=8, column=1)

        self.intStock = IntVar()
        self.entryStock = ttk.Entry(self.master, textvariable=self.intStock)
        self.entryStock.grid(row=8, column=1)

        self.l = Listbox(self.master,listvariable=self.baseDeDatos.listaDeMarcas, height=10)
        self.l.grid(row=9, column=1)

        self.spinval = StringVar()
        self.s = Spinbox(self.master, values = self.baseDeDatos.listaDeAreas, textvariable=self.spinval)
        self.s.grid(row=10, column=1)

        self.buttonAgregarArticulo = Button(self.master, text="Agregar Articulo", command=self.agregarArticulo, width=20, height=3)
        self.buttonAgregarArticulo.grid(row=11, column=1)

    def agregarArticulo(self):
        if(self.verificarDatos()):
            self.baseDeDatos.setComandoSql('INSERT INTO ARTICULOS (CODIGO_DE_BARRA, NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK,ALTA_BAJA)'
                                           'VALUES({},"{}",{},{},{},{},{});')\
                .format(self.miArticulo.codigoDeBarra,self.miArticulo.nombreArticulo,self.miArticulo.precio,
                        self.miArticulo.idMarca,self.miArticulo.idArea,self.miArticulo.stock,self.miArticulo.altaBaja)

            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()

    def verificarDatos(self):
        self.estado = False
        try:
            self.miArticulo.setArticulo(self.intCodigo,self.stringNombre, self.doublePrecio,self.idMarca,self.idArea,self.fechaActualizacion
                                               ,self.intStock,1)
            self.estado = True

        except:
            ttk.messagebox.showinfo(message='VERIFIQUE LOS DATOS INGRESADOS', icon ="warning")
            self.estado = False

        return self.estado

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarArticulo(self.root)
        self.root.mainloop()


