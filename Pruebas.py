from listaCircular import ListaEnlazada
from xml.dom import minidom

listaMatriz = ListaEnlazada()

""" listaMatriz.insertar('luis')
listaMatriz.insertar('marvin')
listaMatriz.insertar('evelin')
listaMatriz.insertar('edwin')
listaMatriz.insertar('cesar')
listaMatriz.insertar('armando')
listaMatriz.insertar('Geovani')
print(listaMatriz.retornarIndice(1).nombre)
print(listaMatriz.retornarIndice(2).nombre)
print(listaMatriz.retornarIndice(7).nombre)
listaMatriz.mostrarNodos()
print("Tamaño: "+str(listaMatriz.tamanio))

fila = ListaEnlazada()
listaMatriz.insertarLi(fila)
listaMatriz.retornarIndice(8).insertar('fila8, columna1')
listaMatriz.retornarIndice(8).insertar('fila8, columna2')
print(listaMatriz.retornarIndice(8).retornarIndice(1).nombre)
print(listaMatriz.retornarIndice(8).retornarIndice(2).nombre) """
#Creo una lista de matrices
""" listaMatriz.insertar('Matriz 1')
listaMatriz.insertar('Matriz 2')
listaMatriz.insertar('Matriz 3')
listaMatriz.insertar('Matriz 4')
#creo una matriz
matriz1 = ListaEnlazada()
#creo las filas y las inserto
fila1 = ListaEnlazada()
fila2 = ListaEnlazada()
fila3 = ListaEnlazada()
matriz1.insertarLi(fila1)
matriz1.insertarLi(fila2)
matriz1.insertarLi(fila3)
#busco una matriz
print(listaMatriz.retornarIndice(1).nombre)
#asigno matriz al atributo
listaMatriz.retornarIndice(1).matriz = matriz1
#agrego elementos a la fila 1
listaMatriz.retornarIndice(1).matriz.retornarIndice(1).insertar('1')
listaMatriz.retornarIndice(1).matriz.retornarIndice(1).insertar('2')
listaMatriz.retornarIndice(1).matriz.retornarIndice(1).insertar('3')
print('fila 1')
listaMatriz.retornarIndice(1).matriz.retornarIndice(1).mostrarNodos()
#agrego elementos a la fila 2
listaMatriz.retornarIndice(1).matriz.retornarIndice(2).insertar('4')
listaMatriz.retornarIndice(1).matriz.retornarIndice(2).insertar('5')
listaMatriz.retornarIndice(1).matriz.retornarIndice(2).insertar('6')
print('fila 2')
listaMatriz.retornarIndice(1).matriz.retornarIndice(2).mostrarNodos() """
""" mixml = minidom.parse('Matriz2.xml')
matrices = mixml.getElementsByTagName('matriz')
for matriz in matrices:
    print(matriz.attributes['nombre'].value)
    print('filas: '+ matriz.getAttribute('n'))
    print('columnas: '+ matriz.getAttribute('m'))
    datos = matriz.getElementsByTagName('dato')
    for dato in datos:
        print('Fila: '+ dato.attributes['x'].value+'  valor: '+dato.firstChild.data)        

for a in range(10):
    print(a) """
listaMatriz.insertar(1)
listaMatriz.insertar(2)
listaMatriz.insertar(3)
listaMatriz.insertar(4)
listaMatriz.retornarEn(1).nombre+=listaMatriz.retornarEn(1).nombre
valor = listaMatriz.retornarEn(1).nombre+listaMatriz.retornarEn(2).nombre 
print(valor)