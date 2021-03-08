from nodoMatriz import Lista

class ListaEnlazada:
    def __init__(self):
        self.tamanio = 0
        self.frecuenciaBinaria = ''
        self.flag = False
        self.inicio = None
    
    def insertar(self, dato):
        nuevo = Lista(dato)
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
            self.tamanio+=1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
            else:
                temporal = self.inicio            
                while temporal.siguiente != self.inicio:
                    temporal = temporal.siguiente
                temporal.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
    
    def insertar2(self, dato,x,y):
        nuevo = Lista(dato,x,y)
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
            self.tamanio+=1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
            else:
                temporal = self.inicio            
                while temporal.siguiente != self.inicio:
                    temporal = temporal.siguiente
                temporal.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
    
    def insertarLi(self, dato):
        nuevo = dato
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
            self.tamanio+=1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
            else:
                temporal = self.inicio            
                while temporal.siguiente != self.inicio:
                    temporal = temporal.siguiente
                temporal.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.tamanio+=1
    
    def retornarEn(self, indice):
        temporal = self.inicio
        contador = 1
        while contador < indice:
            contador+=1
            temporal = temporal.siguiente
        return temporal
    
    def eliminarEn(self,indice):
        
        self.retornarEn(indice-1).siguiente = self.retornarEn(indice+1)
        self.tamanio-=1
        

    def longitud(self):
        return self.tamanio

    def mostrarNodos(self):
        temporal = self.inicio
        size = 0
        while size < self.tamanio:
            size+=1
            print('-'+ str(temporal.nombre))
            temporal = temporal.siguiente
    
    def vaciarLista(self):
        self.inicio = None
    
    def esVacia(self):
        vacia = True
        if self.tamanio==0:
            return vacia
        else:
            vacia = False
            return False