from listaCircular import ListaEnlazada

listaMatriz = ListaEnlazada()

listaMatriz.insertar('luis')
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
#print(listaMatriz.retornarIndice(8))
listaMatriz.retornarIndice(8).insertar('fila8, columna1')
listaMatriz.retornarIndice(8).insertar('fila8, columna2')
print(listaMatriz.retornarIndice(8).retornarIndice(1).nombre)
print(listaMatriz.retornarIndice(8).retornarIndice(2).nombre)
