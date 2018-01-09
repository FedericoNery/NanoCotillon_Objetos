from tkinter import *
from tkinter import messagebox
import BaseDeDatos

class GUIModificarMarca:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.master = master
        master.title("MODIFICAR MARCA")
        master.geometry("565x500+400+50")

        self.labelNombreCliente = Label(self.master, text="Seleccione la marca")
        self.labelNombreCliente.grid(row=0, column=0)

        self.labelNombreNuevoMarca = Label(self.master, text="Nombre nuevo de la marca")
        self.labelNombreNuevoMarca.grid(row=6, column=0)

        self.stringNombreNuevoMarca = StringVar()
        self.entryNombreNuevoMarca = Entry(self.master, textvariable=self.stringNombreNuevoMarca)
        self.entryNombreNuevoMarca.grid(row=7, column=0)

        self.listboxMarcas = Listbox(self.master, listvariable=self.baseDeDatos.listaDeMarcas, height=5)
        self.listboxMarcas.grid(row=1, column=0, rowspan=5)
        self.listboxMarcas.insert(0, *self.baseDeDatos.listaDeMarcas)

        self.buttonModificarMarca = Button(self.master, text="Modificar Marca", command=self.modificarMarca, width=20, height=3)
        self.buttonModificarMarca.grid(row=0, column=1, rowspan=3, padx=5)

        self.idDeMarca = 0

    def modificarMarca(self):
        try:
            numeroNombreAModificar = self.listboxMarcas.curselection()
            nombreAModificar = self.baseDeDatos.listaDeMarcas[numeroNombreAModificar[0]]
            self.determinarNumeroDeMarcaDelArticulo(nombreAModificar)
            nombreNuevo = self.stringNombreNuevoMarca.get()
            self.baseDeDatos.setComandoSql('UPDATE MARCAS SET NOMBRE_MARCA = "{}" WHERE ID_MARCA = {} '.format(nombreNuevo, self.idDeMarca))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
            self.master.destroy()
        except:
            messagebox.showinfo(parent=self.master, message='SELECCIONE MARCA', icon="warning", title="ATENCION!!", type="ok")

    def determinarNumeroDeMarcaDelArticulo(self,nombreDeLaMarca):
        try:
            nombreDeLaMarca = nombreDeLaMarca.upper()
            self.baseDeDatos.setComandoSql('SELECT MARCAS.ID_MARCA FROM MARCAS WHERE NOMBRE_MARCA ="{}";'.format(nombreDeLaMarca))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.setElemento()
            self.idDeMarca = self.baseDeDatos.elemento[0]
        except:
            messagebox.showinfo(parent=self.master, message='ERROR CON ID DE MARCA', icon="error", title="ATENCION", type="ok")


    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarMarca(self.root)
        self.root.mainloop()
        messagebox.showinfo(parent=self.master, message='SELECCIONES UNA MARCA E INGRESE EL NUEVO NOMBRE', icon="info", title="ATENCION", type="ok")

"""
root = Tk()
my_gui = GUIModificarMarca(root)
root.mainloop()
"""