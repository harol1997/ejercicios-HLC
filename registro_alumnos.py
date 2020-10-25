#https://www.freepik.es/iconos-populares
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
            indice_numero_alumnos = 0
            while indice_numero_alumnos < int(numero_alumnos):
                dni = input("Ingrese el dni: ")
                if dni in alumnos_matriculados:
                    print("Hey usted ya ha sido matriculado")
                else:
                    nombre = input("Ingrese su nombre: ")
                    #mostrar los cursos disponibles*************************************************************
                    print("Los cursos disponibles son: ")
                    indice = 1
                    for i in cursos:
                        print(f'{indice}. {i}')
                        indice += 1
                    #mostrar los cursos disponibles*************************************************************

                    #agregamos los cursos****************************************************************************
                    lista_cursos_matriculados_alumno = list()#empieza vacia para cada alumno que se está registrando
                    while True:#ciclo infinito*********************************************************
                        indice_curso = input("Ingrese el indice de curso que desea matricularse?-Para dejar de agregar cursos ingrese 0: ")
                        if indice_curso != "0":
                            if indice_curso.isdigit() == True:#"4"
                                indice_curso = int(indice_curso)#convertir de string a int
                                if indice_curso > 0 and indice_curso <= len(cursos):#si el indice está dentro del rango
                                    lista_cursos_matriculados_alumno.append(cursos[indice_curso-1])
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
                    indice_numero_alumnos += 1

        else:
            print("Solo puede ingresar numeros enteros.")

    elif opcion == "2":#buscar por el numero de dni
        dni = input("Ingrese el dni del alumno que desea encontrar.")
        if dni in alumnos_matriculados:
            print('Nombre:',alumnos_matriculados[dni][0])
            print('Cursos matriculados:',alumnos_matriculados[dni][1])
        else:
            print("No se encontraron resultados")

    elif opcion == "3":
        dni = input("Ingrese el dni que desea eliminar: ")

        if dni in alumnos_matriculados:
            alumnos_matriculados.pop(dni)
            print("El usuario ha sido eliminado con éxito.")
        else:
            print('No se encontraron resultados')

    elif opcion == "4":
        dni = input("Ingrese dni del usuario a editar: ")
        if dni in alumnos_matriculados:
            print("Los cursos disponibles son: ")
            indice_curso = 1
            for i in cursos:
                print(f'{indice_curso}. {i}')
                indice_curso += 1
            #agregamos los cursos****************************************************************************
            lista_cursos_matriculados_alumno = list()#empieza vacia para cada alumno que se está registrando
            while True:#ciclo infinito*********************************************************
                indice_curso = input("Ingrese el indice de curso que desea matricularse?-Para dejar de agregar cursos ingrese 0: ")
                if indice_curso != "0":
                    if indice_curso.isdigit() == True:#"4"
                        indice_curso = int(indice_curso)#convertir de string a int
                        if indice_curso > 0 and indice_curso <= len(cursos):#si el indice está dentro del rango
                            lista_cursos_matriculados_alumno.append(cursos[indice_curso-1])
                        else:
                            print("Hey. Ingrese uno de los indices que se muestra")
                        
                    else:
                        print("Solo puede ingresar numeros enteros")
                else: 
                    break
            #agregamos los cursos****************************************************************************

            #editar
            alumnos_matriculados[dni][1] = lista_cursos_matriculados_alumno


        else:
            print("No se encontraron resultados")

    elif opcion == "5":
        if len(alumnos_matriculados) != 0:
            for i in alumnos_matriculados:
                print(f'{i}: {alumnos_matriculados[i]}')
        else:
            print("No se han registrado alumnos")
    
    elif opcion == "6":#terminamos con la ejecución del while
        break

    else:
        print("Ha ingresao una opcion incorrecta")

    seguir = input("Desea continuar ? y/n: ")#creamos la variable seguir , que me va permitir saber si el usuario continua con el programa o no

#guardar datos en un bloc de notas

f = open('datos.txt','w')
for i in alumnos_matriculados:
    f.write(i+'\n')
f.close()

#*****************

#leyendo los datos

f = open('datos.txt','r')
print(f.read())
f.close()
