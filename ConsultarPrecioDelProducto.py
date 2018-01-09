from tkinter import *
from tkinter import ttk
import Articulo
import BaseDeDatos
from tkinter import messagebox

class GUIConsultarPrecioDelProducto:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.miArticulo = Articulo.Articulo()
        self.master = master
        master.title("PRECIO DEL PRODUCTO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de barra")
        self.labelCodigo.grid(row=0, column=0)

        self.intCodigo = IntVar()
        self.entryCodigo = ttk.Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=0, column=1, padx=5, pady=5)

        self.buttonBuscarPrecio = Button(self.master, text="Buscar precio \n del producto", command=self.buscarPrecioDeUnArticulo, width=15, height=2)
        self.buttonBuscarPrecio.grid(row=0, column=2, rowspan=3, padx=10)

        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=5, column=0,columnspan=3)

        self.resultadosObtenidos = Text(self.master, width=50, height=10, state="disabled", font="Courier",relief=SUNKEN)
        self.resultadosObtenidos.grid(row=6, column=0, columnspan=6)

    def buscarPrecioDeUnArticulo(self):
        try:
            codigoDeBarrasDelArticuloBuscado = self.intCodigo.get()
            self.baseDeDatos.setComandoSql(
                'SELECT * FROM (ARTICULOS) INNER JOIN MARCAS ON ARTICULO_MARCA = ID_MARCA WHERE CODIGO_DE_BARRA ={};'.format(
                    codigoDeBarrasDelArticuloBuscado))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.setElemento()
            self.setearArticuloConElementoBD()

            encabezado = ["Descripcion","Precio","Stock"]
            self.resultadosObtenidos.config(state=NORMAL)
            self.resultadosObtenidos.insert(END,"Descripcion \t")
            self.resultadosObtenidos.insert(END,"Precio \t")
            self.resultadosObtenidos.insert(END,"Stock")
            self.resultadosObtenidos.insert(END, "\n")
            self.resultadosObtenidos.insert(END,self.miArticulo.nombreArticulo+"\t")
            self.resultadosObtenidos.insert(END, str(self.miArticulo.precio)+"\t")
            self.resultadosObtenidos.insert(END, str(self.miArticulo.stock)+"\t")
            self.resultadosObtenidos.config(state=DISABLED)
        except:
            messagebox.showinfo(parent=self.master, message='NO SE ENCONTRO ARTICULO', icon="error", title="ERROR!", type="ok")

    def setearArticuloConElementoBD(self):
        articuloBuscado = self.baseDeDatos.elemento
        self.miArticulo.setArticulo(articuloBuscado[0],articuloBuscado[1],articuloBuscado[2],articuloBuscado[3],articuloBuscado[4],articuloBuscado[5],articuloBuscado[6],articuloBuscado[7])

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIConsultarPrecioDelProducto(self.root)
        self.root.mainloop()

"""
root = Tk()
my_gui = GUIConsultarPorPalabraClave(root)
root.mainloop()
"""