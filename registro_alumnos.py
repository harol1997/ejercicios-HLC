import os

#VARIABLES CONSTANTES*************************
MENU = """1. Registrar
2. Buscar
3. Eliminar
4. Editar
5. Mostrar
6. Salir"""
#VARIABLES CONSTANTES*************************

seguir = 'y'
cursos = ('aritmetica','trigonometria','algebra')#los cursos en donde s e puede matricular el alumno
#nombre, dni, cursos
alumnos_matriculados = dict()#nuevo diccionario que almacenará los alumnos matriculados en el formato 'dni':[nombre,[cursos]]

while seguir != 'n':#
    
    os.system("cls")#limpiar la consola

    print("\t\t\tMENU")
    print("\t\t\t====")
    print(MENU)
    opcion = input("Ingrese una opcion: ")# 4 --> "4"

    if opcion == "1":#nombre,dni,cursos
        numero_alumnos = input("Cuantos alumnos desea registrar?: ")

        if numero_alumnos.isdigit() == True:
            for i in range(numero_alumnos):
                dni = input("Ingrese el dni")
                nombre = input("Ingrese su nombre")
                #mostrar los cursos disponibles*************************************************************
                print("Los cursos disponibles son: ")
                indice = 1
                for i in cursos:
                    print(f'{indice}. {i}')
                    indice += 1
                #mostrar los cursos disponibles*************************************************************

                #agregamos los cursos****************************************************************************
                lista_cursos_matriculados_alumno = list()#empieza vacia para cada alumno que se está registrando
                while True:#************
                    indice_curso = input("Ingrese el indice de curso que desea matricularse?-Para dejar de agregar cursos ingrese 0")
                    if indice_curso != "0":
                        if indice_curso.isdigit() == True:
                            indice_curso = int(indice_curso)
                            if indice_curso > 0 and indice_curso <= len(cursos):
                                lista_cursos_matriculados_alumno.append(cursos[indice_curso-1])
                                break
                            else:
                                print("Hey. Ingrese uno de los indices que se muestra")
                            
                        else:
                            print("Solo puede ingresar numeros enteros")
                    else: 
                        break
                #agregamos los cursos****************************************************************************
                
                #registramos el alumno***************************************************************************
                alumnos_matriculados[dni] = [nombre,lista_cursos_matriculados_alumno]
                #registramos el alumno***************************************************************************

        else:
            print("Solo puede ingresar numeros enteros.")

    elif opcion == "2":#buscar por el numero de dni
        dni = input("Ingrese el dni del alumno que desea encontrar.")

    elif opcion == "3":
        print("Ha ingresado 3")

    elif opcion == "4":
        print("Ha ingresado 4")

    elif opcion == "5":
        print("Ha ingresado 5")
    
    elif opcion == "6":#terminamos con la ejecución del while
        break

    else:
        print("Ha ingresao una opcion incorrecta")

    seguir = input("Desea continuar ? y/n: ")#creamos la variable seguir , que me va permitir saber si el usuario continua con el programa o no
