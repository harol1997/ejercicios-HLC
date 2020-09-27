"""
9.	Dado un número natural de 4 cifras diseñe una algoritmo que permita obtener la suma de sus dígitos. Así, si se lee el numero 2358, el algoritmo deberá mostrar 18 (2+3+5+8 = 18).
"""
num=int(input("ingrese un numero entero de 4 cifras: "))

d1 = (num//1000)
residuo = (num%1000)
d2 = (residuo//100)
residuo = residuo % 100
d3 = (residuo//10)
residuo = (residuo % 10)
d4 = residuo 
resultado=(d1+d2+d3+d4)
print(d1)
print(d2)
print(d3)
print(d4)
print("El resultado es: ",resultado)
