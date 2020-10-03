"""
3.	En un proceso repetitivo se ingresan las edades de las personas, se desea saber cuantas personas mayores de edad hay y cuantas menores de edad. El proceso termina cuando se ingresa el cero. 
"""

cant_mayores = 0
cant_menores = 0
edad_limit = 18

while True:
    edad = int(input("Ingresa tu edad: "))
    if edad == 0:
        break
    if edad >= edad_limit:#mayor de edad
        cant_mayores = cant_mayores +1
    else:#menor de edad
        cant_menores = cant_menores +1

print("La cantidad de mayores es:",cant_mayores)
print("La cantidad de menores es: ",cant_menores)
