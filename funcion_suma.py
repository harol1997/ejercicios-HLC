def suma_numeros(a):
    suma = 0
    for i in a:
        suma = suma + i

    return suma

lista_numeros = []

cant_numeros = int(input("Ingrese cuantos numeros: "))

for i in range(cant_numeros):
    a = int(input("Ingrese un número: "))
    lista_numeros.append(a)

suma_final = suma_numeros(lista_numeros)

print("La suma de los números es:",suma_final)
