# achar valor máximo com divisão e conquista

def maximo(lista):
    
    if len(lista)==1:
        return lista[0]

    meio = len(lista)//2
    l = maximo(lista[:meio])
    r = maximo(lista[meio:])

    if l > r:
        return l
    else:
        return r

lista = [12, 1, 4, 2, 55, 2, 44, 55]

print(maximo(lista))
