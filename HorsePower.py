from xml.dom import minidom
import os
from listaCircular import ListaEnlazada
import time
from graphviz import Digraph
from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify

class HorsePower():
    def __init__(self):        
        self.gate = None    
        self.matrices = ListaEnlazada()
        
    def Menu(self):        
        salida = True        
        while salida:
            try:
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
                    self.escribirXML()
                elif opcion == 4:
                    self.datosEstudiante()
                elif opcion == 5:
                    self.graficar()
                elif opcion == 6:
                    self.Clrscr()
                    salida = False
                else:
                    input('\nIngrese una opción valida.')
            except:
                input('\nIngrese una opción válida. Presione ENTER y vuelva a intentarlo.')
    
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
            repeticiones = ListaEnlazada()
            repeticiones.vaciarLista()
            reduccion = ListaEnlazada()
            reduccion.vaciarLista()
            #accedo a las filas de una matriz en la lista general
            for i in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                #revisando si hay filas parecidas segun el patron de acceso
                repeticion = ListaEnlazada()                                
                repeticion.vaciarLista()
                newFila = ListaEnlazada()
                newFila.vaciarLista()
                for j in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                    #print('entro aqui')
                    if (i+1)!=(j+1):
                        if self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).frecuenciaBinaria == self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).frecuenciaBinaria and self.matrices.retornarEn(a+1).matriz.retornarEn(i+1).flag == False and self.matrices.retornarEn(a+1).matriz.retornarEn(j+1).flag == False:
                            if repeticion.esVacia()==True:
                                repeticion.insertar(i+1)
                                repeticion.insertar(j+1)
                                self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).flag = True
                                #******Nuevo ciclo for para sumar******#
                                for p in range(self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).tamanio):
                                    valor = int(self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).retornarEn(p+1).nombre) + int(self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).retornarEn(p+1).nombre)
                                    newFila.insertar(valor)
                            else:
                                repeticion.insertar(j+1)
                                self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).flag = True
                                #******Nuevo ciclo for para sumar******#
                                for p in range(self.matrices.retornarEn(a+1).matriz.retornarEn(i + 1).tamanio):
                                     newFila.retornarEn(p+1).nombre += int(self.matrices.retornarEn(a+1).matriz.retornarEn(j + 1).retornarEn(p+1).nombre)
                                    
                #print('repeticiones')
                #repeticion.mostrarNodos()
                if repeticion.esVacia() == False:
                    repeticiones.insertarLi(repeticion)
                    reduccion.insertarLi(newFila)
                time.sleep(0.1)
            self.matrices.retornarEn(a+1).repeticiones = repeticiones
            self.matrices.retornarEn(a+1).matrizReducida = reduccion

            if repeticiones.esVacia()==False:
                #self.matrices.retornarEn(a+1).repeticiones = repeticiones
                #reducida = ListaEnlazada()
                #reducida.vaciarLista()
                contador = 0
                for k in range(self.matrices.retornarEn(a+1).matriz.tamanio):
                    flag = False
                    for t in range(repeticiones.tamanio):
                        for b in range(repeticiones.retornarEn(t+1).tamanio):
                            if k+1 == repeticiones.retornarEn(t+1).retornarEn(b+1).nombre:
                                flag=True
                    if flag == False:
                        #print('entre en fila no coincide con nadie')
                        newfila = ListaEnlazada()
                        newfila.vaciarLista()
                        for u in range(self.matrices.retornarEn(a+1).matriz.retornarEn(k+1).tamanio):
                            newfila.insertar(self.matrices.retornarEn(a+1).matriz.retornarEn(k+1).retornarEn(u+1).nombre)
                        self.matrices.retornarEn(a+1).matrizReducida.insertarLi(newfila)
                        contador+=1
            for s in range(contador):
                listita = ListaEnlazada()
                listita.insertar(1)
                self.matrices.retornarEn(a+1).repeticiones.insertarLi(listita)

                        
            print('\nMatriz reducida')
            for n in range(self.matrices.retornarEn(a+1).matrizReducida.tamanio):
                print('fila '+ str(n+1))
                self.matrices.retornarEn(a+1).matrizReducida.retornarEn(n+1).mostrarNodos()        
        
        input('\nProceso terminado, presione ENTER para continuar.')

    def graficar(self):
        self.Clrscr()
        print('>Generar gráfica:\n')
        self.matrices.mostrarNodos()
        name = input('\nIngrese el nombre de la matriz a graficar: ')

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
                            #print('contenido de la lista id')
                            #listaid.mostrarNodos()
                            id2 = 'fila'+str(i+1)+str(j+1)
                            f.node(id2,self.matrices.retornarEn(a+1).matriz.retornarEn(i+1).retornarEn(j+1).nombre)
                            f.edge(str(listaid.retornarEn(j+1).nombre), id2)
                            listaid2.insertar(id2)
                        listaid.vaciarLista()
                        for k in range(columna):                            
                            listaid.insertar(listaid2.retornarEn(k+1).nombre) 
                        listaid2.vaciarLista()                        
                f.view()
    
    def escribirXML(self):
        self.Clrscr()
        print('> Escribiendo archivo XML, espere un momento...')
        top = Element('Matrices')
        for a in range(self.matrices.tamanio):
            fila = str(self.matrices.retornarEn(a+1).matrizReducida.tamanio)
            columna = str(self.matrices.retornarEn(a+1).columna)
            name = self.matrices.retornarEn(a+1).nombre+"_salida"
            grupo = self.matrices.retornarEn(a+1).repeticiones.tamanio
            child = SubElement(top,'Matriz', nombre = str(name), n = str(fila), m = str(columna),g = str(grupo))
            for i in range(self.matrices.retornarEn(a+1).matrizReducida.tamanio):
                for j in range(int(self.matrices.retornarEn(a+1).columna)):
                    row = i+1
                    column = j+1
                    child2 = SubElement(child, 'dato', x = str(row),y = str(column))
                    child2.text = str(self.matrices.retornarEn(a+1).matrizReducida.retornarEn(i+1).retornarEn(j+1).nombre)
            for h in range(int (grupo)):
                child3 = SubElement(child,'frecuencia', g = str(h+1))
                child3.text = str(self.matrices.retornarEn(a+1).repeticiones.retornarEn(h+1).tamanio)
                        
        file = open('salida.xml', 'w')
        file.write(str((prettify(top))))
        file.close()
        time.sleep(1.5)
        os.system('salida.xml')
    
    def cargarArchivo(self):
        try:
            self.Clrscr()
            ruta = input('Ingrese la ruta del archivo: ')
            mixml = minidom.parse(ruta)        
            self.gate = mixml
            input('\nCarga de archivo exitosa, presione ENTER para continuar.')
        except:
            input('Error al cargar el archivo, verifique por favor.')
    
    def datosEstudiante(self):
        self.Clrscr()
        print('Desarrollador: Luis Amilcar Morales Xón.')
        print('Carnet: 201701059.')
        print('Introducción a la programación y computación 2 sección "A".')
        print('Ingeniería en Ciencias y Sistemas.')
        print('4to semestre.')
        input('\nPresione ENTER para volver al menú principal.')