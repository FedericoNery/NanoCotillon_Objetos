from tkinter import *
from tkinter import messagebox
import BaseDeDatos
class GUIEliminarArticulo:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.master = master
        master.title("ELIMINAR ARTICULO")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Codigo de Barra")
        self.labelCodigo.grid(row=0, column=0)

        self.intCodigo = IntVar()
        self.entryCodigo = Entry(self.master, textvariable=self.intCodigo)
        self.entryCodigo.grid(row=1, column=0,padx=5)

        self.buttonAgregarMarca = Button(self.master, text="Eliminar Articulo", command=self.eliminarArticulo, width=20, height=3)
        self.buttonAgregarMarca.grid(row=0, column=1, rowspan=3, padx=10)

    def eliminarArticulo(self):
        try:
            codigoDeBarras = self.intCodigo.get()
            self.baseDeDatos.setComandoSql('UPDATE ARTICULOS SET ALTA_BAJA = 0 WHERE CODIGO_DE_BARRA = {} '.format(str(codigoDeBarras)))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
            self.master.destroy()
        except:
            if(self.intCodigo.get() == ""):
                messagebox.showinfo(parent=self.master, message='INGRESE EL CODIGO DEL PRODUCTO', icon="error", title="ATENCION", type="ok")
            else:
                messagebox.showinfo(parent=self.master, message='NO EXISTE ESE ARTICULO', icon="error", title="ATENCION", type="ok")

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIEliminarArticulo(self.root)
        self.root.mainloop()
"""
root = Tk()
my_gui = GUIEliminarArticulo(root)
root.mainloop()
"""