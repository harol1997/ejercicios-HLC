#saber si un número es primo
def primo(nro):
    if nro <= 1:
        return False
    elif nro == 2:
        return True
    else:
        for i in range(2, nro):
            if nro%1 == 0:
                return False
        return True
        
print(primo(5))
