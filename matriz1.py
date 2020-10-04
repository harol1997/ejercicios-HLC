"""
1.	Ingresar números enteros a una matriz de tamaño N x M e intercambiar los elementos de la primera columna con la última columna.
"""
import os

os.system("cls")

lista_grande  = []

nro_filas = int(input("Ingrese número de filas: "))
nro_columnas = int(input("Ingrese número de columnas: "))


for i in range(nro_filas):#mis filas
    lista_corta = []
    for j in range(nro_columnas):#mis columnas
        numero = int(input("Ingrese un número: "))
        lista_corta.append(numero)
    lista_grande.append(lista_corta)
print("\nANTES DEL CAMBIO")
for i in lista_grande:
    print(i)

for i in range(nro_filas):#mis filas
    for j in range(nro_columnas):#mis columnas
        if j == 0:
            a = lista_grande[i][0]
            lista_grande[i][0] = lista_grande[i][-1]
            lista_grande[i][-1] = a 

print("\nDESPUES DEL CAMBIO") 
for i in lista_grande:
    print(i)
