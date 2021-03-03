from xml.dom import minidom
import os
from listaCircular import ListaEnlazada
import time
from graphviz import Digraph

class HorsePower():
    def __init__(self):        
        self.gate = None    
        self.matrices = ListaEnlazada()
        
    def Menu(self):
        salida = True        
        while salida:
            self.Clrscr()
            print('Menu Principal:\n')
            print('\t1. Cargar Archivo')
            print('\t2. Procesar Archivo')
            print('\t3. Escribir archivo de salida')
            print('\t4. Mostrar datos del estudiante')
            print('\t5. Generar Grafica')
            print('\t6. Salida')

            opcion = int(input('\n\tIngrese una opción: '))
            if opcion == 1:
                self.cargarArchivo()
            elif opcion == 2:
                self.procesarArchivo()
            elif opcion == 3:
                input('escribiendo Archivo')
            elif opcion == 4:
                self.datosEstudiante()
            elif opcion == 5:
                self.graficar()
            elif opcion == 6:
                self.Clrscr()
                salida = False
            else:
                input('\nIngrese una opción valida.')
    
    def Clrscr(self):
        os.system('cls')
    
    def procesarArchivo(self):
        self.Clrscr()
        print('Procesando archivo XML, cargando matrices...')
        nombres = self.gate.getElementsByTagName('matriz')    
        contador = 1
        for matriz in nombres:
            fila = matriz.getAttribute('n')
            columna = matriz.getAttribute('m')
            self.matrices.insertar2(matriz.attributes['nombre'].value, fila, columna)            
            filas = ListaEnlazada()
            for a in range(int(fila)):
                filax= ListaEnlazada()
                filas.insertarLi(filax)
            datos = matriz.getElementsByTagName('dato')
            for dato in datos:
                x = int(dato.attributes['x'].value)
                valor = dato.firstChild.data
                filas.retornarEn(x).insertar(valor)
                if int(valor) == 0:
                    filas.retornarEn(x).frecuenciaBinaria+='0'
                else:
                    filas.retornarEn(x).frecuenciaBinaria+='1'
            self.matrices.retornarEn(contador).matriz= filas
            contador+=1                            
            print('Matriz cargada exitosamente.')
            time.sleep(0.4)

        #print(nombres[0].attributes['nombre'].value)
        #print(self.matrices.retornarEn(1).nombre)
        #print('acceso binario: '+self.matrices.retornarEn(1).matriz.retornarEn(1).binario)
        #self.matrices.retornarEn(1).matriz.retornarEn(1).mostrarNodos()
        
        #parte de las matrices binarias 
        #accedo a las matrices en la lista general
        for a in range(self.matrices.tamanio):            
            binarioFlag = False
            print('\nCalculando matriz binaria: '+str(a+1))            
            matrizTemporal = ListaEnlazada()
            #accedo a las filas de una matriz en la lista general
            for i in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                #revisando si hay filas parecidas segun el patron de acceso
                filaNueva = ListaEnlazada()
                filaNueva.vaciarLista()                
                for j in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                    print('entro aqui')
                    
                    if self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).frecuenciaBinaria == self.matrices.retornarEn(a+1).matriz.retornarEn(j + 2).frecuenciaBinaria and self.matrices.retornarEn(a+1).matriz.retornarEn(j+2).flag == False and self.matrices.retornarEn(a+1).matriz.retornarEn(i+1).flag == False:
                        print('fila '+str(i+1)+'es igual a fila' + str(j+1))
                        self.matrices.retornarEn(a+1).reduccion = True                        
                        self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).flag=True
                        self.matrices.retornarEn(a+1).matriz.retornarEn(j + 2).flag=True
                        for z in range(self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).tamanio):
                            print('filas iguales, sumando')
                            indice = z+1
                            valor = int(self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).retornarEn(indice).nombre) + int(self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).retornarEn(indice).nombre)
                            filaNueva.insertar(valor)
                        matrizTemporal.insertarLi(filaNueva)            
                print('Reduciendo...')
                time.sleep(0.4)
            self.matrices.retornarEn(a+1).matrizReducida = matrizTemporal

        for i in range(self.matrices.tamanio):
            print(self.matrices.retornarEn(i+1).nombre)
            for j in range(self.matrices.retornarEn(i+1).matriz.tamanio):
                print('fila: '+ str((j+1)))
                self.matrices.retornarEn(i+1).matriz.retornarEn(j+1).mostrarNodos()
            if self.matrices.retornarEn(i+1).reduccion == True:
                for k in range(self.matrices.retornarEn(i+1).matrizReducida.tamanio):
                    print('fila: '+ str((k+1)))
                    self.matrices.retornarEn(i+1).matrizReducida.retornarEn(k+1).mostrarNodos()
        input('\nProceso terminado, presione ENTER para continuar.')

    def graficar(self):
        self.Clrscr()
        print('>Generar gráfica:\n')
        self.matrices.mostrarNodos()
        name = input('Ingrese el nombre de la matriz a graficar: ')

        for a in range(self.matrices.tamanio):
            if name == self.matrices.retornarEn(a+1).nombre:
                f = Digraph(filename = self.matrices.retornarEn(a+1).nombre , format='png', encoding='UTF-8')
                f.attr(rankdir = 'TB')
                f.attr('node', shape='ellipse')
                fila = self.matrices.retornarEn(a+1).fila
                column = self.matrices.retornarEn(a+1).columna
                f.node('fila','Filas: '+str(fila))
                f.node('columna','Columnas: '+ str(column))                
                f.node('raiz',self.matrices.retornarEn(a+1).nombre)
                f.edge('raiz','fila')
                f.edge('raiz','columna')
                listaid = ListaEnlazada()
                listaid2 = ListaEnlazada()
                for i in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                    #aqui adentro lista de filas
                    columna = int(column)
                    id = ''
                    id2 = ''
                    if i+1 == 1:
                        for j in range(columna):
                            #aqui adentro una fila
                            id = 'fila'+str(i+1)+str(j+1)
                            f.node(id,self.matrices.retornarEn(a+1).matriz.retornarEn(i+1).retornarEn(j+1).nombre)
                            f.edge('raiz', id)
                            listaid.insertar(id)
                    else:                        
                        for j in range(columna):
                            #aqui adentro una fila
                            print('contenido de la lista id')
                            listaid.mostrarNodos()
                            id2 = 'fila'+str(i+1)+str(j+1)
                            f.node(id2,self.matrices.retornarEn(a+1).matriz.retornarEn(i+1).retornarEn(j+1).nombre)
                            f.edge(str(listaid.retornarEn(j+1).nombre), id2)
                            listaid2.insertar(id2)
                        listaid.vaciarLista()
                        for k in range(columna):                            
                            listaid.insertar(listaid2.retornarEn(k+1).nombre) 
                        listaid2.vaciarLista()                        
                f.view()
    
    def cargarArchivo(self):
        self.Clrscr()
        ruta = input('Ingrese la ruta del archivo: ')
        mixml = minidom.parse(ruta)        
        self.gate = mixml
        input('\nCarga de archivo exitosa, presione ENTER para continuar.')
    
    def datosEstudiante(self):
        self.Clrscr()
        print('Desarrollador: Luis Amilcar Morales Xón.')
        print('Carnet: 201701059.')
        print('Introducción a la programación y computación 2 sección "A".')
        print('Ingeniería en Ciencias y Sistemas.')
        print('4to semestre.')
        input('\nPresione ENTER para volver al menú principal.')