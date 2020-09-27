"""
Primera forma
1.	Construir un algoritmo que permita ingresar 3 números enteros positivos y que determine cual de ellos es el mayor, cual es el menor y cual es el numero medio.
"""
num1=int(input("ingrese el primer numero entero"))
num2=int(input("ingrese el segundo numero entero"))
num3=int(input("ingrese el tercer numero entero"))

if num1>num2 and num1>num3:
  print("El número mayor es:",num1)
  if num2>num3:
    print("El número del medio es:",num2)
    print("El menor es",num3)
  else:
    print("El número del medio es:",num3)
    print("El menor es",num2)

elif num2>num3 and num2>num1:
  print("El número mayor es:",num2)
  if num1>num3:
    print("El número del medio es:",num1)
    print("El menor es",num3)
  else:
    print("El número del medio es:",num3)
    print("El menor es",num1)

elif num3>num1 and num3>num2:
  print("El número mayor es:",num3)
  if num1>num2:
    print("El número del medio es:",num1)
    print("El menor es",num2)
  else:
    print("El número del medio es:",num2)
    print("El menor es",num1)

