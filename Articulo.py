class Articulo():
    def __init__(self):
        self.codigoDeBarra = 0
        self.nombreArticulo = ""
        self.precio = 0.0
        self.idMarca = 0
        self.idArea = 0
        self.fechaActualizacion = ""
        self.stock = 0
        self.altaBaja = 0

    def setArticulo(self,codigoDeBarra,nombreArticulo,precio,idMarca,idArea,fechaActualizacion,stock,altaBaja):
        self.codigoDeBarra = codigoDeBarra
        self.nombreArticulo = nombreArticulo
        self.precio = precio
        self.idMarca = idMarca
        self.idArea = idArea
        self.fechaActualizacion = fechaActualizacion
        self.stock = stock
        self.altaBaja = altaBaja