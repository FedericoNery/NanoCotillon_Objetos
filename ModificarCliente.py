from tkinter import *
from tkinter import ttk
import BaseDeDatos
from tkinter import messagebox

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

        self.valorRadioButton = IntVar()
        self.radioButtonPorNombre = Radiobutton(master, text="Por Nombre", value=1, command=self.selectorBuscarPorNombre,width=10,anchor="w",variable=self.valorRadioButton)
        self.radioButoonPorLista = Radiobutton(master, text="Por Lista", value=2, command=self.selectorBuscarPorLista,width=10,anchor="w",variable=self.valorRadioButton)
        self.radioButtonPorNombre.grid(row=0, column=0,sticky="W")
        self.radioButoonPorLista.grid(row=5, column=0,sticky="NW")
        self.selectorBuscarPorLista()

        self.intContacto = IntVar()
        self.entryNumContacto = Entry(self.master, textvariable=self.intContacto)
        self.entryNumContacto.delete(0, len(str(self.intContacto)))
        self.entryNumContacto.grid(row=1, column=2, padx=5, pady=5)

        self.labelNumeroDeTelefono = Label(self.master, text="Numero de Telefono")
        self.labelNumeroDeTelefono.grid(row=0, column=2)

        self.buttonBuscarCliente = Button(self.master, text="Buscar Cliente", command=self.buscarCliente, width=20, height=3)
        self.buttonBuscarCliente.grid(row=0, column=3, rowspan=3, padx=5)

        self.labelNumeroDeTelefono.configure(state="disabled")
        self.entryNumContacto.configure(state="disabled")

        self.buttonModificarCliente = Button(self.master, text="Modificar Cliente", command=self.modificarCliente, width=20, height=3)

        self.numClienteDeLaLista = 0

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
        try:
            if(self.valorRadioButton.get() == 2):
                if(self.establecerDatosDelClientePorLista()):
                    self.radioButtonPorNombre.grid_forget()
                    self.radioButoonPorLista.grid_forget()

                    self.buttonModificarCliente.grid(row=3, column=3, rowspan=3, padx=5, sticky="n")
                    self.buttonBuscarCliente.configure(state="disabled")
                    self.listboxClientes.configure(state="disabled")
                else:
                    messagebox.showinfo(parent=self.master, message='NO SE PUDIERON \n ESTABLECER LOS DATOS', icon="error", title="ATENCION!", type="ok")
            else:
                messagebox.showinfo(parent=self.master, message='SELECCIONE POR LISTA', icon="warning", title="ATENCION!", type="ok")
        except:
            messagebox.showinfo(parent=self.master, message='SELECCIONE CLIENTE', icon="warning", title="ATENCION!", type="ok")

    def modificarCliente(self):
        try:
            nuevoNombre = self.stringNombreCliente.get()
            nuevoNumero = self.intContacto.get()
            self.baseDeDatos.setComandoSql('UPDATE CLIENTES SET NOMBRE = "{}",NUMERO_TELEFONO = {} WHERE ID_CLIENTE={};'.format(nuevoNombre, nuevoNumero, self.numClienteDeLaLista))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.guardarBaseDeDatos()
        except:
            messagebox.showinfo(parent=self.master, message='VERIFIQUE LOS DATOS', icon="warning", title="ATENCION!", type="ok")

    def establecerDatosDelClientePorLista(self):
        try:
            self.numClienteDeLaLista = self.listboxClientes.curselection()
            self.numClienteDeLaLista = self.numClienteDeLaLista[0] + 1
            self.baseDeDatos.setComandoSql('SELECT NOMBRE,NUMERO_TELEFONO FROM CLIENTES WHERE ID_CLIENTE="{}";'.format(self.numClienteDeLaLista))
            self.baseDeDatos.ejecutarComandoSQL()
            self.baseDeDatos.setElemento()
            datosDelCliente = self.baseDeDatos.elemento
            self.labelNombreCliente.configure(state="normal")
            self.entryNombreCliente.configure(state="normal")
            self.labelNumeroDeTelefono.configure(state="normal")
            self.entryNumContacto.configure(state="normal")
            self.entryNombreCliente.insert(0,datosDelCliente[0])
            self.entryNumContacto.insert(0,datosDelCliente[1])
            return True
        except:
            return False

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIModificarCliente(self.root)
        self.root.mainloop()

root = Tk()
my_gui = GUIModificarCliente(root)
root.mainloop()
