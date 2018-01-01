import sqlite3

class BaseDeDatos():
    def __init__(self):
        self.baseDeDatos = None
        self.cursorBaseDeDatos = None
        self.tabla = None
        self.elemento = None
        self.comandoSQL = ""
        self.listaDeAreas = []
        self.listaDeMarcas = []
        self.conectarConBaseDeDatos()
        self.definirCursor()
        self.extraerListaDeAreas()
        self.extraerListaDeMarcas()

    def conectarConBaseDeDatos(self):
        try:
            self.baseDeDatos = sqlite3.connect("C:/Users/Federico-PC/PycharmProjects/NanoCotillon_Objetos/nanoCotillon.db")
            print("todoOK")
        except:
            self.crearBaseDeDatosNueva()
            print("que onda la BD")

    def definirCursor(self):
        self.cursorBaseDeDatos = self.baseDeDatos.cursor()

    def ejecutarComandoSQL(self):
        self.cursorBaseDeDatos.execute(self.comandoSQL)

    def setTabla(self):
        self.tabla = self.cursorBaseDeDatos.fetchall()

    def setElemento(self):
        self.elemento = self.cursorBaseDeDatos.fetchone()

    def guardarBaseDeDatos(self):
        self.baseDeDatos.commit()

    def ejecutarVariosComandos(self):
        self.cursorBaseDeDatos.executescript(self.comandoSQL)

    def setComandoSql(self,comandoSQL):
        self.comandoSQL = comandoSQL

    def comandoSQLParaCrearBaseDeDatosNueva(self):
        comandoDeCreacion = """
        CREATE TABLE IF NOT EXISTS AREAS(ID_AREA INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_AREA TEXT);
        CREATE TABLE IF NOT EXISTS MARCAS(ID_MARCA INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_MARCA TEXT,ALTA_BAJA INTEGER);
        CREATE TABLE IF NOT EXISTS ARTICULOS( CODIGO_DE_BARRA INTEGER PRIMARY KEY, NOMBRE_ARTICULO TEXT,PRECIO REAL,
        ARTICULO_MARCA INTEGER,ARTICULO_AREA INTEGER,FECHA DATETIME DEFAULT CURRENT_TIMESTAMP,STOCK INTEGER, ALTA_BAJA INTEGER,
        FOREIGN KEY (ARTICULO_MARCA) REFERENCES MARCAS(ID_MARCA),
        FOREIGN KEY (ARTICULO_AREA) REFERENCES AREAS(ID_AREA));
        CREATE TRIGGER IF NOT EXISTS ACT_FECHA AFTER UPDATE OF PRECIO ON ARTICULOS FOR EACH ROW BEGIN UPDATE ARTICULOS SET FECHA = CURRENT_TIMESTAMP;END;

        CREATE TABLE IF NOT EXISTS CLIENTES(ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE TEXT,NUMERO_TELEFONO INTEGER
        ,ALTA_BAJA INTEGER);

        CREATE TABLE IF NOT EXISTS ART_FACT(ID_ART INTEGER,ID_FACT INTEGER, CANTIDAD INTEGER, PRECIO INTEGER,
        FOREIGN KEY (ID_ART) REFERENCES ARTICULOS(ID),
        FOREIGN KEY (ID_FACT) REFERENCES FACTURAS(ID));

        CREATE TABLE IF NOT EXISTS FACTURAS (ID_FACTURA	INTEGER PRIMARY KEY AUTOINCREMENT, FECHA DATETIME DEFAULT CURRENT_TIMESTAMP,
    	ID_CLIENTE INTEGER, FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE));

        INSERT INTO AREAS (NOMBRE_AREA) VALUES("COTILLON");
        INSERT INTO AREAS (NOMBRE_AREA) VALUES("REPOSTERIA");
        INSERT INTO AREAS (NOMBRE_AREA) VALUES("DESCARTABLES");
        INSERT INTO AREAS (NOMBRE_AREA) VALUES("SOUVENIRS");
       """
        return comandoDeCreacion

    def crearBaseDeDatosNueva(self):
       # self.conectarConBaseDeDatos()
       # self.definirCursor()
        self.setComandoSql(self.comandoSQLParaCrearBaseDeDatosNueva())
        self.ejecutarVariosComandos()
        self.guardarBaseDeDatos()
        self.setComandoSql("")

    def extraerListaDeMarcas(self):
        try:
            self.setComandoSql('SELECT NOMBRE_MARCA FROM MARCAS;')
            self.ejecutarComandoSQL()
            tablaDeMarcas = self.cursorBaseDeDatos.fetchall()
            for marca in tablaDeMarcas:
                self.listaDeMarcas.append(marca[0])
                print(marca[0])

        except:
            print("error lista marcas")


    def extraerListaDeAreas(self):
        try:
            self.setComandoSql('SELECT NOMBRE_AREA FROM AREAS;')
            self.ejecutarComandoSQL()
            tablaDeAreas = self.cursorBaseDeDatos.fetchall()
            for area in tablaDeAreas:
                self.listaDeAreas.append(area[0])

        except:
            print("error lista areas")

    def cerrarBaseDeDatos(self):
        self.baseDeDatos.close()

