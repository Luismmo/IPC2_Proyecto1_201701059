from nodoMatriz import Matriz

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
    
    def insertar(self, nombre, x, y):
        nuevo = Matriz(nombre,x,y)
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
            else:
                temporal = self.inicio            
                while temporal.siguiente != self.inicio:
                    temporal = temporal.siguiente
                temporal.siguiente = nuevo
                nuevo.siguiente = self.inicio
    
    def mostrarNodos(self):
        temporal = self.inicio
        while temporal.siguiente is not self.inicio:
            print('Matriz 1:'+temporal.nombre)
            temporal = temporal.siguiente
