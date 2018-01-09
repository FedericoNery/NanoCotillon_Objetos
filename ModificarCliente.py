from tkinter import *
from tkinter import ttk
import BaseDeDatos

class GUIModificarCliente:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
        self.master = master
        master.title("MODIFICAR CLIENTE")
        master.geometry("565x500+400+50")

        self.labelNombreCliente = Label(self.master, text="Nombre del Cliente")
        self.labelNombreCliente.grid(row=0, column=1)

        self.labelDescripcion = Label(self.master, text="Resultado de Busqueda")
        self.labelDescripcion.grid(row=2, column=1)

        self.stringNombreCliente = StringVar()
        self.entryNombreCliente = ttk.Entry(self.master, textvariable=self.stringNombreCliente)
        self.entryNombreCliente.grid(row=1, column=1)

        self.stringResultado= StringVar()
        self.entryResultado = Entry(self.master, textvariable=self.stringResultado)
        self.entryResultado.grid(row=3, column=1, padx=5, pady=5)

        self.listboxClientes = Listbox(self.master, height=10)
        self.listboxClientes.grid(row=5, column=1)
        self.listboxClientes.insert(0, *self.baseDeDatos.devolverListaDeClientes())

        self.radioButtonPorNombre = Radiobutton(master, text="Por Nombre", value=1, command=self.selectorBuscarPorNombre,width=10,anchor="w")
        self.radioButoonPorLista = Radiobutton(master, text="Por Lista", value=2, command=self.selectorBuscarPorLista,width=10,anchor="w")
        self.radioButtonPorNombre.grid(row=0, column=0,sticky="W")
        self.radioButoonPorLista.grid(row=5, column=0,sticky="NW")
        self.selectorBuscarPorLista()

        self.intContacto = IntVar()
        self.entryNumContacto = Entry(self.master, textvariable=self.intContacto)
        self.entryNumContacto.delete(0, len(str(self.intContacto)))
        self.entryNumContacto.grid(row=1, column=2, padx=5, pady=5)

        self.labelNumeroDeTelefono = Label(self.master, text="Numero de Telefono")
        self.labelNumeroDeTelefono.grid(row=0, column=2)

        self.buttonAgregarCliente = Button(self.master, text="Buscar Cliente", command=self.buscarCliente, width=20, height=3)
        self.buttonAgregarCliente.grid(row=0, column=3, rowspan=3, padx=5)

        self.labelNumeroDeTelefono.configure(state="disabled")
        self.entryNumContacto.configure(state="disabled")

    def selectorBuscarPorNombre(self):
        self.labelNombreCliente.configure(state="normal")
        self.labelDescripcion.configure(state="normal")
        self.entryNombreCliente.configure(state="normal")
        self.entryResultado.configure(state="disabled")
        self.listboxClientes.configure(state="disabled")

    def selectorBuscarPorLista(self):
        self.labelNombreCliente.configure(state="disabled")
        self.labelDescripcion.configure(state="disabled")
        self.entryNombreCliente.configure(state="disabled")
        self.listboxClientes.configure(state="normal")

    def buscarCliente(self):
        self.radioButtonPorNombre.grid_forget()
        self.radioButoonPorLista.grid_forget()

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarCliente(self.root)
        self.root.mainloop()

root = Tk()
my_gui = GUIModificarCliente(root)
root.mainloop()
