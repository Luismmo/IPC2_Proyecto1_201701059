import os

class HorsePower():
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
                input('Cargando Archivo')
            elif opcion == 2:
                input('Procesando Archivo')
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
    
    def datosEstudiante(self):
        self.Clrscr()
        print('Desarrollador: Luis Amilcar Morales Xón.')
        print('Carnet: 201701059.')
        print('Introducción a la programación y computación 2 sección "A".')
        print('Ingeniería en Ciencias y Sistemas.')
        print('4to semestre.')
        input('\nPresione ENTER para volver al menú principal.')