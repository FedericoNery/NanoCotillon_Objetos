from tkinter import Tk, Label, Button
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import BaseDeDatos
import Articulo
import time
import AgregarMarca


class GUIAgregarArticulo:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()

        self.master = master
        master.title("AGREGAR ARTICULO")
        master.geometry("565x200+400+200")


        self.labelCodigo = Label(self.master, text="Codigo de Barra")
        self.labelCodigo.grid(row=0, column=1)
        self.labelDescripcion = Label(self.master, text="Descripción")
        self.labelDescripcion.grid(row=0, column=2)
        self.labelPrecio = Label(self.master, text="Precio")
        self.labelPrecio.grid(row=2, column=1)
        self.labelStock = Label(self.master, text="Stock")
        self.labelStock.grid(row=4, column=1)
        self.labelMarca = Label(self.master, text="Marca")
        self.labelMarca.grid(row=2, column=2)
        self.labelArea = Label(self.master, text="Area")
        self.labelArea.grid(row=0, column=3)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=1, column=1, padx=5, pady = 5)

        self.stringNombre = StringVar()
        self.entryNombre = ttk.Entry(self.master, textvariable=self.stringNombre)
        self.entryNombre.grid(row=1, column=2, padx=5, pady = 5)

        self.doublePrecio = DoubleVar()
        self.entryPrecio = ttk.Entry(self.master, textvariable=self.doublePrecio)
        self.entryPrecio.grid(row=3, column=1, padx=5, pady = 5)

        self.intStock = IntVar()
        self.entryStock = ttk.Entry(self.master, textvariable=self.intStock)
        self.entryStock.grid(row=5, column=1, padx=5, pady = 5)

        self.listboxMarcas = Listbox(self.master, listvariable=self.baseDeDatos.listaDeMarcas, height=5)
        self.listboxMarcas.grid(row=3, column=2, rowspan = 5)
        self.listboxMarcas.insert(0, *self.baseDeDatos.listaDeMarcas)

        self.stringArea = StringVar()
        self.spinboxArea = Spinbox(self.master, values = self.baseDeDatos.listaDeAreas, textvariable=self.stringArea)
        self.spinboxArea.grid(row=1, column=3)

        self.buttonAgregarArticulo = Button(self.master, text="Agregar Articulo", command=self.agregarArticulo, width=20, height=3)
        self.buttonAgregarArticulo.grid(row=2, column=3, rowspan=3, padx=10)

    def agregarArticulo(self):
        if(self.verificarDatos()):
            self.baseDeDatos.setComandoSql('INSERT INTO ARTICULOS (CODIGO_DE_BARRA, NOMBRE_ARTICULO,PRECIO,ARTICULO_MARCA,ARTICULO_AREA,STOCK,ALTA_BAJA)'
                                           'VALUES({},"{}",{},{},{},{},{});')\
                .format(self.miArticulo.codigoDeBarra,self.miArticulo.nombreArticulo,self.miArticulo.precio,
                        self.miArticulo.idMarca,self.miArticulo.idArea,self.miArticulo.stock,self.miArticulo.altaBaja)

            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
            messagebox.showinfo(parent=self.master, message='ARTICULO GUARDADO', icon="info", title="EXITO!", type="ok")
            self.master.destroy()

    def verificarDatos(self):
        self.estado = False
        try:
            fecha = time.strftime("%y/%m/%d")
            self.intCodigo = self.entryCodigo.get()
            self.stringNombre = self.entryNombre.get()
            self.doublePrecio = self.entryPrecio.get()

            codigoDeBarras = self.intCodigo
            nombre = self.stringNombre
            precio = self.doublePrecio

            self.stringArea = self.spinboxArea.get()
            idMarca = self.listboxMarcas.curselection()

            idArea = self.baseDeDatos.listaDeAreas.index(self.stringArea)
            stock = self.entryStock.get()


            if(len(idMarca) != 0):
                idMarca = idMarca[0]
                self.miArticulo.setArticulo(codigoDeBarras, nombre, precio, idMarca, idArea, fecha, stock, 1)
                self.estado = True
            else:
                self.master.destroy()
                self.baseDeDatos.cerrarBaseDeDatos()
                AgregarMarca.GUIAgregarMarca.crearVentana(self)
                self.estado = False
        except:
            messagebox.showinfo(parent=self.master,message='VERIFIQUE LOS DATOS INGRESADOS', icon ="warning", title="ERROR")
            self.estado = False

        return self.estado

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarArticulo(self.root)
        self.root.mainloop()


