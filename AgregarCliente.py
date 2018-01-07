from tkinter import *
from tkinter import ttk

class GUIAgregarCliente:
    def __init__(self, master):
        self.master = master
        master.title("AGREGAR CLIENTE")
        master.geometry("565x500+400+50")

        self.labelCodigo = Label(self.master, text="Nombre de Cliente")
        self.labelCodigo.grid(row=0, column=0)
        self.labelPrecio = Label(self.master, text="Numero de Telefono")
        self.labelPrecio.grid(row=0, column=1)

        self.stringNombreCliente = StringVar()
        self.entryNombreCliente = ttk.Entry(self.master, textvariable=self.stringNombreCliente)
        self.entryNombreCliente.grid(row=1 , column=0)

        self.intContacto = IntVar()
        self.entryContacto = Entry(self.master, textvariable=self.intContacto)
        self.entryContacto.grid(row=1, column=1, padx=5, pady=5)

        self.buttonAgregarCliente = Button(self.master, text="Agregar Cliente", command=self.agregarCliente, width=20, height=3)
        self.buttonAgregarCliente.grid(row=0, column=2, rowspan=3, padx=10)

    def agregarCliente(self):
        nombreDelCliente = self.stringNombreCliente.get()
        noExisteCliente = verificarQueNoExistaElCliente(nombreDelCliente)

        if (noExisteCliente):
            numeroDeTelefonoDelCliente = ingreso_de_datos.ingresoNumeroDelCliente()
            comandoSQL = 'INSERT INTO CLIENTES(NOMBRE,NUMERO_TELEFONO,ALTA_BAJA) VALUES("{}",{},1);'.format(nombreDelCliente, numeroDeTelefonoDelCliente)
            funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
            funciones_SQLite.guardarBaseDeDatos(baseDeDatos)
        else:
            print("Ya existe el cliente")

    def verificarQueNoExistaElCliente(nombreDelCliente):
        comandoSQL = 'SELECT NOMBRE FROM CLIENTES;'
        funciones_SQLite.ejecutarComandoSQL(comandoSQL, cursorBaseDeDatos)
        tablaNombresDeClientes = funciones_SQLite.extraerTabla(cursorBaseDeDatos)

        for nombre in tablaNombresDeClientes:
            if (nombre[0] == nombreDelCliente):
                return False
        return True

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarCliente(self.root)
        self.root.mainloop()


