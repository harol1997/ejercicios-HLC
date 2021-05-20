class Complejo:

    def __init__(self, parte_entera=0, parte_compleja=0):
        self.parte_entera = parte_entera
        self.parte_compleja = parte_compleja

    @staticmethod
    def suma(*numeros_complejos):
        partes_enteras = [numero.parte_entera for numero in numeros_complejos]
        partes_imaginarias = [numero.parte_compleja for numero in numeros_complejos]

        suma_enteros = sum(partes_enteras)
        suma_complejos = sum(partes_imaginarias)

        return Complejo(suma_enteros, suma_complejos)

    def __str__(self):
        return f"{self.parte_entera} + {self.parte_compleja}i"

numero1 = Complejo(1, 2)
numero2 = Complejo(2, 5)

resultado =   Complejo.suma(numero1, numero2)

print(f"{numero1} + {numero2} = {resultado}")