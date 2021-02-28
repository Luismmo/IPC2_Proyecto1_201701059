from xml.dom import minidom
import os
from listaCircular import ListaEnlazada
import time

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
                input('generando grafica')
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
            self.matrices.insertar(matriz.attributes['nombre'].value)
            fila = matriz.getAttribute('n')
            columna = matriz.getAttribute('m')
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
                    filas.retornarEn(x).binario+='0'
                else:
                    filas.retornarEn(x).binario+='1'
            self.matrices.retornarEn(contador).matriz= filas
            contador+=1                            
            print('Matriz cargada exitosamente.')
            time.sleep(0.4)
        #print(nombres[0].attributes['nombre'].value)
        print(self.matrices.retornarEn(1).nombre)
        print('acceso binario: '+self.matrices.retornarEn(1).matriz.retornarEn(1).binario)
        self.matrices.retornarEn(1).matriz.retornarEn(1).mostrarNodos()
        input('\nProceso terminado, presione ENTER para continuar.')

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