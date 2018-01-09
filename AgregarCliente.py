from tkinter import *
from tkinter import ttk
import BaseDeDatos
from tkinter import messagebox

class GUIAgregarCliente:
    def __init__(self, master):
        self.baseDeDatos = BaseDeDatos.BaseDeDatos()
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
        nombreDelCliente = nombreDelCliente.upper()
        if (self.verificarQueNoExistaElCliente(nombreDelCliente)):
            try:
                numeroDeTelefonoDelCliente = self.intContacto.get()
                if(self.verificarNumeroDeTelefono(numeroDeTelefonoDelCliente)):
                    self.baseDeDatos.setComandoSql('INSERT INTO CLIENTES(NOMBRE,NUMERO_TELEFONO,ALTA_BAJA) VALUES("{}",{},1);'.format(nombreDelCliente, str(numeroDeTelefonoDelCliente)))
                    self.baseDeDatos.ejecutarComandoSQL()
                    self.baseDeDatos.guardarBaseDeDatos()
                else:
                    messagebox.showinfo(parent=self.master, message='INGRESE BIEN EL NUMERO', icon="warning", title="ATENCION!", type="ok")
            except:
                messagebox.showinfo(parent=self.master, message='COMPLETE LOS DATOS', icon="warning", title="ATENCION!", type="ok")
        else:
            messagebox.showinfo(parent=self.master, message='YA EXISTE EL CLIENTE', icon="warning", title="ATENCION!", type="ok")

    def verificarNumeroDeTelefono(self, numeroDeTelefono):
        if(str(numeroDeTelefono).isdigit() and (len(str(numeroDeTelefono)) == 8 or len(str(numeroDeTelefono)) == 10)):
            return True
        else:
            return False

    def verificarQueNoExistaElCliente(self,nombreDelCliente):
        self.baseDeDatos.setComandoSql('SELECT NOMBRE FROM CLIENTES WHERE NOMBRE="{}";'.format(nombreDelCliente))
        self.baseDeDatos.ejecutarComandoSQL()
        self.baseDeDatos.setElemento()
        try:
            nombreEncontrado = self.baseDeDatos.elemento[0]
            if(nombreEncontrado == nombreDelCliente):
                return False
        except:
            return True

    def crearVentana(self):
        self.root = Tk()
        self.my_gui = GUIAgregarCliente(self.root)
        self.root.mainloop()


