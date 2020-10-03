"""
1.	Ingresar números enteros y calcular la suma de dichos números. El algoritmo termina cuando se ingresa el numero cero. 
"""

suma = 0

while True:
    numero = int(input("Ingresar números enteros: "))
    if numero == 0:
        break
    suma = suma + numero

print("La suma de los números enteros es:",suma)
