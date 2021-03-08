class Lista():
    def __init__(self, nombre, fila = None, columna = None):
        self.fila = fila
        self.columna = columna
        self.nombre = nombre        
        self.matriz = None
        self.matrizReducida = None
        self.repeticiones = None
        self.siguiente = None

    """ def __init__(self, nombre,fila, columna):
        self.fila = fila 
        self.columna = columna
        self.nombre = nombre        
        self.matriz = None
        self.matrizReducida = None
        self.reduccion = False
        self.siguiente = None """