from tkinter import *
from tkinter import ttk
import BaseDeDatos
from tkinter import messagebox

class GUIAgregarMarca:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()

        self.master = master
        master.title("AGREGAR MARCA")
        master.geometry("565x500+400+50")


        self.labelNombreMarca = Label(self.master, text="Nombre de Marca")
        self.labelNombreMarca.grid(row=0, column=1, padx=10)

        self.stringNombreMarca = StringVar()
        self.entryNombreMarca = ttk.Entry(self.master, textvariable=self.stringNombreMarca)
        self.entryNombreMarca.grid(row=1, column=1, padx=10)

        self.buttonAgregarMarca = Button(self.master, text="Agregar Marca", command=self.agregarMarca, width=20, height=3)
        self.buttonAgregarMarca.grid(row=0, column=2, rowspan=3, padx=10)

    def agregarMarca(self):
        try:
            self.stringNombreMarca = self.entryNombreMarca.get()
            self.baseDeDatos.setComandoSql('INSERT INTO MARCAS (NOMBRE_MARCA,ALTA_BAJA) VALUES("{}",1);'.format(self.stringNombreMarca))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
            self.baseDeDatos.cerrarBaseDeDatos()
            messagebox.showinfo(parent=self.master, message='MARCA GUARDADA', icon="info", title="EXITO!", type="ok")
            self.master.destroy()
        except:
            messagebox.showinfo(parent=self.master, message='NOSE QUE ONDA', icon="warning", title="ERROR", type="ok")
    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarMarca(self.root)
        self.root.mainloop()


